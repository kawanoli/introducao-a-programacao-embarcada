import streamlit as st
from componentes import remove_espaco_sup

#Funcao para criacao do cabecalho; chamada em todo inicio de página ✈️
def cria_cabecalho():
    remove_espaco_sup()

    st.image("images/bkg.JPG" ,use_container_width=True)
    st.markdown(
        "<h1 style='text-align: center;'>Introdução à Programação de Embarcados em C++</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h4 style='text-align: right;'>Por Kawan Oliveira</h3>",
        unsafe_allow_html=True
    )
    st.markdown("---")