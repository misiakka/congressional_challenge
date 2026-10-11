import streamlit as st

def render_footer():
    # --------------------------------------------------


    st.markdown("---")


    st.markdown(
        """
        <div class="footer">
            <strong> FoodRescue</strong>
            <p>Rescuing surplus food. Supporting local communities.</p>
            <p>Streamlit prototype • Built to explore food redistribution.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
