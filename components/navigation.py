import streamlit as st

def render_sidebar():
    # --------------------------------------------------


    with st.sidebar:
        st.markdown("# 🌿 FoodRescue")
        st.caption("Good food. Better communities.")
        st.divider()


        page = st.radio(
            "Navigation",
            ["Home", "Donate Food", "Find Food"],
            key="navigation",
        )


        st.divider()


        st.markdown("### How it works")
        st.markdown(
            """
            **1. Businesses** list surplus food.


            **2. Community organizations** find available donations.


            **3. Both sides** coordinate pickup to help reduce food waste.
            """
        )


        st.divider()
        st.caption("FoodRescue • Demo Prototype")




    #

    return page
