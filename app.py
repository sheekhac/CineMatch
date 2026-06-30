import streamlit as st
import pandas as pd
from recommender import prepare_movie_data, get_recommendations

movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

movies_with_ratings = prepare_movie_data(movies, ratings)

if "started" not in st.session_state:
    st.session_state.started = False

if "genre" not in st.session_state:
    st.session_state.genre = None

if "preference" not in st.session_state:
    st.session_state.preference = None

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
    st.write("Great choice! Now, let's narrow it down a bit more.")
    st.write("How niche would you like the movie to be?")

    if st.button("Popular"):
        st.session_state.preference = "Popular"

    if st.button("Highly Rated"):
        st.session_state.preference = "Highly Rated"

    if st.button("Underrated"):
        st.session_state.preference = "Underrated"

if st.session_state.genre and st.session_state.preference:
    recommendations = get_recommendations(
        movies_with_ratings,
        st.session_state.genre,
        st.session_state.preference
    )

    st.write("### Recommended Movies")

    st.write(
        recommendations[["title", "genres", "average_rating", "rating_count"]]
    )