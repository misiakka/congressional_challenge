"""Search and claim available donations."""
import streamlit as st
from components.cards import render_donation_card
from components.navigation import go_to
from data.database import CATEGORIES, RECEIVER, claim_donation, list_donations


def render():
    st.title('Find food')
    st.caption('Browse available donations from local businesses.')
    search, category = st.columns([2, 1])
    with search:
        query = st.text_input('Search', placeholder='Food, business, or neighborhood')
    with category:
        selected = st.selectbox('Category', ['All categories'] + CATEGORIES)
    donations = list_donations(status='Available')
    matches = [item for item in donations if
               (selected == 'All categories' or item['category'] == selected) and
               (not query.strip() or query.lower().strip() in ' '.join(
                   str(item[key]) for key in ('food', 'business', 'location', 'notes')).lower())]
    st.caption(f'{len(matches)} available donation(s)')
    if not matches:
        st.info('No donations match yet. Try a different search or check back later.')
    user = st.session_state.user
    for donation in matches:
        render_donation_card(donation)
        if user and user['role'] == RECEIVER:
            if st.button('Claim this donation', key=f"claim_{donation['id']}", type='primary'):
                if claim_donation(donation['id'], user['id']):
                    st.success('Donation claimed! See My Activity for pickup details.')
                else:
                    st.warning('This donation is no longer available.')
                st.rerun()
        elif not user:
            st.caption('Log in as a community organization to claim this donation.')
    if not user and st.button('Sign up to claim food'):
        go_to('Account')
