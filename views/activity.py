"""A simple activity page for both sides of a donation."""
import streamlit as st
from components.navigation import go_to
from components.cards import render_donation_card
from data.database import DONOR, complete_donation, list_donations


def render():
    st.title('My activity')
    user = st.session_state.user
    if not user:
        st.info('Log in to see your donations and pickups.')
        if st.button('Go to account'):
            go_to('Account')
        return
    is_donor = user['role'] == DONOR
    items = list_donations(donor_id=user['id']) if is_donor else list_donations(claimed_by=user['id'])
    st.caption('Your posted donations' if is_donor else 'Donations your organization claimed')
    if not items:
        st.info('Nothing here yet. Your activity will appear when you post or claim food.')
    for item in items:
        render_donation_card(item)
        if item['status'] == 'Claimed':
            st.caption(f"Claimed by: {item['claimant_name']}")
            if st.button('Confirm pickup completed', key=f"finish_{item['id']}"):
                if complete_donation(item['id'], user['id']):
                    st.success('Pickup marked complete.')
                    st.rerun()
                else:
                    st.warning('This pickup cannot be updated.')
