import streamlit as st

# --------------------------------------------------


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
