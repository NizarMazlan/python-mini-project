import streamlit as st

st.header("st.button")

if st.button("Say Hello"):
    st.button("Say Goodbye")
    st.write("Why hello there")
elif st.button("Say Goodbye"):
    st.write("Goodbye")