import streamlit as st
from map_component import render_compost_map

st.set_page_config(page_title="Food Composting App", layout="wide")

# Header
st.markdown("<h1 style='text-align: center;'>Food Composting Locator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Map test.</p>", unsafe_allow_html=True)


# Use 3 columns and place the map in the center column
col1, col2, col3 = st.columns([1, 1, 1])  # 1:1:1 width ratio

with col2:
    render_compost_map()