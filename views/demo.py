"""Demo walkthrough for businesses and food banks.

Demo donations live only in session state, not in the real database.
"""
import streamlit as st
from components.cards import render_donation_card
from data.database import CATEGORIES

# Fictional food listings used during presentations.
SAMPLE_DONATIONS = [
    {"id": 1, "business": "Sunrise Bakery (demo)", "food": "Fresh bread and pastries", "quantity": 40, "category": "Bakery", "pickup": "Today, 3–5 PM", "location": "Queens, NY", "notes": "Packaged and ready for pickup.", "status": "Available", "claimed_by": None},
    {"id": 2, "business": "Green Market (demo)", "food": "Mixed fresh vegetables", "quantity": 25, "category": "Produce", "pickup": "Tomorrow, 10 AM–12 PM", "location": "Manhattan, NY", "notes": "Assorted seasonal produce.", "status": "Available", "claimed_by": None},
    {"id": 3, "business": "Neighborhood Cafe (demo)", "food": "Prepared sandwiches", "quantity": 18, "category": "Prepared Meals", "pickup": "Today, 4–6 PM", "location": "Brooklyn, NY", "notes": "Keep chilled until pickup.", "status": "Available", "claimed_by": None},
]

def render():
    st.title("Explore both perspectives")
    st.caption("A safe, interactive walkthrough of both user experiences. All demo listings are fictional and remain separate from real accounts and donations.")
    st.session_state.setdefault("demo_role", "Business")
    st.session_state.setdefault("demo_items", [dict(item) for item in SAMPLE_DONATIONS])
    role = st.radio("View the app as", ["Business", "Food Bank"], horizontal=True, key="demo_role")
    st.markdown(f'<div class="demo-panel"><h3>{"Business dashboard" if role == "Business" else "Food bank dashboard"}</h3><p>{"Create and manage surplus food listings." if role == "Business" else "Browse donations and arrange pickups."}</p></div>', unsafe_allow_html=True)
    items = st.session_state.demo_items
    total = len(items)
    available = sum(item["status"] == "Available" for item in items)
    claimed = sum(item["status"] == "Claimed" for item in items)
    total_col, available_col, claimed_col = st.columns(3)
    total_col.metric("Demo listings", total)
    available_col.metric("Available", available)
    claimed_col.metric("Demo requests", claimed)
    if role == "Business":
        with st.expander("+ Create a donation", expanded=False):
            with st.form("demo_new_donation", clear_on_submit=True):
                business = st.text_input("Business name", value="Your local business")
                food = st.text_input("Food description", placeholder="e.g. Fresh apples")
                quantity = st.number_input("Portions / items", min_value=1, value=10)
                category = st.selectbox("Category", CATEGORIES)
                location = st.text_input("Pickup neighborhood", value="Queens, NY")
                pickup = st.text_input("Pickup window", value="Tomorrow, 2–4 PM")
                if st.form_submit_button("Add demo donation", type="primary"):
                    if not business.strip() or not food.strip() or not location.strip() or not pickup.strip():
                        st.warning("Please complete the donation details.")
                    else:
                        new_id = max((item["id"] for item in items), default=0) + 1
                        new_donation = {
                            "id": new_id,
                            "business": business.strip(),
                            "food": food.strip(),
                            "quantity": quantity,
                            "category": category,
                            "location": location.strip(),
                            "pickup": pickup.strip(),
                            "notes": "Demo donation",
                            "status": "Available",
                            "claimed_by": None,
                        }
                        items.insert(0, new_donation)
                        st.rerun()
        st.subheader("Your demonstration listings")
        for item in items:
            render_donation_card(item)
            if item["status"] == "Available" and st.button("Cancel listing", key=f"demo_cancel_{item['id']}"):
                item["status"] = "Cancelled"
                st.rerun()
            elif item["status"] == "Claimed":
                st.caption("Claimed by Hope Community Food Bank (demo)")
                if st.button("Simulate completed pickup", key=f"demo_complete_{item['id']}", type="primary"):
                    item["status"] = "Completed"
                    st.rerun()
    else:
        query = st.text_input("Search available food", placeholder="Try bakery, vegetables, Queens...")
        category = st.selectbox("Filter category", ["All categories"] + CATEGORIES)
        matches = []
        for item in items:
            if item["status"] != "Available":
                continue
            if category != "All categories" and item["category"] != category:
                continue
            searchable = " ".join(str(item[key]) for key in ("food", "business", "location"))
            if query.lower() in searchable.lower():
                matches.append(item)
        st.subheader("Available food")
        if not matches:
            st.info("No available demo donations match your filters.")
        for item in matches:
            render_donation_card(item)
            if st.button("Request food (demo)", key=f"demo_claim_{item['id']}", type="primary"):
                item["status"] = "Claimed"
                item["claimed_by"] = "Demo food bank"
                st.rerun()
        st.subheader("Your claimed donations")
        claimed_items = [i for i in items if i["claimed_by"] == "Demo food bank"]
        if not claimed_items:
            st.caption("Claim a listing above to see it appear here.")
        for item in claimed_items:
            render_donation_card(item)
    st.caption("Demo only: fictional listings and simulated actions. No real food has been distributed through this walkthrough.")
    st.divider()
    if st.button("Reset demonstration", use_container_width=True):
        st.session_state.demo_items = [dict(item) for item in SAMPLE_DONATIONS]
        st.rerun()
