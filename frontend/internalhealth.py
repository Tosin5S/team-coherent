#!/usr/bin/env python3
import streamlit as st

st.title("Team Coherent")
text_tab, file_tab, web_tab = st.tabs(['Text', 'File', 'Web'])
with text_tab:
    st.text('Enter the user text to analyse')
    text_input = st.text_area('Text to analyse')
with file_tab:
    st.text('Upload a file containing the posts to analyse')
    file_input = st.file_uploader('Upload file')
with web_tab:
    st.text('You can also provide a social media feed to analyse a user newsfeed')
    link_to_feed = st.text_input('Enter link to social media feed', placeholder='https://twitter.com/timadey/post/12345')

emotion = st.button('Get emotion ')
