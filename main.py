
import streamlit as st


st.set_page_config(layout="wide")

with st.sidebar:
    st.page_link("main.py", label="Home", icon="🏠")
    st.page_link("pages/cmcapital.py", label="CM Capital", icon="1️⃣")
    st.page_link("pages/xp.py", label="XP", icon="2️⃣")
    st.page_link("http://www.google.com", label="Google", icon="🌎")




