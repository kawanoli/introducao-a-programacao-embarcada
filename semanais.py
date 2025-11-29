from streamlit_option_menu import option_menu
import streamlit as st

def semanais():
    escolha = option_menu(
        menu_title=None,
        options=["Semana 1", "Semana 2", "Semana 3"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"width": "100%", "padding": "0px"},
            "nav-link": {"font-size": "18px", "text-align": "center"},
            "nav-link-selected": {"background-color": "#0B1A5C", "color": "white"},
        }
    )

    #st.write(f"Você selecionou **{escolha}**")

    if escolha == "Semana 1":
        st.markdown("# Atividades Semanais - Semana 1")
        st.markdown("### :cry: Por enquanto aqui está vazio")
    elif escolha == "Semana 2":
        st.markdown("# Atividades Semanais - Semana 2")
        st.markdown("### :cry: Por enquanto aqui está vazio")
    else:
        st.markdown("# Atividades Semanais - Semana 3")
        st.markdown("### :cry: Por enquanto aqui está vazio")
