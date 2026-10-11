import streamlit as st
from components.cards import render_donation_card, safe_text
from data.donations import available_donations

def render():
    # --------------------------------------------------

    st.markdown(
        """
        <div class="hero-card">
            <h1>Good food deserves a second chance. 🌿</h1>
            <p>
                FoodRescue connects businesses with surplus food to
                food banks and community organizations that need it.
                Together, we can reduce food waste and help more
                people access nutritious food.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


    donations = st.session_state.donations
    available = available_donations()
    claimed = sum(
        1 for donation in donations
        if donation["status"] == "Claimed"
    )
    completed = st.session_state.completed_donations


    st.markdown("## Our community at a glance")
    st.markdown(
        '<p class="section-caption">A snapshot of activity in this demo.</p>',
        unsafe_allow_html=True,
    )


    metric1, metric2, metric3 = st.columns(3)


    with metric1:
        st.metric("Available listings", len(available))


    with metric2:
        st.metric("Claimed listings", claimed)


    with metric3:
        st.metric("Completed pickups", completed)


    st.write("")


    st.markdown("## How FoodRescue works")


    col1, col2, col3 = st.columns(3)


    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <h3>🏪 Donate surplus food</h3>
                <p>
                    Restaurants, grocery stores, cafes, and bakeries
                    can share food that is still suitable for donation.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <h3>🤝 Find a match</h3>
                <p>
                    Food banks and community organizations can browse
                    listings and find donations that fit their needs.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <h3>🌎 Make an impact</h3>
                <p>
                    Redistributing surplus food can reduce waste
                    and help direct more resources to local communities.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


    st.markdown("## Recently available food")


    recent = available[:3]


    if recent:
        for donation in recent:
            render_donation_card(donation)
    else:
        st.info("There are no available listings right now.")


    left, right = st.columns(2)


    with left:
        if st.button("Donate Food", key="home_donate", use_container_width=True):
            st.session_state.navigation = "Donate Food"
            st.rerun()


    with right:
        if st.button("Find Food", key="home_find", use_container_width=True):
            st.session_state.navigation = "Find Food"
            st.rerun()


    st.markdown(
        """
        <div class="info-card">
            <p>
                <strong>Our mission:</strong>
                Make it easier for businesses to donate surplus food
                and for community organizations to find it.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )




    #
