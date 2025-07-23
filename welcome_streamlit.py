import streamlit as st

# App Title
st.title("👋 Welcome App")

# Input fields
name = st.text_input("What is your name?")
age = st.number_input("How old are you?", min_value=0, max_value=120, step=1)

# Button
if st.button("Greet Me"):
    if name:
        st.success(f"Hello, {name}! 🎉 Welcome to your Python journey. You are {age} years old.")
    else:
        st.warning("Please enter your name first.")