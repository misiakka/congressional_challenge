import streamlit as st
from datetime import datetime

def initialize_state():
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


    #
