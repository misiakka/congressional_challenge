
import streamlit as st
from components.navigation import go_to


def render():
    # HERO: TEXT ON THE LEFT, IMAGE ON THE RIGHT
    left, right = st.columns([1.1, 0.9], gap="large", vertical_alignment="center")

    with left:
        st.markdown(
            """
            <div class="hero-copy">
                <p class="hero-eyebrow">LESS WASTE. MORE GOOD.</p>
                <h1>Good food deserves a second chance.</h1>
                <p class="hero-description">
                    FoodRescue connects businesses with surplus food to food
                    banks and community organizations, helping good food reach
                    the people who need it.
                </p>
                <div class="hero-pills">
                    <span>Reduce food waste</span>
                    <span>Support communities</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        
        if not st.session_state.get("logged_in", False):
            if st.button(
                "Join FoodRescue →",
                key="mission_signup",
                type="primary",
            ):
                go_to("Sign Up")
        else:
            st.success("Welcome to the FoodRescue community!")


    with right:
        st.image(
            "assets/food_rescue_produce.png",
            use_container_width=True,
        )

    # INTRODUCTION TO THE FEATURES
    st.markdown(
        """
        <div class="section-heading">
            <p class="section-eyebrow">WHY FOODRESCUE</p>
            <h2>Small actions. Meaningful change.</h2>
            <p>
                Together, we can make surplus food a resource instead of waste.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    first, second, third = st.columns(3, gap="medium")

    with first:
        st.markdown(
            """
            <div class="feature-card">
                <div class="card-number">01</div>
                <h3>Keep good food in use</h3>
                <p>
                    Help prevent edible surplus food from going to waste
                    by connecting it with organizations that can use it.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with second:
        st.markdown(
            """
            <div class="feature-card">
                <div class="card-number">02</div>
                <h3>Support local communities</h3>
                <p>
                    Help food banks and community organizations access
                    donations for the people they serve.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with third:
        st.markdown(
            """
            <div class="feature-card">
                <div class="card-number">03</div>
                <h3>Make sharing simpler</h3>
                <p>
                    Bring donors and food-rescue organizations together
                    in one place to coordinate available food.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # HOW IT WORKS
    st.markdown(
        """
        <div class="section-heading how-it-works-heading">
            <p class="section-eyebrow">HOW IT WORKS</p>
            <h2>From surplus to shared.</h2>
            <p>A simple process that helps good food find a destination.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    step1, step2, step3 = st.columns(3, gap="medium")

    with step1:
        st.markdown(
            """
            <div class="process-card">
                <div class="process-icon">01</div>
                <h3>Businesses list food</h3>
                <p>
                    Businesses share details about suitable surplus food
                    available for donation.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with step2:
        st.markdown(
            """
            <div class="process-card">
                <div class="process-icon">02</div>
                <h3>Organizations find it</h3>
                <p>
                    Food banks and community organizations browse
                    available listings and claim donations.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with step3:
        st.markdown(
            """
            <div class="process-card">
                <div class="process-icon">03</div>
                <h3>Food reaches people</h3>
                <p>
                    Donors and recipient organizations coordinate pickup
                    so donations can be put to good use.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # CLOSING CALL TO ACTION
    st.markdown(
        """
        <div class="closing-banner">
            <p class="section-eyebrow">BE PART OF THE CHANGE</p>
            <h2>Let's give good food<br>a second chance.</h2>
            <p>
                Join a community working toward less food waste
                and stronger local food networks.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.get("logged_in", False):
        if st.button(
            "Get Started →",
            key="closing_signup",
            type="primary",
        ):
            st.session_state.home_navigation = "Sign Up"
            st.rerun()

    st.caption(
        "FoodRescue is a demonstration prototype. "
        "Donation availability and pickup arrangements depend on participating organizations."
    )
