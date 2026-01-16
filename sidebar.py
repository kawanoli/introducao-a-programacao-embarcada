import streamlit as st
from componentes import sidebar_style
from paginainicial import pagina_inicial
from dia1 import dia_um
from semanais import semanais
from sobre import sobre_mim

def menu_lateral():
    # Menu lateral
    st.sidebar.image("images/prd.png", caption="Potiguar Rocket Design", use_container_width=True)
    #st.sidebar.markdown(sidebar_logo(), unsafe_allow_html=True)
    st.sidebar.title("Menu")
    opcao = st.sidebar.selectbox("Selecione a página a ser vista", ["Página Inicial", "Questões", "Atividades Semanais", "Sobre o Autor"])

    if opcao == "Página Inicial":
        sidebar_style([
        ("Introdução", "introducao"),
        ("Materiais", "contexto"),
        ("Configurando o ambiente", "ambiente"),
        ("Recomendações bibliográficas", "biblio"),
        ("Material básico de git", "git"),
        ])
        pagina_inicial()

    elif opcao == "Questões":
        dia_um()

    elif opcao == "Atividades Semanais":
        semanais()

    elif opcao == "Sobre o Autor":
        sobre_mim()