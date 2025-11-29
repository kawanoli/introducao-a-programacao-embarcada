import streamlit as st
from sidebar import menu_lateral
#from mirror import editor_cpp 

#st.write("## Enunciado do exercício")
#st.write("Faça um programa que imprima ...")
# Adiciona o editor
#editor_cpp()

st.set_page_config(
    page_title="Introdução à Programação de Embarcados",
    page_icon="images/prd.png",                 
    layout="wide"
)

menu_lateral()