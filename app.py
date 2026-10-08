import streamlit as st

st.title("FoodRescue")

food = st.text_input("Food item")
quantity = st.number_input("Quantity", min_value=1)

if st.button("Submit Donation"):
    st.success("Donation submitted!")