from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_ace import st_ace
import base64

randvec_code = """
#include <iostream>   // Biblioteca para entrada e saída (cout, endl)
#include <cstdlib>    // Biblioteca que fornece rand() e srand()
#include <random>     // Biblioteca para geração de sementes aleatórias para a randomização

using namespace std;

// ------------------------------------------------------------
// A função gerarPontos preenche um vetor de inteiros com IDs aleatórios q
// que representam possíveis pontos de pouso na superfície lunar.
//
// São usados os parâmetros:
//   pontos: ponteiro para o início do vetor de pontos de pouso
//   tamanho: quantidade de elementos do vetor
//
// Vale destacar que os valores gerados NÃO estão ordenados.
// ------------------------------------------------------------
void gerarPontos(int* pontos, int tamanho) {
    random_device rd;
    srand(rd());

    // Preenche o vetor com valores aleatórios
    for (int i = 0; i < tamanho; i++) {
        pontos[i] = rand();
    }
}

int main() {
    // Define a quantidade de pontos de pouso disponíveis
    int tamanhoVetor = 100000;

    // Alocação dinâmica de memória para armazenar os pontos de pouso
    // Cada posição do vetor representa o ID de um ponto possível
    int* pontosDePouso = new int[tamanhoVetor];

    // Variável que armazenará o ID do ponto de pouso desejado
    int alvo;

    // Gera os pontos de pouso de forma aleatória
    gerarPontos(pontosDePouso, tamanhoVetor);

    // Seleciona aleatoriamente um ID existente no vetor
    // Isso garante que o ponto de pouso procurado realmente exista
    alvo = pontosDePouso[rand() % tamanhoVetor];

    // Exibe o ID que o sistema deverá localizar
    cout << "Buscando ponto de pouso com ID: " << alvo << endl;

    // ------------------------------------------------------------
    // A partir daqui, você deve desenvolver o algoritmo necessário
    // para localizar o ponto de pouso desejado da forma mais 
    // eficiente possível, explicando as decisões.
    // ------------------------------------------------------------


    // Liberação da memória alocada dinamicamente
    delete[] pontosDePouso;

    return 0;
}
"""

monte_code = """
#include <iostream>
#include <cmath>
#include <random>

using namespace std;

// Gravidade constante (m/s²)
const double G = 9.8;

// ------------------------------------------------------------
// Função para gerar um número aleatório
// Você deve passar para a função, os dois valores (min e max)
// de intervalo na qual o número pode se encontrar.
// ------------------------------------------------------------
double aleatorio(double min, double max) {
    return min + (max - min) * (rand() / (double) RAND_MAX);
}

// ------------------------------------------------------------
// Função para converter um ângulo de graus para radianos
// ------------------------------------------------------------
double grausParaRadianos(double graus) {
    return graus * 3.141592653589793 / 180.0;
}

// ------------------------------------------------------------
// Função para calcular o alcance R com base na equação
// R = (v² * sin(2θ)) / g
// Com a gravidade constante (9,8 m/s²)
// ------------------------------------------------------------
double calcularAlcance(double v, double theta) {
    double thetaRad = grausParaRadianos(theta);
    return (v * v * sin(2 * thetaRad)) / G;
}

int main() {
    // Setando a seed
    random_device rd;
    srand(rd());

    int N;          // Número de simulações
    double v0;      // Velocidade nominal
    double deltaV;  // Variação máxima da velocidade
    double theta0;  // Ângulo nominal
    double deltaTheta; // Variação máxima do ângulo
    int K;          // Número de regiões (bins) da distribuição

    cout << "Digite o numero de simulacoes (N): ";
    cin >> N;

    cout << "Digite a velocidade nominal v0 (m/s): ";
    cin >> v0;

    cout << "Digite a variacao maxima da velocidade Δv (m/s): ";
    cin >> deltaV;

    cout << "Digite o angulo nominal θ0 (graus): ";
    cin >> theta0;

    cout << "Digite a variacao maxima do angulo Δθ (graus): ";
    cin >> deltaTheta;

    cout << "Digite o numero de regioes K para a distribuicao: ";
    cin >> K;

    // ------------------------------------------------------------
    // A partir daqui, você deve gerar valores aleatórios 
    // de v e θ dentro dos intervalos (use a função "aleatorio"
    // que foi criada), calcular o alcance para cada simulação,
    // armazenar/analisar os resultados, e construir a distribuição 
    // do alcance em K regiões
    // ------------------------------------------------------------

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
                Questão 1 - Cada segundo custa
            </span>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("images/quests/imagem12.webp", width=400)
        
        st.markdown("""
Uma equipe da agência espacial está desenvolvendo, em C++, um software embarcado responsável por determinar rapidamente o local de pouso de um módulo lunar.

O sistema recebe um vetor de inteiros contendo os IDs dos possíveis pontos de pouso, porém esses IDs chegam fora de ordem (não estão organizados de forma crescente nem decrescente), devido à forma como os dados são coletados pelos sensores orbitais.

Cada ID é único e corresponde a um ponto de pouso válido. O sistema também recebe um ID alvo, que representa o ponto de pouso selecionado após a análise dos sensores.
        """)

        st.markdown("""
        Sendo assim, monte um programa que:
        """)

        st.markdown(r"""
        1. Receba um vetor de inteiros com os IDs dos pontos de pouso desordenados.
        2. Receba um inteiro representando o ID do ponto de pouso desejado.
        3. Retorne a posição (índice) desse ID no vetor, o mais rápido possível, considerando que o sistema opera em tempo crítico.
        """)

        st.markdown("""
Ao final de tudo, descreva a estratégia adotada para resolver o problema, explicando por que ela é eficiente e por que ela foi escolhida.
""")
        
        st.markdown("""
Para você começar a trabalhar, este abaixo é o esboço inicial do código a ser desenvolvido; ele já te dá o vetor (que está sendo feito por meio de randomização, para simular a inserção dos dados), e a variável que guarda o alvo que deve ser procurado. Parta deste código como base.
""")
        st.markdown("""
           <style>
           .streamlit-expanderHeader, .streamlit-expanderContent {
               font-family: "Fira Code", monospace;
           }
           </style>
           """,
           unsafe_allow_html=True
        )
        st.code(randvec_code, language="cpp")

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
                Questão 2 - Apostando todas as fichas
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

        st.markdown("Para você começar a trabalhar, este abaixo é o esboço inicial do código a ser desenvolvido; ele já te dá as funções básicas para trabalhar. Parta deste código como base.")
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
        st.code(monte_code, language="cpp")

        st.markdown("<br><br>", unsafe_allow_html=True)  # adiciona espaço


    else:
        st.markdown("# Atividades Semanais - Semana 3")
        st.markdown("### :cry: Por enquanto aqui está vazio")
























