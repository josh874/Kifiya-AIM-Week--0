import streamlit as st
import pandas as pd
import plotly.express as px 

st.set_page_config(page_title="Kifiya AI Mastery",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )

st.title("MoonLight Energy Solutions")
val = st.slider("Select a value", 0, 100, 0, step=1)
st.write(val)
btn1 = st.button("Click Me")
if btn1:
    st.write("I am clicked")

