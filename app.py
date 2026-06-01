import streamlit as st

st.title("CineMatch 🎬")
st.write("Don't know what to watch? Let me help find the perfect movie for you!")

if st.button("Get Started"):
    st.write("What are you in the mood for?")

    st.button("Action")
    st.button("Comedy")
    st.button("Romance")
    st.button("Horror")