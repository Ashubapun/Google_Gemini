from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
def get_gemini_respone(query):
    response = model.generate_content(query)
    return response.text

## APP

st.set_page_config(page_title = "Question Answering BOT using GEMINI")

st.header("Gemini LLM App")

input = st.text_input('Input : ', key = 'input')

submit = st.button("Ask your query")

if submit:
    response = get_gemini_respone(input)
    st.subheader("The Response is ")
    st.write(response)
    




