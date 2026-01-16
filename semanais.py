from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_ace import st_ace
import base64

# Código de rand da questão 3
cpp_code = """
// Inclua a biblioteca random, defina uma seed
// Depois gere seus números com rand()

#include <iostream>
#include <random>

using namespace std;

int main() {
    // Setando a seed
    random_device rd;
    srand(rd());
    
    // Rand gera números mt grandes, restrinja a um intervalo (ex.: 0 à 99)
    int numero_aleatorio = rand() % 100; 
    cout << "Random number: " << numero_aleatorio << endl;

    return 0;
}
"""

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
























