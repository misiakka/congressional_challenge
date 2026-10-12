import streamlit as st


def render():
    st.markdown('<p class="eyebrow">OUR MISSION</p>', unsafe_allow_html=True)

    intro, picture = st.columns([1.15, 1], gap="large", vertical_alignment="center")
    with intro:
        st.markdown(
            """
            <div class="mission-copy">
                <h1>Good food deserves a second chance.</h1>
                <p>FoodRescue connects businesses with surplus food to food banks
                and community organizations that can put it to good use.</p>
                <p>Our mission is to reduce avoidable food waste while helping
                communities access food with dignity.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if not st.session_state.get("logged_in", False):
            if st.button("Sign Up", key="mission_signup", type="primary"):
                st.session_state.home_navigation = "Sign Up"
                st.rerun()
        else:
            st.caption("Welcome to the FoodRescue community.")

    with picture:
        st.image("assets/food_rescue_produce.png", use_container_width=True)

    st.markdown("## How we hope to make a difference")
    first, second, third = st.columns(3, gap="medium")
    with first:
        st.markdown(
            '<div class="feature-card"><h3>Reduce food waste</h3>'
            '<p>Give surplus food a useful second life instead of sending it to waste.</p></div>',
            unsafe_allow_html=True,
        )
    with second:
        st.markdown(
            '<div class="feature-card"><h3>Support local communities</h3>'
            '<p>Help food banks and community organizations find food they can distribute.</p></div>',
            unsafe_allow_html=True,
        )
    with third:
        st.markdown(
            '<div class="feature-card"><h3>Make donating simpler</h3>'
            '<p>Offer one place to share food availability and coordinate pickup.</p></div>',
            unsafe_allow_html=True,
        )

    st.markdown("## How FoodRescue works")
    st.markdown(
        "Businesses post suitable surplus food. Community organizations "
        "browse available donations, claim listings, and coordinate pickup "
        "directly with donors."
    )
    st.caption("FoodRescue is currently a demonstration prototype.")
