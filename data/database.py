"""Small, readable SQLite layer for FoodRescue.

All SQL values use placeholders. A fresh connection per operation keeps the app
simple and avoids sharing connections between Streamlit sessions.
"""
import hashlib
import hmac
import os
import secrets
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / 'foodrescue.db'
CATEGORIES = ['Prepared Meals', 'Produce', 'Bakery', 'Dairy', 'Packaged Food', 'Other']
DONOR = 'Business / Food Donor'
RECEIVER = 'Food Bank / Community Organization'


def connect():
    connection = sqlite3.connect(DB_PATH, timeout=15)
    connection.row_factory = sqlite3.Row
    connection.execute('PRAGMA busy_timeout=15000')
    connection.execute('PRAGMA foreign_keys=ON')
    return connection


def initialize_database():
    with connect() as db:
        db.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE COLLATE NOCASE,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('Business / Food Donor', 'Food Bank / Community Organization')),
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )''')
        db.execute('''CREATE TABLE IF NOT EXISTS donations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            donor_id INTEGER NOT NULL REFERENCES users(id),
            business TEXT NOT NULL,
            food TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity > 0),
            category TEXT NOT NULL,
            pickup TEXT NOT NULL,
            location TEXT NOT NULL,
            notes TEXT NOT NULL DEFAULT '',
            status TEXT NOT NULL DEFAULT 'Available' CHECK(status IN ('Available','Claimed','Completed','Cancelled')),
            claimed_by INTEGER REFERENCES users(id),
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )''')
        db.execute('CREATE INDEX IF NOT EXISTS idx_donations_status ON donations(status)')


def password_digest(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), bytes.fromhex(salt), 600000).hex()


def create_user(name, email, password, role):
    if role not in (DONOR, RECEIVER):
        raise ValueError('Please select an account type.')
    if len(password) < 12:
        raise ValueError('Use a password with at least 12 characters.')
    salt = secrets.token_hex(16)
    try:
        with connect() as db:
            cursor = db.execute('INSERT INTO users(name,email,password_hash,salt,role) VALUES(?,?,?,?,?)',
                                (name.strip(), email.strip().lower(), password_digest(password, salt), salt, role))
            new_user_id = cursor.lastrowid
        return get_user(new_user_id)
    except sqlite3.IntegrityError as error:
        raise ValueError('An account with that email already exists.') from error


def get_user(user_id):
    with connect() as db:
        row = db.execute('SELECT id,name,email,role FROM users WHERE id=?', (user_id,)).fetchone()
        return dict(row) if row else None


def authenticate(email, password):
    with connect() as db:
        row = db.execute('SELECT * FROM users WHERE email=?', (email.strip().lower(),)).fetchone()
    if row and hmac.compare_digest(row['password_hash'], password_digest(password, row['salt'])):
        return get_user(row['id'])
    return None


def add_donation(donor_id, business, food, quantity, category, pickup, location, notes):
    user = get_user(donor_id)
    if not user or user['role'] != DONOR:
        raise ValueError('Only signed-in donor accounts can post donations.')
    if category not in CATEGORIES or not all(x.strip() for x in (business, food, pickup, location)):
        raise ValueError('Complete all required donation fields.')
    with connect() as db:
        cursor = db.execute('''INSERT INTO donations
            (donor_id,business,food,quantity,category,pickup,location,notes)
            VALUES(?,?,?,?,?,?,?,?)''',
            (donor_id, business.strip(), food.strip(), int(quantity), category,
             pickup.strip(), location.strip(), notes.strip()))
        return cursor.lastrowid


def list_donations(status=None, donor_id=None, claimed_by=None):
    query = '''SELECT d.*, u.name AS claimant_name FROM donations d
               LEFT JOIN users u ON u.id=d.claimed_by WHERE 1=1'''
    values = []
    if status:
        query += ' AND d.status=?'; values.append(status)
    if donor_id is not None:
        query += ' AND d.donor_id=?'; values.append(donor_id)
    if claimed_by is not None:
        query += ' AND d.claimed_by=?'; values.append(claimed_by)
    query += ' ORDER BY d.id DESC'
    with connect() as db:
        return [dict(row) for row in db.execute(query, values).fetchall()]


def claim_donation(donation_id, receiver_id):
    user = get_user(receiver_id)
    if not user or user['role'] != RECEIVER:
        return False
    with connect() as db:
        result = db.execute('''UPDATE donations SET status='Claimed', claimed_by=?
                               WHERE id=? AND status='Available' ''', (receiver_id, donation_id))
        return result.rowcount == 1


def complete_donation(donation_id, user_id):
    # Either the donor or the organization that claimed it can confirm pickup.
    with connect() as db:
        result = db.execute('''UPDATE donations SET status='Completed'
                               WHERE id=? AND status='Claimed'
                               AND (donor_id=? OR claimed_by=?)''', (donation_id, user_id, user_id))
        return result.rowcount == 1


def cancel_donation(donation_id, donor_id):
    with connect() as db:
        result = db.execute('''UPDATE donations SET status='Cancelled'
                               WHERE id=? AND donor_id=? AND status='Available' ''', (donation_id, donor_id))
        return result.rowcount == 1
