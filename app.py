
from pathlib import Path

import streamlit as st

from data.database import initialize_database
from components.navigation import render_sidebar
from components.footer import render_footer
from views import activity, donate, find_food, home, signup


# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="FoodRescue",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# -----------------------------------
# LOAD CSS
# -----------------------------------

css_path = Path(__file__).parent / "styles" / "main.css"

if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )



initialize_database()
st.session_state.setdefault("user", None)
st.session_state.setdefault("page", "Home")


# -----------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------

page = render_sidebar()


# -----------------------------------
# ACCOUNT BUTTON
# -----------------------------------

_, account_action = st.columns([8, 1.15])

with account_action:

    if st.session_state.user:
        if st.button("Log Out", key="header_logout", use_container_width=True):
            st.session_state.user = None
            st.session_state.page = "Home"
            st.rerun()
    elif page != "Account":
        if st.button("Sign in / Sign up", key="header_signup", use_container_width=True):
            st.session_state.page = "Account"
            st.rerun()


# -----------------------------------
# PAGE ROUTING
# -----------------------------------

if page == "Home":
    home.render()
elif page == "Donate Food":
    donate.render()
elif page == "Find Food":
    find_food.render()
elif page == "My Activity":
    activity.render()
elif page == "Account":
    signup.render()


# -----------------------------------
# FOOTER
# -----------------------------------

render_footer()
