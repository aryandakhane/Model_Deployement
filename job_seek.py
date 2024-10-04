import streamlit as st
import pandas as pd

name= st.text_input("Enter your name","")

#st.markdown(f"How are you:{name}?")

job= st.text_area("What do you do?")
age= st.number_input("Enter a number value", min_value=5, max_value=80)

#st.markdown=(f"How are you doing:{}?")

if name!="":
    st.markdown(
        f"""
        * Name: {name}
        * Job: {job}
        * Age:{age}
        """
    )
is_available_for_work = st.checkbox("Available for work!")

st.write(is_available_for_work)
threshold= st.slider("Pick a threshold", min_value=1.0, max_value=100.0, value=5.0, step=0.5)
st.write(threshold)