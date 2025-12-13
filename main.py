import streamlit as st
from sidebar import menu_lateral

st.set_page_config(
    page_title="Introdução à Programação de Embarcados",
    page_icon="images/prd.png",                 
    layout="wide"
)

menu_lateral()