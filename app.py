import streamlit as st
from utils import func

st.set_page_config(page_title="How's the App ?",
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("How's the App 📱")

input_text=st.text_input("Enter the link of your app")

submit=st.button("Analyze")

if submit:
    st.write(func.scrape_content(input_text)[0:-1])
    #print(func.scrape_content(input_text))