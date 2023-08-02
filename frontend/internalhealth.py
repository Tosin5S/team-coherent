import streamlit as st
from backend import cohere_emotional_analysis as health

emoji = {
    'love': ':hearts:',
    'anger': ':angry:',
    'joy': ':joy:',
    'sadness': ':sad:',
    'surprise': ':open_mouth:',
    'fear': ':fear:'
}

# Set page layout
st.set_page_config(page_title="Internal Health", page_icon=":bar_chart:",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.write(
    """
    <style>
    .navbar {
        display: flex;
        justify-content: space-around;
        padding: 10px;
        background-color: #f5f5f5;
        border-bottom: 1px solid #ddd;
    }
    .navbar a {
        text-decoration: none;
        color: #333;
        padding: 5px 10px;
        border-radius: 5px;
    }
    .navbar a:hover {
        background-color: #ddd;
    }
    </style>
    """, unsafe_allow_html=True
)

# Links in the simulated navbar
st.markdown(
    """
    <div class="navbar">
        <a href="https://github.com/Timadey/team-coherent" target="_blank">GitHub</a>
        <a href="https://devpost.com/software/internal-health" target="_blank">Devpost</a>
        <a href="#about">About</a>
    </div>
    """, unsafe_allow_html=True
)




# Set page layout
st.markdown("<h1 style='text-align: center;'>Internal Health</h1>", unsafe_allow_html=True)

# Create user input section
user_input = st.text_area("Enter your the user post:")

if st.button("Generate reply"):
    with st.spinner('Analyzing post...'):
        emotion = health.classify_emotion(user_input)

        st.subheader('Suggested Reply')
        st.write(health.write_post(user_input))
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Emotional Level')
            st.bar_chart(health.plotter(user_input))
        with col2:
            st.subheader('Emotion')
            st.write(f'This person currently has a feeling of {emotion} {emoji.get(emotion)}')

st.markdown("<h1 style='text-align: left;'>About</h1>", unsafe_allow_html=True)
st.write("""
Many people share their thoughts on social media, but some of them may struggle with mental health issues that lead to suicidal actions.
         These issues may not appear suddenly, but rather show up gradually in their posts and activities. 
         Social media networks have a lot of data that can be used to help people improve their mental health. 
         One way to do this is by using sentiment analysis, which can detect the emotions and feelings behind the posts. 
         By analyzing the sentiment of the posts, social media networks can use machine learning algorithms to predict the behavior and actions of the users. 
         They can also use this information to connect the users with healthcare professionals who can provide personalized mental health care. Moreover, 
         they can use generative AI to create responses that match the users’ emotions and needs, such as comfort, encouragement, or humor.

Our project, Internal Health, aims to use social media as a tool for mental health care. 
         We use Cohere’s API to classify the posts into six different emotions and then generate appropriate responses using GPT. 
         We hope that our project can help social media users feel better and get the help they need.

Live Demo: https://internal-health.onrender.com/
Devpost Page: https://devpost.com/software/internal-health
Reference https://www.hindawi.com/journals/cin/2022/9194031/ 
         """)