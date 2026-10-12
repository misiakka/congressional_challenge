import streamlit as st

PAGES = ("Home", "Donate Food", "Find Food")


def go_to(page):
    """Use a non-widget session key for routing."""
    st.session_state.current_page = page
    st.rerun()


def render_sidebar():
    with st.sidebar:
        st.markdown('<div class="sidebar-brand">FoodRescue</div>', unsafe_allow_html=True)
        st.caption("Good food. Better communities.")
        st.divider()
        st.markdown('<p class="sidebar-label">EXPLORE</p>', unsafe_allow_html=True)
        for page in PAGES:
            selected = st.session_state.current_page == page
            if st.button(page, key=f"nav_{page}", use_container_width=True,
                         type="primary" if selected else "secondary"):
                go_to(page)
        st.divider()
        if st.session_state.get("logged_in"):
            st.caption(f"Signed in as {st.session_state.get('user_name', 'Member')}")
        else:
            st.caption("Sign up to join the community")
        st.caption("FoodRescue · Prototype")
