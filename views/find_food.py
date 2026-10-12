import streamlit as st
from components.cards import render_donation_card, safe_text
from data.donations import available_donations

def render():
    # --------------------------------------------------

    st.title("Find Available Food")
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




    #
