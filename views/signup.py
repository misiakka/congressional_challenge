"""Actual account registration and login, backed by SQLite."""
import re
import streamlit as st
from components.navigation import go_to
from data.database import DONOR, RECEIVER, authenticate, create_user


def render():
    st.title('Your FoodRescue account')
    st.caption('One account for donating or receiving food.')
    if st.session_state.user:
        user = st.session_state.user
        st.success(f"You're signed in as {user['name']}.")
        st.write(f"Account type: {user['role']}")
        if st.button('View My Activity'):
            go_to('My Activity')
        return

    _, middle, _ = st.columns([1, 2, 1])
    with middle:
        create_tab, login_tab = st.tabs(['Create account', 'Log in'])
        with create_tab:
            with st.form('create_account'):
                name = st.text_input('Full name', max_chars=100)
                email = st.text_input('Email address', max_chars=254)
                role = st.selectbox('I am a...', [DONOR, RECEIVER])
                password = st.text_input('Password (12+ characters)', type='password')
                confirm = st.text_input('Confirm password', type='password')
                submitted = st.form_submit_button('Create account', use_container_width=True)
            if submitted:
                if not name.strip() or not re.fullmatch(r'[^@\s]+@[^@\s]+\.[^@\s]+', email.strip()):
                    st.error('Enter your name and a valid email address.')
                elif password != confirm:
                    st.error('Your passwords do not match.')
                else:
                    try:
                        st.session_state.user = create_user(name, email, password, role)
                        go_to('My Activity')
                    except ValueError as error:
                        st.error(str(error))
        with login_tab:
            with st.form('login_account'):
                email = st.text_input('Email', key='login_email')
                password = st.text_input('Password', type='password', key='login_password')
                submitted = st.form_submit_button('Log in', use_container_width=True)
            if submitted:
                user = authenticate(email, password)
                if user:
                    st.session_state.user = user
                    go_to('My Activity')
                else:
                    st.error('Email or password is incorrect.')
    st.caption('Prototype notice: please use test information, not sensitive personal details.')


# Backward-compatible name used in earlier versions.
def show_signup():
    render()
