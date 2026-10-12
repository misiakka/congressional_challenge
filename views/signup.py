import re
import streamlit as st


def show_signup():
    st.markdown(
        """<div class="hero-card">
            <h1>Join FoodRescue</h1>
            <p>Create a demo profile and help good food find a new home.</p>
        </div>""",
        unsafe_allow_html=True,
    )

    _, center, _ = st.columns([1, 2, 1])
    with center:
        if st.session_state.get("logged_in", False):
            st.success("You're already using a demo profile.")
            if st.button("Go to Home", use_container_width=True):
                st.session_state.current_page = "Home"
                st.rerun()
            return

        st.subheader("Create your demo profile")
        st.caption("No password is needed for this prototype. This is not a real account.")
        with st.form("signup_form"):
            name = st.text_input("Full Name", placeholder="Your name")
            email = st.text_input("Email Address", placeholder="demo@example.com")
            account_type = st.selectbox(
                "I am a...",
                ["Business / Food Donor", "Food Bank / Community Organization"],
            )
            agreed = st.checkbox("I understand this is a demo profile, not a real account")
            submitted = st.form_submit_button("Join FoodRescue", use_container_width=True)

        if submitted:
            if not name.strip():
                st.error("Please enter your name.")
            elif not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()):
                st.error("Please enter a valid email format.")
            elif not agreed:
                st.error("Please confirm that you understand this is a demo.")
            else:
                # Only temporary demo display information is kept in this browser session.
                # No password, database account, or authentication is created.
                st.session_state.logged_in = True
                st.session_state.user_name = name.strip()
                st.session_state.account_type = account_type
                st.session_state.current_page = "Home"
                st.rerun()

        st.caption("Please use test information. Profiles disappear when the session ends.")
