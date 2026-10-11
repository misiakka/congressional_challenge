from pathlib import Path
import streamlit as st
from data.state import initialize_state
from components.navigation import render_sidebar
from components.footer import render_footer
from views import home, donate, find_food

st.set_page_config(page_title="FoodRescue", page_icon="🌿", layout="wide", initial_sidebar_state="expanded")

css = (Path(__file__).parent / "styles" / "main.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

initialize_state()
page = render_sidebar()

if page == "Home":
    home.render()
elif page == "Donate Food":
    donate.render()
elif page == "Find Food":
    find_food.render()

render_footer()
