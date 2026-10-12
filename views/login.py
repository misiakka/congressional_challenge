
import streamlit as st
from components.navigation import go_to
from data.accounts import authenticate_user


def show_login():

    st.markdown(
        """
        <div class="hero-card">
            <h1>Welcome Back</h1>
            <p>Log in to your FoodRescue account.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    _, center, _ = st.columns([1, 2, 1])

    with center:

        st.subheader("Log In")

        with st.form("login_form"):

            email = st.text_input("Email Address")

            password = st.text_input(
                "Password",
                type="password"
            )

            submitted = st.form_submit_button(
                "Log In",
                use_container_width=True,
                type="primary"
            )

        if submitted:

            user = authenticate_user(email, password)

            if user:

                st.session_state.logged_in = True
                st.session_state.user_id = user["id"]
                st.session_state.user_name = user["name"]
                st.session_state.account_type = user["account_type"]
                go_to("Home")

            else:
                st.error("Invalid email or password.")

        st.divider()

        st.write("Don't have an account?")

        if st.button("Create Account", use_container_width=True):
            go_to("Sign Up")
