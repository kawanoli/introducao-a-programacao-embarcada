import streamlit as st
from cabecalho import cria_cabecalho
import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def pagina_inicial():
    cria_cabecalho()
    
    col1, col2, col3 = st.columns([5, 1, 5])
    with col2:
        st.image("images/timbu.png", caption="\"A vitória pertence aquele que acredita nela, e aquele que acredita nela por mais tempo.\" ~Pearl Harbor", width=200)
    

    st.markdown('<a name="introducao"></a>', unsafe_allow_html=True)
    st.markdown("## Introdução")
    st.markdown(
        """ 
        Bem vindos ao material interativo do trainee! O objetivo dele é não só servir de apoio para o livro, mas concentrar os caminhos para os materiais do trainee, de forma que se torne fácil de se acessar tudo, e central.

        Espero que esse trainee possa agregar a todos que estão acompanhando, bem como espero poder colaborar logo com todos vocês.
        """
    )
    st.markdown('<a name="contexto"></a>', unsafe_allow_html=True)
    st.markdown("## Materiais")
    st.markdown(
        """
        Por aqui, podemos ter acesso ao livro texto (clicando no kindle para redirecionar ao local que ele se encontra no drive), bem como o caminho para a pasta com os arquivos do trainee (desde slides até outros materiais).
        
        """)
    col1, col2 = st.columns([5, 5])
    with col1:
        #st.image("images/kindle.png", width=200)
        kindle = img_to_base64("images/kindle.png")
        st.markdown(
            f"""
            <a href="https://drive.google.com/file/d/1eKmpfiKAkmB41iVyDxrd-eL2eApNui9F/view?usp=drive_link">
                <img src="data:image/png;base64,{kindle}" width="200">
            </a>
            """,
            unsafe_allow_html=True
        )
    with col2:
        #st.image("images/drive.png", width=200)
        drive = img_to_base64("images/drive.png")
        st.markdown(
            f"""
            <a href="https://drive.google.com/drive/folders/1ZGV7cN9v64pWTBisIy6K-7B9ZogMPbfg?usp=drive_link">
                <img src="data:image/png;base64,{drive}" width="200">
            </a>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<a name="ambiente"></a>', unsafe_allow_html=True)
    st.markdown("## Configurando o ambiente")
    st.markdown("""
    Deixo aqui de referência alguns textos e videos de como configurar o ambiente do VSCode para programação em C++. Lembrem-se de instalar a extensão do PlatformIO também, para podermos trabalhar com embarcados propriamente.
                
    Para os sistemas Windows e Linux, basicamente esse tutorial da própria Microsoft deve ser o suficiente:
    https://code.visualstudio.com/docs/languages/cpp
    O mais dificil nesse processo, em minha visão, é provavelmente instalar o MinGW. Então você pode ir direto para esse vídeo da própria Microsoft, que ensina direitinho:
    https://youtu.be/oC69vlWofJQ?si=rrJBlFxTiqfyB8ek
    Sempre uso ele quando preciso reinstalar o MinGW por qualquer motivo que seja, então considero ele bem útil.
                
    Para MacOS acaba sendo um pouco mais trabalhoso, por causa do Xcode. Mas esse vídeo curto que linko abaixo já é o suficiente para fazer funcionar:
    https://youtu.be/r8nzxy3oPe4?si=b2jEjY1H2P-vGorS
                
    Infelizmente, esse não é o mesmo que eu vi quando configurei o meu pela primeira vez (infelizmente o vídeo do indiano desapareceu :/ ); entretanto, esse vídeo que estou linkando faz o mesmo passo a passo basicamente, embora pareceu um pouco mais confuso.
    """)
    st.markdown("""
    PS.: Prometo posteriormente gravar a minha versão do vídeo do MacOS, porque esse recomendado é bem cagado (embora foi o único que funcionou corretamente por aqui).
    """)

    st.markdown('<a name="biblio"></a>', unsafe_allow_html=True)
    st.markdown("## Recomendações bibliográficas")
    st.markdown("""
    Ter boas referências é essencial para consolidar a lógica e o raciocínio em programação. **Grokking Algorithms** ajuda a entender algoritmos de forma visual e intuitiva; **Princípios e Práticas de Programação com C++** aprofunda a base e a filosofia da linguagem; e o **Competitive Programmer’s Handbook** estimula a aplicação prática, otimização e pensamento crítico. Juntos, esses livros se complementam: fixam conceitos, fortalecem a base técnica e incentivam a prática constante.
    """)

    st.markdown('<a name="git"></a>', unsafe_allow_html=True)
    st.markdown("## Material básico de git")
    st.markdown("""
    Bem, esse material é bem antigo e simples. Realmente é só pra poder dar um pontapé inicial.
    """)
    col1, col2, col3 = st.columns([5, 5, 5])
    with col2:
        #st.image("images/git.png", width=200)
        git = img_to_base64("images/git.PNG")
        st.markdown(
            f"""
            <a href="https://docs.google.com/presentation/d/1RsrSoX_vt9J8jy0HxHINgUUeXOTDO30Gi27uQEpv4VY/edit?usp=sharing">
                <img src="data:image/png;base64,{git}" width="200">
            </a>
            """,
            unsafe_allow_html=True
        )