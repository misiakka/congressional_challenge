import streamlit as st
from html import escape

def safe_text(value):
    """Escape text before displaying it inside custom HTML."""
    return escape(str(value))

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




#
