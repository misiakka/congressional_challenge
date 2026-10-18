"""One navigation state, shared by the sidebar and every page button."""
import streamlit as st

PAGES = ('Home', 'Donate Food', 'Find Food', 'My Activity', 'Account')


def go_to(page):
    if page in PAGES:
        st.session_state.page = page
        st.rerun()


def render_sidebar():
    with st.sidebar:
        st.markdown('### FoodRescue')
        st.caption('Good food. Better communities.')
        st.divider()
        for page in PAGES:
            if st.button(page, key=f'nav_{page}', use_container_width=True,
                         type='primary' if st.session_state.page == page else 'secondary'):
                go_to(page)
        st.divider()
        user = st.session_state.get('user')
        if user:
            st.caption(f"Signed in as {user['name']}")
        else:
            st.caption('Sign in to post or claim donations.')
    return st.session_state.page
