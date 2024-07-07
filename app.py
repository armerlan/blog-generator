import streamlit as st
from llm_helper import getLlamaResponse

st.set_page_config(page_title = "Generate Blogs",
                   page_icon = ":b:",
                   layout = 'centered',
                   initial_sidebar_state = 'collapsed')

st.header("Generate Blogs 🅱️")

input_text = st.text_input("Enter the Blog Topic")


#Creating two more columns for additional 2 fields

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No. of words')
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientists', 'Common People'), index = 0)

submit = st.button("Generate")

if submit:
    st.write(getLlamaResponse(input_text, no_words, blog_style))