import streamlit as st
import google.generativeai as genai

st.title("welcome to AI app")
user_input = st.text_input("Ask me any thing:")  

genai.configure(api_key="AIzaSyDvHpIpsZy5aSBWCBBrmY3wnIwcd4qOKG4")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input :
    response = model.generate_content(user_input)
    st.write("Response:", response.text)
        
        