import streamlit as st
st.title("Some Basic commands in Streamlit")
name =st.text_input("Enter your name")
if st.button("Submit"):
    st.write(f"Hello, {name}")
