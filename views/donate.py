import streamlit as st
from components.cards import render_donation_card, safe_text
from data.donations import available_donations
from datetime import datetime

def render():
    # --------------------------------------------------

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




    #
