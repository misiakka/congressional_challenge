
from pathlib import Path
import streamlit as st

from data.state import initialize_state
from components.navigation import render_sidebar
from components.footer import render_footer

from views import home, donate, find_food
from views.signup import show_signup


# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------

st.set_page_config(
    page_title="FoodRescue",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------
# LOAD CSS
# ---------------------------------------

css_path = Path(__file__).parent / "styles" / "main.css"

css = css_path.read_text(encoding="utf-8")

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True
)


# ---------------------------------------
# INITIALIZE SESSION STATE
# ---------------------------------------

initialize_state()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "account_type" not in st.session_state:
    st.session_state.account_type = ""

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"


# ---------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------

page = render_sidebar()


# ---------------------------------------
# DISPLAY PAGES
# ---------------------------------------

if page == "Home":
    home.render()

elif page == "Sign Up":
    show_signup()

elif page == "Donate Food":
    donate.render()

elif page == "Find Food":
    find_food.render()


# ---------------------------------------
# LOGOUT
# ---------------------------------------

if st.session_state.logged_in:

    with st.sidebar:

        st.divider()

        if st.button("Log Out", use_container_width=True):

            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.session_state.account_type = ""
            st.session_state.current_page = "Home"

            st.rerun()


# ---------------------------------------
# FOOTER
# ---------------------------------------

render_footer()
