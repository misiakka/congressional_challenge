
import streamlit as st

st.set_page_config(
    page_title="FoodRescue",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom styling
st.markdown("""
<style>
    .stApp {
        background-color: #FEFAE0;
        color: #283618;
    }

    h1, h2, h3 {
        color: #283618;
    }

    .hero {
        text-align: center;
        padding: 65px 20px;
    }

    .hero h1 {
        font-size: 58px;
        margin-bottom: 15px;
    }

    .hero p {
        font-size: 20px;
        color: #606C38;
    }

    .feature-card {
        background-color: #E9EDC9;
        padding: 25px;
        border-radius: 16px;
        min-height: 180px;
        margin-bottom: 15px;
    }

    .feature-card h3 {
        font-size: 22px;
    }

    .stButton > button {
        background-color: #606C38;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 25px;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #283618;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Navigation
left, right = st.columns([3, 2])

with left:
    st.markdown("### 🌱 FoodRescue")

with right:
    page = st.selectbox(
        "Navigation",
        ["Home", "Donate Food", "Find Food"],
        label_visibility="collapsed"
    )

st.divider()

# Homepage
if page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>Rescue Food. Nourish Communities.</h1>
        <p>
            Connecting surplus food with the people
            and communities who need it most.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("🍎 Donate Food"):
            st.session_state["page"] = "Donate Food"
            st.rerun()

    with col2:
        if st.button("🔎 Find Food"):
            st.session_state["page"] = "Find Food"
            st.rerun()

    with col3:
        if st.button("🌍 Our Mission"):
            st.session_state["show_mission"] = True

    if st.session_state.get("show_mission"):
        st.info(
            "Our mission is to reduce food waste "
            "while supporting communities experiencing "
            "food insecurity."
        )

    st.write("")
    st.write("")

    st.header("How FoodRescue Works")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🍎 1. Donate</h3>
            <p>
                Businesses list surplus food
                that would otherwise go to waste.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🤝 2. Connect</h3>
            <p>
                Our platform helps match donations
                with local community organizations.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🌱 3. Rescue</h3>
            <p>
                Organizations coordinate pickups
                and help distribute donated food.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.header("Our Impact")

    a, b, c = st.columns(3)

    a.metric("Food Rescued", "0 lbs")
    b.metric("Donations Completed", "0")
    c.metric("Community Partners", "0")

    st.caption("Impact statistics will update as donations are completed.")

elif page == "Donate Food":
    st.title("🍎 Donate Food")
    st.write("Donation form coming soon!")

elif page == "Find Food":
    st.title("🔎 Find Food")
    st.write("Available food listings coming soon!")
