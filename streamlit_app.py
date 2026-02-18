import streamlit as st
import requests

st.title("🛒 SecureStore – Panel")

username = st.text_input("Username")
role = st.selectbox("Role", ["admin", "user"])

if st.button("Login"):
    res = requests.post(
        "http://localhost:8000/login",
        params={
            "username": username,
            "role": role
        }    
    )
    st.json(res.json())