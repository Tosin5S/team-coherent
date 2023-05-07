#!/usr/bin/env python3
# import streamlit as st

import streamlit as st
from backend import cohere_emotional_analysis as health

emoji = {
    'love' : ':hearts:',
    'anger' : ':angry:',
    'joy' : ':joy:',
    'sadness' : ':sad:',
    'surprise' : ':open_mouth:',
    'fear' : 'fear'
}

# Set page title
st.set_page_config(page_title="Internal Health", page_icon=":bar_chart:")

# Set page layout
st.markdown("<h1 style='text-align: center;'>Internal Health</h1>", unsafe_allow_html=True)

# Create user input section
user_input = st.text_area("Enter your the user post:")

if st.button("Generate reply"):
    with st.spinner('Analysing post...'):
        emotion = health.classify_emotion(user_input)

        st.subheader('Suggested Reply')
        st.write(health.write_post(user_input))
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Emotional Level')
            st.bar_chart(health.plotter(user_input))
        with col2:
            st.subheader('Emotion')
            st.write(f'This person currently has a feeling {emotion} {emoji.get(emotion)}')
