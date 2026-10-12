
import sqlite3
import hashlib
import hmac
import secrets
from pathlib import Path

DB_PATH = Path(__file__).parent / "foodrescue.db"


def connect():
    return sqlite3.connect(DB_PATH, timeout=10)


def initialize_database():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                account_type TEXT NOT NULL
            )
        """)


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt),
        600000
    ).hex()


def create_account(name, email, password, account_type):
    email = email.strip().lower()
    name = name.strip()

    if not name or not email or not password:
        return False, "Please complete all fields."

    if len(password) < 12:
        return False, "Password must contain at least 12 characters."

    salt = secrets.token_hex(16)
    password_hash = hash_password(password, salt)

    try:
        with connect() as conn:
            conn.execute(
                """
                INSERT INTO users
                (name, email, password_hash, salt, account_type)
                VALUES (?, ?, ?, ?, ?)
                """,
                (name, email, password_hash, salt, account_type)
            )
        return True, "Account created successfully!"

    except sqlite3.IntegrityError:
        return False, "This email is already registered."


def authenticate_user(email, password):
    email = email.strip().lower()

    with connect() as conn:
        conn.row_factory = sqlite3.Row

        user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

    if user is None:
        return None

    attempted_hash = hash_password(password, user["salt"])

    if hmac.compare_digest(attempted_hash, user["password_hash"]):
        return {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "account_type": user["account_type"]
        }

    return None
