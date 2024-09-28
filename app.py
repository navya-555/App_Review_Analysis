import streamlit as st
from utils import func
import os
import google.generativeai as genai

def main():
    # Streamlit page configuration
    st.set_page_config(page_title="App Analysis Tool",
                        layout='centered',
                        initial_sidebar_state='collapsed')

    # Header
    st.header("How's the App 📱")

    # Input for Google API key with secure input
    key = st.text_input("Enter your Google API key", type="password")

    # Input for app link
    input_text = st.text_input("Enter the link of your app", placeholder="https://example.com")

    # Button to analyze the app
    submit = st.button("Analyze")

    # API key validation and model setup
    if key:
        try:
            genai.configure(api_key=key)
            gemini_model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        except Exception as e:
            st.error("An error occurred.")
    else:
        gemini_model=None

    # Analyze the app link
    if submit:
        if input_text:
            if key:
                try:
                    with st.spinner('Processing...'):
                        result = func.process_link(input_text, gemini_model)
                    st.markdown(result)
                except Exception as e:
                    st.error(f"Error analyzing the app link: {str(e)}")
            else:
                st.warning("Please enter Google API key.")
        else:
            st.error("Please enter a valid app link.")

if __name__ == "__main__":
    main()
