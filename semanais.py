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

rad_code = """
// Converte ângulo de graus para radianos
double grausParaRadianos(double graus) {
    return graus * 3.141592653589793 / 180.0;
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
        with open("images/timbu.png", "rb") as f:
            data1 = f.read()
            data1_base64 = base64.b64encode(data1).decode()

        with open("images/quests/cab1.png", "rb") as f:
            data2 = f.read()
            data2_base64 = base64.b64encode(data2).decode()

        with open("images/quests/button.png", "rb") as f:
            img_button = base64.b64encode(f.read()).decode()

        st.markdown(f"""
        <div style="
            display: flex;
            justify-content: center;   /* centraliza horizontalmente */
            width: 100%;
        ">
            <img src="data:image/png;base64,{data2_base64}" 
                style="
                    width: 80%;          /* ocupa grande parte da tela */
                    max-width: 1200px;   /* não ultrapassa 1200px */
                    height: auto;        /* mantém proporção */
                    border-radius: 10px;
                ">
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)  # adiciona espaço

        st.markdown(f"""
        <div style="display: flex; align-items: center;">
            <img src="data:image/png;base64,{data1_base64}" width="80" style="margin-right: 15px;">
            <span style="
                font-size: 2.6rem;       /* tamanho semelhante ao st.title */
                font-weight: 800;         /* negrito igual ao st.title */
                line-height: 1.2;         /* espaçamento de linha */
                margin: 0;
            ">
                Questão 1 - O metrô de Tbilisi
            </span>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("images/quests/imagem1.png", width=400)
        
        st.markdown("""
        Tbilisi, capital da Geórgia, foi a quarta cidade da União Soviética a desenvolver um sistema de metrô, seguindo Moscou, Leningrado e Kiev. A construção começou no início da década de 1960 e o primeiro trecho da rede foi inaugurado em 11 de janeiro de 1966, com seis estações iniciais. Assim como outros sistemas de metrô soviéticos da época, o Metrô de Tbilisi combinava engenharia funcional com construção em nível profundo e elementos arquitetônicos ornamentados, especialmente nas estações centrais.

        Tbilisi foi priorizada para o desenvolvimento inicial do metrô principalmente devido à sua geografia desafiadora: o denso núcleo urbano da cidade fica ao longo de um estreito vale fluvial, e as colinas ao redor dificultam o transporte de superfície. Os planejadores soviéticos também viam Tbilisi como um importante centro regional e buscavam destacar sua importância por meio de projetos de infraestrutura em grande escala, incluindo o metrô.

        Após o colapso da União Soviética na década de 1990, o Metrô de Tbilisi enfrentou uma grave crise. A falta de financiamento, os frequentes cortes de energia e a negligência crônica na manutenção afetaram severamente as operações diárias. Os funcionários do metrô frequentemente trabalhavam meses sem receber salário, enquanto sistemas de segurança essenciais, como ventilação, componentes elétricos e mecanismos de frenagem, praticamente não receberam atualizações. Embora o metrô nunca tenha parado de funcionar, operou em modo de sobrevivência mínima durante grande parte da década.

        Apesar de sua importância para a mobilidade urbana, a cobertura do metrô permanece limitada. Com apenas duas linhas, o sistema atende somente uma parte da cidade, deixando grandes bairros residenciais como Didi Dighomi, Lisi e Digomi sem acesso. Embora existam planos para a expansão da rede, o progresso tem sido lento devido a restrições financeiras e mudanças nas prioridades políticas.
        """)

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("images/quests/imagem2.png", width=400)
        
        st.markdown("""
        Após anos com expansão limitada, a expansão da rede metroviária de Tbilisi entrou em uma nova fase. A prefeitura deseja planejar novas linhas de metrô, mas desta vez utilizando critérios mais completos e modernos. A decisão de construir novos trechos deve levar em conta não apenas a viabilidade estrutural dos bairros, mas também:
        - Proximidade geográfica entre bairros (distâncias em uma matriz de adjacência).
        - Fluxo de deslocamento desejado pelos moradores (quais bairros eles mais querem alcançar).
        - Justificativa lógica para a construção da linha, evitando conexões longas e trechos pouco utilizados.

        Você deve escrever um programa que auxilie na criação de um mapa de linhas recomendadas para expansão, considerando as informações fornecidas pela prefeitura.
        Os dados necessários para resolver o problema já estarão embutidos no código. Você contará com uma lista de 20 bairros, cada um acompanhado de uma pontuação de viabilidade entre 0 e 100, sendo permitida a construção de estações apenas nos bairros cuja pontuação seja igual ou superior a 70. Além disso, será fornecida uma matriz de distâncias entre os bairros, com valores que variam de 0 a 20, onde 0 indica ausência de ligação direta e valores maiores representam bairros mais afastados; considere como viáveis apenas as conexões cuja distância seja menor ou igual a 10. Por fim, cada bairro também possui informações sobre os três destinos mais desejados pelos seus moradores, obtidos por meio de pesquisa populacional; se um bairro “A” deseja se deslocar até “B”, essa demanda aumenta a relevância da conexão entre eles.

        #### Você deve implementar um programa que:
        1. Identifique todos os bairros viáveis (pontuação ≥ 70).
        2. Avalie todas as conexões possíveis entre bairros viáveis, verificando se:
        - a distância entre eles é ≤ 10, e
        - há fluxo relevante (um quer ir ao outro ou vice-versa).
        3. Encontrar linhas metroviárias possíveis, onde:
        - cada linha deve ser um caminho contínuo,
        - só usando bairros viáveis,
        - com pelo menos 3 bairros.
        4. Para cada linha encontrada, calcule:
        - tamanho da linha
        - soma das viabilidades
        - média de viabilidade
        - demanda atendida (quantos fluxos internos da linha aparecem)
        - custo da linha (soma das distâncias entre bairros consecutivos)
        5. Decida quais linhas devem ser construídas usando o seguinte critério obrigatório:
        - Uma linha deve ser construída se: (Demanda_total × Média_de_viabilidade) / Custo_total ≥ 10
        6. Exiba:
        - Bairros viáveis
        - Conexões recomendadas
        - Todas as linhas possíveis
        - Linhas aprovadas
        - Métricas gerais da expansão
        """)

        st.markdown("**As informações acerca dos bairros, viabilidade, fluxos desejados, e as distâncias, se encontram no .txt abaixo:**")
        col1, col2, col3 = st.columns([1, 10, 10])
        with col2:
            #st.image("images/quests/button.png", width=200)
            st.markdown(
                f"""
                <a href="{"https://drive.google.com/file/d/1xEnCp4BS6pee9_T3kkq20h3UoZJJ8MbO/view?usp=drive_link"}" target="_blank">
                    <img src="data:image/png;base64,{img_button}" 
                        width="200" 
                        style="
                            cursor: pointer;
                            border-radius: 20px;  
                        ">
                </a>
                """,
                unsafe_allow_html=True
            )

        
        st.markdown("<br><br>", unsafe_allow_html=True)  # adiciona espaço

        st.markdown(f"""
        <div style="display: flex; align-items: center;">
            <img src="data:image/png;base64,{data1_base64}" width="80" style="margin-right: 15px;">
            <span style="
                font-size: 2.6rem;       /* tamanho semelhante ao st.title */
                font-weight: 800;         /* negrito igual ao st.title */
                line-height: 1.2;         /* espaçamento de linha */
                margin: 0;
            ">
                Questão 2 - Amanhecer
            </span>
        </div>
        """, unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("images/quests/imagem3.png", width=400)

        st.markdown("""O Zarya, também conhecido como Functional Cargo Block (FGB), foi o primeiro módulo lançado da Estação Espacial Internacional (ISS), entrando em órbita em 20 de novembro de 1998. Construído pela Rússia, sua função inicial era fornecer armazenamento, energia elétrica, controle de atitude e propulsão para a estação, garantindo que outros módulos pudessem ser acoplados posteriormente.
Embora tenha sido projetado como um módulo de carga funcional, o Zarya desempenhou um papel essencial como núcleo logístico e de suporte, permitindo a chegada e integração de módulos da NASA e da ESA. Ele inclui tanques de combustível, sistemas de controle de propulsão e painéis solares que geram energia para a estação, sendo um componente crítico para a operação inicial da ISS.
Além de suas funções técnicas, o Zarya serviu como base para os primeiros experimentos de acoplagem automatizada, demonstrando a complexidade da engenharia necessária para manter módulos acoplados em órbita e garantindo que a ISS pudesse crescer de forma modular, com segurança e eficiência, marcando o início da construção da estação e simbolizando a cooperação espacial internacional com seu nome, que significa "Amanhecer" em russo.""")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("images/quests/imagem4.png", width=400)

        st.markdown("""Você recebeu um conjunto de dados de séries temporais de medições do satélite Zarya. Devido ao ruído do sensor, os dados contêm pequenas flutuações aleatórias. Sua tarefa é normalizar os dados usando o filtro:
""")
        st.markdown(r"""
$$
y[n] = \frac{x[n] + y[n-1]}{2}, \quad y[0] = x[0]
$$

- \(x[n]\) é o valor da medição no instante \(n\)  
- \(y[n]\) é o valor filtrado no instante \(n\)  
- \(y[0] = x[0]\)  
                    
Cada coluna (altitude, velocidade, temperatura e potência) deve ser filtrada independentemente.
""")        
        st.markdown("""
#### O que deve ser feito:

1. Carregue o conjunto de dados CSV (o CSV será fornecido ao final do enunciado da questão).  
2. Aplique o filtro a cada coluna de medição (altitude, velocidade, temperatura, potência).  
3. Após aplicar o filtro, cada coluna deve ser avaliada quanto à **estabilidade**, definida como:  
   - **Estável:** se não há um salto muito grande de valor de um momento para outro.  
   - **Instável:** se o salto ultrapassa o limiar estipulado (você está livre para definir esse limiar).  

O resultado final deve indicar se cada coluna está **Estável** ou **Instável** após a suavização.""")
        
        st.markdown("**O link para o CSV com os dados se encontra abaixo:**")
        col1, col2, col3 = st.columns([1, 10, 10])
        with col2:
            st.markdown(
                f"""
                <a href="{"https://drive.google.com/file/d/1P-BXVSo4xRMxji-zScg9PY4A1OjMD65r/view?usp=drive_link"}" target="_blank">
                    <img src="data:image/png;base64,{img_button}" 
                        width="200" 
                        style="
                            cursor: pointer;
                            border-radius: 20px;  
                        ">
                </a>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br><br>", unsafe_allow_html=True)  # adiciona espaço
        
        st.markdown(f"""
        <div style="display: flex; align-items: center;">
            <img src="data:image/png;base64,{data1_base64}" width="80" style="margin-right: 15px;">
            <span style="
                font-size: 2.6rem;       /* tamanho semelhante ao st.title */
                font-weight: 800;         /* negrito igual ao st.title */
                line-height: 1.2;         /* espaçamento de linha */
                margin: 0;
            ">
                Questão 3 - Programação Esportiva
            </span>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("images/quests/imagem5.png", width=400)

        st.markdown("""O gênero de jogos de manager de futebol surgiu da necessidade de simular o futebol de forma estratégica, permitindo ao jogador assumir o papel de treinador ou gestor de um clube, sem depender de habilidades manuais nos controles. 
Nos anos 1980, os primeiros títulos pioneiros, como Football Manager para o ZX Spectrum, eram predominantemente baseados em texto e estatísticas, oferecendo ao jogador a possibilidade de tomar decisões sobre escalações, táticas e contratações. Com a década de 1990, o gênero se consolidou e se popularizou, com jogos como Championship Manager e Elifoot, que introduziram interfaces gráficas mais elaboradas, menus interativos e simulações detalhadas de partidas, muitas vezes utilizando bases de dados reais de jogadores, aumentando o realismo da experiência. 
""")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("images/quests/imagem6.png", width=400)

        st.markdown("""Já nos anos 2000, o gênero se expandiu para plataformas online, com títulos como Hattrick, que permitiam a interação entre milhares de jogadores em tempo real, incorporando elementos como finanças do clube, treinamento, contratos e patrocinadores. A partir dos anos 2010, o gênero se adaptou ao mundo mobile e multiplataforma, com jogos como Top Eleven e versões móveis de Football Manager, mantendo a essência da gestão e do planejamento estratégico, enquanto os motores de simulação se tornaram cada vez mais sofisticados, oferecendo partidas realistas e permitindo a criação de comunidades de jogadores que compartilham ligas, estatísticas e modificações. Assim, o gênero de manager de futebol evoluiu de simples simuladores textuais para complexos sistemas de gestão, combinando estratégia, estatísticas e interação social, mantendo sempre o foco na experiência de gestão de um clube de futebol.
Além da evolução tecnológica e da complexidade das decisões de gestão, os jogos de manager de futebol dependem fortemente de matemática, probabilidade e estatística para simular partidas e resultados. Cada jogador e time é representado por atributos numéricos que refletem habilidades como ataque, defesa, resistência e entrosamento. 
O motor do jogo utiliza fórmulas probabilísticas para calcular a chance de um passe ser completado, um chute resultar em gol ou um jogador sofrer lesão, considerando também fatores externos como clima, estádio e tática escolhida. As estatísticas históricas, médias de desempenho e distribuições de frequência são incorporadas para criar simulações realistas, tornando cada partida um resultado estocástico, ou seja, baseado em probabilidades, mas influenciado pelas decisões estratégicas do jogador. 
Dessa forma, entender conceitos de estatística, média, variância e probabilidade se torna essencial tanto para a criação desses jogos quanto para o planejamento dentro do jogo, pois cada escolha tática altera as chances de diferentes resultados em uma temporada ou competição.
""")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("images/quests/imagem7.png", width=400)

        st.markdown("""
Sua tarefa é criar um mini-simulador de partidas de futebol, onde o usuário poderá selecionar dois times que irão se enfrentar.
""")
        st.markdown("""

Cada time possuirá 5 jogadores:

**Jogadores de linha (4)**
- 1 defensor
- 2 alas
- 1 atacante
                    
**Goleiro (1)**

**Atributos de jogadores de linha (valores de 1 a 100):**
- Marcação
- Passe
- Finalização
- Decisões
- Imprevisibilidade
- Agilidade
- Equilíbrio
- Força

**Atributos do goleiro (valores de 1 a 100):**
- Defesa de perto
- Defesa de longe

#### Regras de ações e jogabilidade

#### Ações possíveis de um jogador de linha com a posse de bola:
- **Passar a bola:** escolher aleatoriamente entre outro jogador de linha do mesmo time. A chance de sucesso depende do atributo passe do jogador que passa, com um leve fator aleatório influenciado por decisão e imprevisibilidade.
- **Chutar a gol:** depende do atributo finalização, modulado pela decisão, imprevisibilidade e a defesa do goleiro adversário (distância do chute influencia se usa defesa de perto ou defesa de longe).
- **Driblar:** tenta avançar, pode ser sucedido ou não dependendo de agilidade, equilíbrio e aleatoriedade. Se driblar e chegar perto do gol, pode chutar; se falhar, perde a bola para o defensor ou goleiro adversário.

#### Força e marcação
- A força do jogador que marca influencia a chance de roubar a bola.
- O equilíbrio do jogador com a posse de bola influencia a chance de resistir à marcação.

#### Goleiros
- Nunca chutam a bola.
- Podem defender chutes (dependendo do tipo de chute: defesa de perto ou defesa de longe).
- Após defender, reposicionam a bola para um defensor ou um dos alas, escolhido aleatoriamente.

###### **Lembrem-se de adicionar aleatoriedade em cada ação, para evitar que um jogador dependa apenas de seus atributos estáticos e acabe por sempre vencer ou sempre perder a ação!**    
                
#### Início de cada tempo ou reinício após gol
- Posse de bola obrigatoriamente com o atacante do time com a posse.
- O atacante passa para um dos dois alas.
- No início da partida, o time da casa começa com a bola.

#### Duração
- Cada tempo terá 20 ações (passes, chutes ou dribles).

#### Saída esperada
Cada ação do jogo deve ser registrada no terminal, permitindo acompanhar o que aconteceu.

**Informações de cada ação podem incluir:**
- Jogador que executou a ação
- Tipo de ação (passar, driblar, chutar)
- Resultado da ação (sucesso ou falha)
- Goleiro ou defensor que interagiu, se aplicável
- Eventual gol marcado
""")
        st.markdown("**Para randomizar um número, você pode usar esse código abaixo:**")
        st.markdown(
            """
            <style>
            .streamlit-expanderHeader, .streamlit-expanderContent {
                font-family: "Fira Code", monospace;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.code(cpp_code, language="cpp")

        
        st.markdown("**As informações acerca dos times e seus atributos, se encontram no .txt abaixo:**")
        col1, col2, col3 = st.columns([1, 10, 10])
        with col2:
            st.markdown(
                f"""
                <a href="{"https://drive.google.com/file/d/1t3EXTcLRP25HN87Qe4ByTsIuGbt2-hA1/view?usp=drive_link"}" target="_blank">
                    <img src="data:image/png;base64,{img_button}" 
                        width="200" 
                        style="
                            cursor: pointer;
                            border-radius: 20px;  
                        ">
                </a>
                """,
                unsafe_allow_html=True
            )

        st.markdown("**Sinta-se livre para mudar os nomes dos times, atributos, ou adicionar times, caso deseje**")
        
    elif escolha == "Semana 2":
        with open("images/timbu.png", "rb") as f:
            data1 = f.read()
            data1_base64 = base64.b64encode(data1).decode()

        with open("images/quests/cab2.png", "rb") as f:
            data2 = f.read()
            data2_base64 = base64.b64encode(data2).decode()

        with open("images/quests/button.png", "rb") as f:
            img_button = base64.b64encode(f.read()).decode()

        st.markdown(f"""
        <div style="
            display: flex;
            justify-content: center;   /* centraliza horizontalmente */
            width: 100%;
        ">
            <img src="data:image/png;base64,{data2_base64}" 
                style="
                    width: 80%;          /* ocupa grande parte da tela */
                    max-width: 1200px;   /* não ultrapassa 1200px */
                    height: auto;        /* mantém proporção */
                    border-radius: 10px;
                ">
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)  # adiciona espaço

        st.markdown(f"""
        <div style="display: flex; align-items: center;">
            <img src="data:image/png;base64,{data1_base64}" width="80" style="margin-right: 15px;">
            <span style="
                font-size: 2.6rem;       /* tamanho semelhante ao st.title */
                font-weight: 800;         /* negrito igual ao st.title */
                line-height: 1.2;         /* espaçamento de linha */
                margin: 0;
            ">
                Questão 1 - Apostando todas as fichas
            </span>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("images/quests/imagem8.jpg", width=400)
        
        st.markdown("""
        Durante o lançamento de um foguete, pequenas incertezas no ângulo, na velocidade inicial e em condições ambientais podem alterar significativamente o local de queda do foguete ou de seus estágios.

        Para avaliar riscos e definir zonas de segurança, engenheiros utilizam simulações de Monte Carlo para estimar, por meio de simulação, a região mais provável de impacto, considerando incertezas nos parâmetros de lançamento.

        Simulações de Monte Carlo são técnicas computacionais usadas para estimar resultados de problemas complexos por meio de experimentos aleatórios repetidos. Em vez de calcular uma solução exata por fórmulas fechadas, o método simula muitas possibilidades diferentes, utilizando números aleatórios, e analisa estatisticamente os resultados obtidos.
        Essas simulações são especialmente úteis quando o sistema envolve incertezas, variáveis aleatórias ou comportamentos difíceis de modelar diretamente, sendo amplamente utilizadas em áreas como engenharia, física, finanças e ciência de dados.
        
        O nome Monte Carlo faz referência ao famoso distrito de cassinos em Mônaco. A analogia vem do fato de que o método se baseia em sorteios aleatórios, assim como apostas em jogos de azar. Assim como em um cassino, quanto maior o número de “apostas” (simulações realizadas), mais confiável tende a ser a estimativa final.
                    
        Neste exercício, você deverá simular uma série de lançamentos e estimar a distribuição dos possíveis raios de quedado foguete, para ajudar a determinar a probabilidade de onde iremos encontrar o mesmo na hora da recuperação. Para simplificar, todas as fórmulas e constantes necessárias são fornecidas: a aceleração da gravidade é constante, g = 9.8 m/s², e o alcance horizontal do foguete é calculado por
        """)
        
        st.markdown(r"""
        $$
        R = \frac{v^2 \cdot \sin(2\theta)}{g}
        $$
        """)
        st.markdown("""
        em que v é a velocidade inicial do foguete e θ é o ângulo de lançamento em radianos (a funçao de conversao para radianos já será dada).

        Os valores utilizados em cada simulação variam de forma aleatória e uniforme dentro dos seguintes intervalos:

                    
        """)
        st.markdown(r"""
        $$
        \begin{aligned}
        v &\in [v_0 - \Delta v,\; v_0 + \Delta v] \\
        \theta &\in [\theta_0 - \Delta \theta,\; \theta_0 + \Delta \theta]
        \end{aligned}
        $$
        """)

        st.markdown("""
        O programa deve ler:
        """)
        
        st.markdown(r"""
        - **N**: número de simulações  
        - **v₀**: velocidade nominal *(m/s)*  
        - **Δv**: variação máxima da velocidade *(m/s)*  
        - **θ₀**: ângulo nominal *(graus)*  
        - **Δθ**: variação máxima do ângulo *(graus)*  
        - **K**: número de regiões para análise da distribuição  
        """)

        st.markdown("""
        Sendo assim, monte um programa que:
        """)

        st.markdown(r"""
        1. Simule **N** lançamentos do foguete (o N sendo de sua escolha), gerando aleatoriamente os valores de **$v$** e **$\theta$** dentro de intervalos fornecidos (também à sua escolha), e calcule o raio de queda **$R$** de cada lançamento.
        2. Determine o menor e o maior valor de **$R$** obtidos na simulação, denotados por **$R_{\min}$** e **$R_{\max}$**.
        3. Divida o intervalo **$[R_{\min}, R_{\max}]$** em **K** regiões consecutivas de mesmo tamanho (escolha bem o valor de K).
        4. Conte quantos lançamentos caíram em cada região e estime a probabilidade de queda em cada uma delas como a proporção de lançamentos que ocorreram na respectiva região.
        5. Apresente os resultados de forma textual, mostrando para cada região:
            - intervalo da região  
            - quantidade de lançamentos  
            - probabilidade de queda *(em percentual)*  
        """)

        st.markdown("""Exemplo:""")
        st.code(
        """Exemplo de entrada:
N = 1000
v0 = 50
Δv = 5
θ0 = 45
Δθ = 5
K = 5

Exemplo de saída possível:
Raio mínimo: 199 m
Raio máximo: 258 m

Região 1 [199 - 210]: 95 lançamentos (9.5%)
Região 2 [210 - 222]: 210 lançamentos (21.0%)
Região 3 [222 - 234]: 320 lançamentos (32.0%)
Região 4 [234 - 246]: 240 lançamentos (24.0%)
Região 5 [246 - 258]: 135 lançamentos (13.5%)
        """,
        language="text"
        )
        st.caption(
        "Os números acima são ilustrativos. "
        "Seus resultados podem variar devido à natureza aleatória da simulação."
        )

        st.markdown("**Para a funçao de conversao para radianos, você pode usar a função abaixo:**")
        st.markdown(
            """
            <style>
            .streamlit-expanderHeader, .streamlit-expanderContent {
                font-family: "Fira Code", monospace;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.code(rad_code, language="cpp")

        st.markdown("<br><br>", unsafe_allow_html=True)  # adiciona espaço

        st.markdown(f"""
        <div style="display: flex; align-items: center;">
            <img src="data:image/png;base64,{data1_base64}" width="80" style="margin-right: 15px;">
            <span style="
                font-size: 2.6rem;       /* tamanho semelhante ao st.title */
                font-weight: 800;         /* negrito igual ao st.title */
                line-height: 1.2;         /* espaçamento de linha */
                margin: 0;
            ">
                Questão 2 - De olhos bem abertos
            </span>
        </div>
        """, unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("images/quests/imagem9.png", width=400)

        st.markdown("""
        Um drone que monitora plantações envia imagens da superfície terrestre para análise de vegetação. Cada imagem colorida é capturada em três canais: vermelho (R), verde (G) e azul (B). Para que o computador possa processar os dados, cada canal da imagem é transformado em uma matriz de números inteiros, onde cada elemento representa a intensidade do pixel naquele canal, variando de 0 (intensidade mínima) a 255 (intensidade máxima). Sendo assim, a “sobreposição” dos canais é o que gera a imagem final que vemos em nossos computadores.
        
        Cada pixel da imagem pode representar terra, água ou vegetação.
        
        Assim, cada imagem colorida é representada por três matrizes do mesmo tamanho, correspondendo aos canais R, G e B. Com essas matrizes, é possível analisar as cores de cada pixel individualmente e identificar regiões de interesse, como áreas de vegetação saudável, diferenciando-as de terra nua, água ou áreas degradadas.
""")
        
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.image("images/quests/imagem10.png", width=700)

        st.markdown("""
        Para analisar a saúde e a produtividade das plantações, engenheiros precisam identificar os pixels que representam plantas, definidos por valores de intensidade dentro de um limiar para cada canal:
        """)

        st.markdown(r"""
        $$
        \begin{aligned}
        Rmin ≤ R ≤ Rmax \\
        Gmin ≤ G ≤ Gmax \\
        Bmin ≤ B ≤ Bmax
        \end{aligned}
        $$
        """)

        st.markdown("""
        Um pixel que atende a essas três condições é considerado como representando vegetação relevante. Além disso, os pixels com maior intensidade total (R+G+B) indicam regiões potencialmente mais saudáveis ou produtivas, que devem ser priorizadas para análise.
        """)

        st.markdown("""
        Sendo assim, monte um programa que:
        """)

        st.markdown(r"""
        1. Percorre todas as matrizes e identifica os pixels que representam plantas, dentro do limiar definido.
        2. Armazena as posições (linha e coluna) desses pixels.
        3. Ao final, apresente:
            - Quantidade de pixels de plantação encontrados
            - Pixel mais intenso (maior soma R+G+B)
            - Top-K pixels mais intensos, em ordem decrescente de intensidade, indicando linha, coluna e intensidade         
        4. Receba nas entradas:
            - M, N: dimensões da imagem
            - Limiares: Rmin, Rmax, Gmin, Gmax, Bmin, Bmax
            - K: número de pixels mais intensos a retornar                  
        5. Mostre na saída:
            - Total de pixels que representam plantas
            - Coordenadas do pixel mais intenso e sua intensidade
            - Lista dos top-K pixels mais intensos com coordenadas e intensidade
                    
        **Dica:** como as matrizes já são passadas, você pode já guardar direto no programa, para evitar ter que passar na entrada (e perder tempo nos testes).
        """)

        st.markdown("""Exemplo:""")
        st.code(
        """Exemplo simplificado (3x3)
Matrizes:
R = [[10, 200, 50],
     [30, 100, 255],
     [0,  50,  75]]

G = [[5,  180, 60],
     [40, 120, 250],
     [10, 45,  80]]

B = [[0,  150, 70],
     [35, 110, 245],
     [5,  50,  60]]

Limiares:
R: 50–255
G: 50–200
B: 50–255
K = 2

Processamento:
Pixels dentro do limiar:
(0,1): 200+180+150 = 530
(1,2): 255+250+245 = 750

Saída esperada:
Total de pixels de plantação: 2
Pixel mais intenso: (1,2) intensidade 750
Top 2 pixels mais intensos:
1: (1,2) intensidade 750
2: (0,1) intensidade 530
        """,
        language="text"
        )
        st.caption(
        "Os resultados acima são ilustrativos. "
        "Seus resultados podem variar devido à natureza aleatória dos dados e limiares."
        )

        st.markdown("**As informações acerca dos limiares, bem como as matrizes, se encontram no .txt abaixo:**")
        col1, col2, col3 = st.columns([1, 10, 10])
        with col2:
            #st.image("images/quests/button.png", width=200)
            st.markdown(
                f"""
                <a href="{"https://drive.google.com/file/d/1ZMe09lXoNOuX7kf6jquzeqc-N8H_3gT7/view?usp=share_link"}" target="_blank">
                    <img src="data:image/png;base64,{img_button}" 
                        width="200" 
                        style="
                            cursor: pointer;
                            border-radius: 20px;  
                        ">
                </a>
                """,
                unsafe_allow_html=True
            )

    else:
        st.markdown("# Atividades Semanais - Semana 3")
        st.markdown("### :cry: Por enquanto aqui está vazio")
























