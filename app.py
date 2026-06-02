import streamlit as st
import pandas as pd

movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

if "started" not in st.session_state:
    st.session_state.started = False

if "genre" not in st.session_state:
    st.session_state.genre = None

st.title("CineMatch 🎬")
st.write("Don't know what to watch? Let me help find the perfect movie for you!")

if not st.session_state.started:
    if st.button("Get Started"):
        st.session_state.started = True
        st.rerun()

if st.session_state.started:
    st.write("What are you in the mood for?")

    if st.button("Action"):
        st.session_state.genre = "Action"

    if st.button("Comedy"):
        st.session_state.genre = "Comedy"

    if st.button("Romance"):
        st.session_state.genre = "Romance"

    if st.button("Horror"):
        st.session_state.genre = "Horror"

if st.session_state.genre:
    st.write(f"Great choice! Now, let's narrow it down a bit more. How niche would you like the movie to be?")

    st.button("Popular")
    st.button("Highly rated")
    st.button("Underrated")

st.write("MovieLens loaded successfully!")
st.write(movies.head())
