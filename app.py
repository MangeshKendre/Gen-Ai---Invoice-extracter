# Import necessary libraries
from dotenv import load_dotenv
load_dotenv()  # Load all environment variables from .env 

import streamlit as st
import os
from PIL import Image 
import pathlib
import textwrap

import google.generativeai as genai

# Configure Gemini API with API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get responses
def get_gemini_response(input, image, prompt):
    # Use the Gemini API to generate content based on input, image, and prompt
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        # Prepare the image for processing
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Initialize our Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

# Set up header for the Streamlit app
st.header("Image data Extractor Application (Gen Ai)")

# File uploader for image selection
uploaded_file = st.file_uploader("Select image ...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Text input for user to enter a prompt
input=st.text_input("Input Prompt: ", key="input")

# Button to trigger image processing and response generation
submit=st.button("See image details as per input prompt")

# Initial prompt for the user
input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

## If the submit button is clicked
if submit:
    # Process the uploaded image and get a response using the Gemini API
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    
    # Display the generated response
    st.subheader("The Response is")
    st.write(response)
