
import re
import streamlit as st
from components.navigation import go_to
from data.accounts import create_account


def show_signup():

    st.markdown(
        """
        <div class="hero-card">
            <h1>Join FoodRescue</h1>
            <p>Create an account and help good food find a new home.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    _, center, _ = st.columns([1, 2, 1])

    with center:

        if st.session_state.get("logged_in", False):
            st.success("You are already logged in!")

            if st.button("Go Home", use_container_width=True):
                go_to("Home")

            return

        st.subheader("Create an Account")

        with st.form("signup_form"):

            name = st.text_input("Full Name")
            email = st.text_input("Email Address")

            password = st.text_input(
                "Password",
                type="password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password"
            )

            account_type = st.selectbox(
                "I am a...",
                [
                    "Business / Food Donor",
                    "Food Bank / Community Organization"
                ]
            )

            submitted = st.form_submit_button(
                "Create Account",
                use_container_width=True,
                type="primary"
            )

        if submitted:

            if not re.fullmatch(
                r"[^@\s]+@[^@\s]+\.[^@\s]+",
                email.strip()
            ):
                st.error("Please enter a valid email address.")

            elif password != confirm_password:
                st.error("Passwords do not match.")

            else:
                success, message = create_account(
                    name,
                    email,
                    password,
                    account_type
                )

                if success:
                    go_to("Log In")
                else:
                    st.error(message)

        st.divider()

        st.write("Already have an account?")

        if st.button("Log In", use_container_width=True):
            go_to("Log In")
