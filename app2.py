import streamlit as st
st.title("some basic commands like slider , button in streamlit")
age = st.slider("Select your age", 1, 100)
city = st.selectbox("choose your city", ["delhi", "mumbai", "chennai", "kolkata"])

if st.button("show details"):
    st.write("age:", age)
    st.write("city:", city)
st.checkbox("I agree to the terms and conditions")