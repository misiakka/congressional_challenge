import streamlit as st

PAGES = ["Home", "Donate Food", "Find Food", "Sign Up"]


def render_sidebar():
    # Home-page buttons request navigation before the radio widget is created.
    requested = st.session_state.pop("home_navigation", None)
    if requested in PAGES:
        st.session_state.current_page = requested

    with st.sidebar:
        st.markdown("# FoodRescue")
        st.caption("Good food. Better communities.")
        st.divider()

        page = st.radio("Navigation", PAGES, key="current_page")
        st.divider()
        st.caption("FoodRescue • Demo Prototype")
    return page
