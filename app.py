
from pathlib import Path

import streamlit as st

from data.database import initialize_database
from components.navigation import go_to
from components.footer import render_footer
from views import activity, donate, find_food, home, signup, demo


# Page configuration

st.set_page_config(
    page_title="FoodRescue",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# Load css

css_path = Path(__file__).parent / "styles" / "main.css"

if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )



initialize_database()
st.session_state.setdefault("user", None)
st.session_state.setdefault("page", "Home")


# Keep the brand and navigation together, rather than stacking two rows.
nav_items = ["Home", "Find Food", "Donate Food", "My Activity", "Demo Studio", "Account"]
header = st.container(key="site_navigation")
with header:
    brand, *nav_columns = st.columns([2.0, 0.8, 1, 1, 1, 1.1, 0.9], gap="small", vertical_alignment="center")
    with brand:
        st.markdown('<div class="fr-brand">🌿 FoodRescue<small>Good food. Better communities.</small></div>', unsafe_allow_html=True)
    for column, destination in zip(nav_columns, nav_items):
        with column:
            if st.button(destination, key=f"top_{destination}", use_container_width=True,
                         type="primary" if st.session_state.page == destination else "secondary"):
                go_to(destination)

page = st.session_state.page
if st.session_state.user:
    if st.button("Log out", key="logout"):
        st.session_state.user = None
        go_to("Home")

# Page routing

if page == "Home":
    home.render()
elif page == "Donate Food":
    donate.render()
elif page == "Find Food":
    find_food.render()
elif page == "My Activity":
    activity.render()
elif page == "Demo Studio":
    demo.render()
elif page == "Account":
    signup.render()


# Footer

render_footer()
