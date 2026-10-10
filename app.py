

import streamlit as st
from datetime import datetime
from html import escape

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="FoodRescue",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# CUSTOM CSS — FOREST GREEN THEME
# --------------------------------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

    .stApp {
        background-color: #FEFAE0;
        color: #263D2A;
        font-family: 'DM Sans', sans-serif;
    }

    h1, h2, h3 {
        color: #263D2A;
        font-weight: 700;
    }

    p, label {
        color: #354A37;
    }

    [data-testid="stSidebar"] {
        background-color: #E3EBD9;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #263D2A;
    }

    .hero-card {
        background: linear-gradient(135deg, #355E3B, #263D2A);
        color: white;
        padding: 42px 36px;
        border-radius: 28px;
        margin-bottom: 28px;
    }

    .hero-card h1 {
        color: white;
        font-size: 42px;
        margin-bottom: 12px;
    }

    .hero-card p {
        color: #F4F6ED;
        font-size: 17px;
        line-height: 1.7;
    }

    .feature-card {
        background-color: #E3EBD9;
        padding: 26px;
        border-radius: 24px;
        min-height: 185px;
        margin-bottom: 18px;
        border: 1px solid #D3DFC9;
    }

    .feature-card h3 {
        margin-top: 0;
        color: #263D2A;
    }

    .feature-card p {
        line-height: 1.65;
    }

    .listing-card {
        background-color: #E3EBD9;
        padding: 24px;
        border-radius: 24px;
        margin-bottom: 18px;
        border: 1px solid #D3DFC9;
    }

    .listing-card h3 {
        margin-top: 0;
        margin-bottom: 10px;
    }

    .info-card {
        background-color: #EEF2E8;
        border-left: 5px solid #78966B;
        padding: 22px;
        border-radius: 20px;
        margin-bottom: 15px;
    }

    .info-card p {
        margin-bottom: 0;
    }

    .small-label {
        color: #526B51;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }

    .status-badge {
        display: inline-block;
        background-color: #D3E4CE;
        color: #263D2A;
        padding: 6px 12px;
        border-radius: 30px;
        font-size: 12px;
        font-weight: 700;
    }

    .section-caption {
        color: #526B51;
        font-size: 16px;
        margin-top: -8px;
        margin-bottom: 22px;
    }

    .stButton > button {
        background-color: #355E3B;
        color: white;
        border: 1px solid #355E3B;
        border-radius: 18px;
        padding: 12px 20px;
        font-weight: 600;
        transition: background-color 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #263D2A;
        color: white;
        border-color: #263D2A;
    }

    .stButton > button:focus {
        color: white;
        border-color: #78966B;
        box-shadow: 0 0 0 2px #D3E4CE;
    }

    .stTextInput input,
    .stTextArea textarea,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 12px;
    }

    div[data-testid="stMetric"] {
        background-color: #E3EBD9;
        padding: 22px;
        border-radius: 22px;
        border: 1px solid #D3DFC9;
    }

    div[data-testid="stMetricLabel"] {
        color: #526B51;
    }

    div[data-testid="stMetricValue"] {
        color: #263D2A;
    }

    hr {
        border-color: #D3DFC9;
    }

    .footer {
        text-align: center;
        color: #526B51;
        padding: 25px 0 10px 0;
        font-size: 13px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# SESSION STATE — DEMO DATA AND DONATIONS
# --------------------------------------------------

if "donations" not in st.session_state:
    st.session_state.donations = [
        {
            "id": 1,
            "business": "Green Leaf Cafe",
            "food": "Fresh sandwiches and wraps",
            "quantity": 25,
            "category": "Prepared Meals",
            "pickup": "Today, 6:00 PM",
            "location": "Manhattan, NY",
            "notes": "Individually packaged. Please bring insulated bags.",
            "status": "Available",
            "organization": "",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "id": 2,
            "business": "Sunrise Bakery",
            "food": "Bread, bagels, and pastries",
            "quantity": 40,
            "category": "Bakery",
            "pickup": "Today, 7:00 PM",
            "location": "Brooklyn, NY",
            "notes": "Assorted baked goods from today's inventory.",
            "status": "Available",
            "organization": "",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
        },
        {
            "id": 3,
            "business": "Fresh Market",
            "food": "Apples, bananas, and vegetables",
            "quantity": 30,
            "category": "Produce",
            "pickup": "Tomorrow, 10:00 AM",
            "location": "Queens, NY",
            "notes": "Fresh produce. Bring reusable crates if possible.",
            "status": "Available",
            "organization": "",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
        },
    ]

if "next_donation_id" not in st.session_state:
    st.session_state.next_donation_id = (
        max(
            (item["id"] for item in st.session_state.donations),
            default=0,
        )
        + 1
    )

if "completed_donations" not in st.session_state:
    st.session_state.completed_donations = 0

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def safe_text(value):
    """Escape text before displaying it inside custom HTML."""
    return escape(str(value))


def available_donations():
    """Return donations that have not been claimed or completed."""
    return [
        donation
        for donation in st.session_state.donations
        if donation["status"] == "Available"
    ]


def find_matches(category, location):
    """
    Simple rule-based matching demo.

    Prioritizes the same food category and location.
    This is not an AI model or a live location service.
    """
    matches = []

    for donation in available_donations():
        score = 0

        if category == "All Categories" or donation["category"] == category:
            score += 2

        if location.strip().lower() in donation["location"].lower():
            score += 1

        if score > 0:
            matches.append((score, donation))

    matches.sort(key=lambda item: item[0], reverse=True)
    return [donation for _, donation in matches]


def render_donation_card(donation):
    """Display a food listing using the site's card design."""
    st.markdown(
        f"""
        <div class="listing-card">
            <span class="status-badge">
                {safe_text(donation['status'])}
            </span>
            <h3>{safe_text(donation['food'])}</h3>
            <p>
                <strong>Donated by:</strong>
                {safe_text(donation['business'])}
            </p>
            <p>
                <strong>Quantity:</strong>
                {safe_text(donation['quantity'])} portions/items
            </p>
            <p>
                <strong>Category:</strong>
                {safe_text(donation['category'])}
            </p>
            <p>
                <strong>Pickup:</strong>
                {safe_text(donation['pickup'])}
            </p>
            <p>
                <strong>Location:</strong>
                {safe_text(donation['location'])}
            </p>
            <p>
                <strong>Additional details:</strong>
                {safe_text(donation['notes'] or 'No additional details provided.')}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

with st.sidebar:
    st.markdown("# 🌿 FoodRescue")
    st.caption("Good food. Better communities.")
    st.divider()

    page = st.radio(
        "Navigation",
        ["Home", "Donate Food", "Find Food"],
        index=0,
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


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if page == "Home":

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
            st.session_state.home_navigation = "Donate Food"
            st.rerun()

    with right:
        if st.button("Find Food", key="home_find", use_container_width=True):
            st.session_state.home_navigation = "Find Food"
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


# --------------------------------------------------
# DONATE FOOD PAGE
# --------------------------------------------------

elif page == "Donate Food":

    st.title("Donate Surplus Food 🌿")
    st.markdown(
        '<p class="section-caption">'
        'Help good food reach people who need it instead of going to waste.'
        '</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">
            <p>
                <strong>For food businesses:</strong>
                Add your organization and food details below.
                Please list only food that is safe and appropriate to donate.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("donation_form", clear_on_submit=True):

        st.markdown("### Business information")

        business = st.text_input(
            "Business or organization name *",
            placeholder="e.g., Green Leaf Cafe",
        )

        location = st.text_input(
            "Pickup location *",
            placeholder="e.g., Manhattan, NY",
        )

        st.markdown("### Food donation details")

        food = st.text_input(
            "Food items *",
            placeholder="e.g., Fresh sandwiches and salads",
        )

        col1, col2 = st.columns(2)

        with col1:
            quantity = st.number_input(
                "Quantity of portions/items *",
                min_value=1,
                max_value=100000,
                value=10,
                step=1,
            )

        with col2:
            category = st.selectbox(
                "Food category *",
                [
                    "Prepared Meals",
                    "Produce",
                    "Bakery",
                    "Dairy",
                    "Packaged Food",
                    "Other",
                ],
            )

        pickup = st.text_input(
            "Pickup time *",
            placeholder="e.g., Today, 6:00 PM",
        )

        notes = st.text_area(
            "Additional details",
            placeholder=(
                "Add storage instructions, packaging details, "
                "allergen information, or other pickup instructions."
            ),
        )

        submitted = st.form_submit_button(
            "Submit Food Donation",
            use_container_width=True,
        )

        if submitted:
            if not business.strip():
                st.error("Please enter your business or organization name.")
            elif not location.strip():
                st.error("Please enter the pickup location.")
            elif not food.strip():
                st.error("Please enter the food items.")
            elif not pickup.strip():
                st.error("Please enter the pickup time.")
            else:
                new_donation = {
                    "id": st.session_state.next_donation_id,
                    "business": business.strip(),
                    "food": food.strip(),
                    "quantity": int(quantity),
                    "category": category,
                    "pickup": pickup.strip(),
                    "location": location.strip(),
                    "notes": notes.strip(),
                    "status": "Available",
                    "organization": "",
                    "created_at": datetime.now().strftime("%Y-%m-%d"),
                }

                st.session_state.donations.insert(0, new_donation)
                st.session_state.next_donation_id += 1

                st.success(
                    "Your donation has been added to the available food listings!"
                )
                st.info(
                    "This prototype stores donations in the current "
                    "Streamlit session. It does not yet publish them to "
                    "a permanent database."
                )

    st.divider()

    st.markdown("## Your available donations")

    all_donations = [
        donation
        for donation in st.session_state.donations
        if donation["status"] == "Available"
    ]

    if all_donations:
        for donation in all_donations:
            render_donation_card(donation)
    else:
        st.info("No available donations have been listed yet.")


# --------------------------------------------------
# FIND FOOD PAGE
# --------------------------------------------------

elif page == "Find Food":

    st.title("Find Available Food 🤝")
    st.markdown(
        '<p class="section-caption">'
        'Explore available donations and find food that fits your organization’s needs.'
        '</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="info-card">
            <p>
                <strong>For food banks and community organizations:</strong>
                Search current demo listings by food type, location,
                or keywords. Review pickup details before claiming a listing.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        search_query = st.text_input(
            "Search food listings",
            placeholder="Search by food, business, or location...",
        )

    with col2:
        selected_category = st.selectbox(
            "Filter by category",
            [
                "All Categories",
                "Prepared Meals",
                "Produce",
                "Bakery",
                "Dairy",
                "Packaged Food",
                "Other",
            ],
        )

    available = available_donations()
    filtered = []

    for donation in available:
        matches_query = (
            not search_query.strip()
            or search_query.lower() in donation["food"].lower()
            or search_query.lower() in donation["business"].lower()
            or search_query.lower() in donation["location"].lower()
            or search_query.lower() in donation["notes"].lower()
        )

        matches_category = (
            selected_category == "All Categories"
            or donation["category"] == selected_category
        )

        if matches_query and matches_category:
            filtered.append(donation)

    st.markdown(f"### {len(filtered)} available listing(s)")

    if not filtered:
        st.info(
            "No listings match your search. Try a different keyword "
            "or choose another category."
        )

    for donation in filtered:
        render_donation_card(donation)

        with st.expander(
            f"Claim this donation from {donation['business']}"
        ):
            st.write(
                "Review the pickup information and enter your "
                "organization's name to claim this demo listing."
            )

            organization = st.text_input(
                "Food bank or organization name",
                key=f"organization_{donation['id']}",
                placeholder="e.g., Community Food Pantry",
            )

            if st.button(
                "Claim Donation",
                key=f"claim_{donation['id']}",
                use_container_width=True,
            ):
                if not organization.strip():
                    st.warning(
                        "Please enter your organization name before claiming."
                    )
                else:
                    for item in st.session_state.donations:
                        if item["id"] == donation["id"]:
                            item["status"] = "Claimed"
                            item["organization"] = organization.strip()
                            break

                    st.success(
                        "Donation marked as claimed in this demo. "
                        "Please coordinate pickup directly with the donor."
                    )
                    st.rerun()

    st.divider()

    st.markdown("## Donation tracking")

    claimed_donations = [
        donation
        for donation in st.session_state.donations
        if donation["status"] == "Claimed"
    ]

    completed_donations = [
        donation
        for donation in st.session_state.donations
        if donation["status"] == "Completed"
    ]

    track1, track2 = st.columns(2)

    with track1:
        st.metric("Awaiting pickup", len(claimed_donations))

    with track2:
        st.metric("Completed pickups", len(completed_donations))

    if claimed_donations:
        st.markdown("### Claimed donations")

        for donation in claimed_donations:
            st.markdown(
                f"""
                <div class="listing-card">
                    <h3>{safe_text(donation['food'])}</h3>
                    <p><strong>Donor:</strong> {safe_text(donation['business'])}</p>
                    <p><strong>Claimed by:</strong> {safe_text(donation['organization'])}</p>
                    <p><strong>Pickup:</strong> {safe_text(donation['pickup'])}</p>
                    <p><strong>Location:</strong> {safe_text(donation['location'])}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button(
                "Mark Pickup Completed",
                key=f"complete_{donation['id']}",
                use_container_width=True,
            ):
                for item in st.session_state.donations:
                    if item["id"] == donation["id"]:
                        item["status"] = "Completed"
                        break

                st.session_state.completed_donations += 1
                st.success("Pickup marked as completed in this demo.")
                st.rerun()

    if completed_donations:
        st.markdown("### Completed donations")

        for donation in completed_donations:
            st.markdown(
                f"""
                <div class="info-card">
                    <p>
                        <strong>{safe_text(donation['food'])}</strong>
                        — donated by {safe_text(donation['business'])}
                        and claimed by {safe_text(donation['organization'])}.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <div class="footer">
        <strong>🌿 FoodRescue</strong>
        <p>Rescuing surplus food. Supporting local communities.</p>
        <p>Streamlit prototype • Built to explore food redistribution.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
