import streamlit as st
from questoes import *

def dia_um():
    questao = st.selectbox("Selecione a questão:", ["Questão 1", "Questão 2"])
    if questao == "Questão 1":
        questao1(key="q1")
    elif questao == "Questão 2":
        questao2(key="q2")
    

