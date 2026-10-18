"""Food posting and donor-side management."""
import streamlit as st
from components.navigation import go_to
from components.cards import render_donation_card
from data.database import CATEGORIES, DONOR, add_donation, cancel_donation, list_donations


def render():
    st.title('Donate food')
    st.caption('Have extra food? Share what is available and when it can be picked up.')
    user = st.session_state.user
    if not user:
        st.info('Create an account or log in as a food donor to post a listing.')
        if st.button('Sign up to donate'):
            go_to('Account')
        return
    if user['role'] != DONOR:
        st.warning('Your account is set up to receive donations. Only donor accounts can post food.')
        return

    with st.form('donation_form', clear_on_submit=True):
        st.subheader('New donation')
        business = st.text_input('Business name *', max_chars=100)
        food = st.text_input('What food is available? *', placeholder='e.g. 20 fresh sandwiches', max_chars=150)
        one, two = st.columns(2)
        with one:
            quantity = st.number_input('Number of items or portions *', min_value=1, max_value=100000, value=10)
            location = st.text_input('Pickup neighborhood / location *', max_chars=150)
        with two:
            category = st.selectbox('Category', CATEGORIES)
            pickup = st.text_input('Pickup date and time *', placeholder='e.g. Oct 20, 3–5 PM', max_chars=120)
        notes = st.text_area('Notes (storage, allergens, packaging)', max_chars=1200)
        submitted = st.form_submit_button('Post donation', use_container_width=True)
    if submitted:
        try:
            add_donation(user['id'], business, food, quantity, category, pickup, location, notes)
            st.success('Your donation is live! Community organizations can now find it.')
        except ValueError as error:
            st.error(str(error))

    st.divider()
    st.subheader('Your donations')
    donations = list_donations(donor_id=user['id'])
    if not donations:
        st.info('You have not posted any donations yet.')
    for donation in donations:
        render_donation_card(donation)
        if donation['status'] == 'Claimed':
            st.caption(f"Claimed by: {donation['claimant_name']}")
        if donation['status'] == 'Available' and st.button('Cancel listing', key=f"cancel_{donation['id']}"):
            if cancel_donation(donation['id'], user['id']):
                st.rerun()
