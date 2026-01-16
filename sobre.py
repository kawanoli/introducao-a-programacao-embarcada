import streamlit as st
from componentes import contact_style, sobre_link

def sobre_mim():
    st.markdown("## 👋 Sobre mim")
    
    # Colunas para layout
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Imagem de perfil (opcional)
        st.image("images/kawan.jpeg" ,use_container_width=True)
    
    with col2:
        # Informações básicas
        st.markdown("""
        ### **Kawan Oliveira**  
        _Estudante de Engenharia da Computação_  
        UFRN, Departamento de Engenharia da Computação e Automação  
        
        ---
        """)
        
        st.markdown("""
        Olá 👋! Meu nome é Kawan, tenho 22 anos e sou um estudante de Engenharia da Computação na UFRN, e atualmente, membro do setor de eletrônica daqui do PRD

        - Técnico em Eletrotécnica pelo IFRN Central

        - Membro do PRD no setor de Eletrônica desde 2024.2

        - Ex Monitor de Lógica de Programação por 1 ano e meio

        - Ex Membro do URA, onde pude participar de eventos de divulgação científica

        - Apaixonado por engenharia e fascinado por veículos de engenharia (foguetes, carros, aviões, etc)

        - Minhas áreas de interesse são sistemas embarcados e visão computacional (e, claro, qualquer coisa correlata)

        - Atualmente faço parte da equipe de desenvolvimento do PotyraSat


        ---

        🚀🚀 Atualmente membro do setor de eletrônica da :rainbow[Potiguar Rocket Design (PRD)] 
        
        """)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            sobre_link()
        
        st.markdown("""
        ---

        Sinta-se à vontade para entrar em contato se tiver alguma oportunidade interessante ou sugestões! 😉

                    
        ---
        
        """)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            st.markdown("""""")
            st.markdown("""**Conecte-se comigo:** """)
        with col2:
            contact_style()
        








