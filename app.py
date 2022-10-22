import streamlit as st
import pickle
import praw

st.write("API fetch . . .")

pickle_in = open("reddit.pkl", "rb")

reddit = pickle.load(pickle_in)

subreddit_title = st.text_input("subreddit : r/")
try:
    subreddit = reddit.subreddit(subreddit_title)
    hot = subreddit.hot(limit=10)

    for i in hot:
        st.write(i.title)
        st.write(i.url)
        st.write(f"Upvote Ratio: {i.upvote_ratio}")
except ValueError:
    st.write("Enter the subreddit name to fetch content")
    