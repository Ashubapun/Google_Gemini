from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_respone(input, image):
    if input!="":
        response = model.generate_content([input, image])

    else:
        response = model.generate_content(image)

    return response.text

st.set_page_config(page_title = "Gemini Pro Vision")

st.header("Gemini Vision LLM App")

input = st.text_input('Input Prompt : ', key = 'input')

upload_file = st.file_uploader("Upload an Image ", type = ['jpg', 'jpeg', 'png'])
image  = ''
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption = 'Uploaded Image', use_column_width = True)

submit = st.button("Tell me about the image")

if submit:
    response = get_gemini_respone(input, image)
    st.subheader("The Response is ")
    st.write(response)