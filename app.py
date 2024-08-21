import streamlit as st
import google.generativeai as genai


st.title("welcome my dravid")

genai.configure(api_key="AIzaSyBZh3cnizfN8mOoar9QpdzYDWJHsmV5YzM")

text=st.text_input("Enter your queston")

model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])
response=chat.send_message(text)
st.write(response.text)