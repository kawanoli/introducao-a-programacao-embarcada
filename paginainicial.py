import streamlit as st
from cabecalho import cria_cabecalho

def pagina_inicial():
    cria_cabecalho()
    
    col1, col2, col3 = st.columns([5, 1, 5])
    with col2:
        st.image("images/timbu.png", caption="\"A vitória pertence aquele que acredita nela, e aquele que acredita nela por mais tempo.\" ~Pearl Harbor", width=200)
    

    st.markdown('<a name="introducao"></a>', unsafe_allow_html=True)
    st.markdown("## Introdução")
    st.markdown(
        """ 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean suscipit mauris ac gravida vehicula. Cras in mi enim. Duis vitae ultricies nunc, id euismod turpis. 
        Cras vel consectetur est. Vestibulum condimentum dolor neque, vitae pretium nisi efficitur ullamcorper. Quisque a urna vel turpis tristique laoreet sit amet semper nunc. 
        Phasellus imperdiet aliquam felis. Ut euismod lectus at laoreet feugiat. Interdum et malesuada fames ac ante ipsum primis in faucibus. Proin a lorem eget enim euismod 
        tempus. Nullam vel suscipit mi. Pellentesque consequat libero non enim molestie vehicula. Pellentesque convallis ex justo, ut sodales turpis pharetra in. Donec leo 
        sapien, blandit id congue quis, euismod quis nunc. Pellentesque rutrum porta nisi vitae volutpat. Proin congue lectus et scelerisque suscipit.
        """
    )
    st.markdown('<a name="contexto"></a>', unsafe_allow_html=True)
    st.markdown("## Materiais")
    st.markdown(
        """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean suscipit mauris ac gravida vehicula. Cras in mi enim. Duis vitae ultricies nunc, id euismod turpis. 
        Cras vel consectetur est. Vestibulum condimentum dolor neque, vitae pretium nisi efficitur ullamcorper. Quisque a urna vel turpis tristique laoreet sit amet semper nunc. 
        Phasellus imperdiet aliquam felis. Ut euismod lectus at laoreet feugiat. Interdum et malesuada fames ac ante ipsum primis in faucibus. Proin a lorem eget enim euismod 
        tempus. Nullam vel suscipit mi. Pellentesque consequat libero non enim molestie vehicula. Pellentesque convallis ex justo, ut sodales turpis pharetra in. Donec leo 
        sapien, blandit id congue quis, euismod quis nunc. Pellentesque rutrum porta nisi vitae volutpat. Proin congue lectus et scelerisque suscipit.
        """
    )