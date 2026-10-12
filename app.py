from pathlib import Path
import streamlit as st

st.set_page_config(page_title="FoodRescue", page_icon="🍏", layout="wide", initial_sidebar_state="collapsed")

from data.state import initialize_state
from data.accounts import initialize_database
from components.navigation import render_sidebar, go_to
from components.footer import render_footer
from views import home, donate, find_food
from views.signup import show_signup
from views.login import show_login

css_path = Path(__file__).parent / "styles" / "main.css"
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

initialize_database()
initialize_state()
for key, default in {
    "logged_in": False, "user_id": None, "user_name": "",
    "account_type": "", "current_page": "Home",
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

render_sidebar()

brand, actions = st.columns([5, 2], vertical_alignment="center")
with brand:
    st.markdown('<div class="brand-title">Food<span>Rescue</span></div>', unsafe_allow_html=True)
with actions:
    if st.session_state.logged_in:
        if st.button("Log Out", key="header_logout", use_container_width=True):
            for key, value in {"logged_in": False, "user_id": None, "user_name": "", "account_type": ""}.items():
                st.session_state[key] = value
            go_to("Home")
    else:
        left, right = st.columns(2, gap="small")
        with left:
            if st.button("Sign Up", key="header_signup", type="primary", use_container_width=True):
                go_to("Sign Up")
        with right:
            if st.button("Log In", key="header_login", use_container_width=True):
                go_to("Log In")

st.markdown('<div class="header-rule"></div>', unsafe_allow_html=True)
page = st.session_state.current_page

if page == "Home":
    home.render()
elif page == "Sign Up":
    show_signup()
elif page == "Log In":
    show_login()
elif page == "Donate Food":
    if not st.session_state.logged_in:
        st.info("Please log in to donate food.")
        if st.button("Log In to Donate", type="primary"):
            go_to("Log In")
    elif st.session_state.account_type != "Business / Food Donor":
        st.warning("Donation posting is available to Business / Food Donor accounts.")
    else:
        donate.render()
elif page == "Find Food":
    if not st.session_state.logged_in:
        st.info("Please log in to browse food listings.")
        if st.button("Log In to Find Food", type="primary"):
            go_to("Log In")
    elif st.session_state.account_type != "Food Bank / Community Organization":
        st.warning("Food claiming is available to Food Bank / Community Organization accounts.")
    else:
        find_food.render()
else:
    go_to("Home")

render_footer()
