from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_ace import st_ace
import base64

fuse_code = """
/*
=========================================================
 ATIVIDADE - FUSÃO DE SENSORES PARA ESTIMATIVA DE ALTURA
=========================================================

Fluxo geral do sistema:

Sensores (BMP180 + MPU6050)
        ↓
Leitura via funções fornecidas
        ↓
Processamento (Aqui é a sua implementação)
        ↓
Criação de pacote de telemetria
        ↓
Envio para base (função fornecida)

Você NÃO deve modificar:
- readBaroHeight()
- readAccelZ()
- getDeltaTime()
- sendToBase()

Seu trabalho está concentrado no loop().
*/

#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;

// =======================================================
// FUNÇÕES FORNECIDAS - LEITURA DOS SENSORES
// =======================================================


/*
---------------------------------------------------------
readBaroHeight()

Lê o sensor BMP180 e retorna a altura em metros.

Etapas internas:
1. Lê pressão atmosférica em Pascal.
2. Converte pressão para altura usando modelo padrão.
3. Retorna altura estimada.

IMPORTANTE:
- O valor retornado já está em METROS.
- É uma altura absoluta.
- Pode ter pequenas oscilações (ruído).
---------------------------------------------------------
*/
float readBaroHeight() {
    float pressure = bmp.readPressure();
    float seaLevel = 101325.0;  // pressão de referência
    float height = 44330.0 * (1.0 - pow(pressure / seaLevel, 0.1903));
    return height;
}


/*
---------------------------------------------------------
readAccelZ()

Lê o eixo Z do MPU6050 via I2C.

Etapas internas:
1. Acessa registrador do eixo Z.
2. Lê valor bruto (int16).
3. Converte para unidade "g".
4. Converte para m/s².

IMPORTANTE:
- O valor retornado inclui a gravidade.
- Quando parado sobre uma mesa:
      retorno ≈ +9.81 m/s²
- NÃO retorna zero quando parado.
---------------------------------------------------------
*/
float readAccelZ() {

    // Inicia comunicação com endereço do MPU6050
    Wire.beginTransmission(0x68);

    // Registrador inicial do eixo Z
    Wire.write(0x3F);

    // Finaliza escrita, mas mantém conexão ativa
    Wire.endTransmission(false);

    // Solicita 2 bytes (eixo Z)
    Wire.requestFrom(0x68, 2, true);

    // Junta os dois bytes em um inteiro de 16 bits
    int16_t raw = Wire.read() << 8 | Wire.read();

    // Conversão para g (escala ±2g)
    float accel = raw / 16384.0;

    // Conversão para m/s²
    return accel * 9.81;
}


/*
---------------------------------------------------------
sendToBase()

Simula envio de telemetria para uma base remota.

Você deve:
- Criar uma struct
- Preencher essa struct
- Passar como argumento para essa função

A função está em formato template para aceitar
qualquer tipo de struct definida por você, de modo
a não depender de uma eventual "passagem de nome igual"
para a função.
---------------------------------------------------------
*/
template <typename T>
void sendToBase(const T& packet) {
    Serial.println("[TX] Enviando pacote para base...");
}


/*
---------------------------------------------------------
Controle de tempo

getDeltaTime() retorna o intervalo de tempo (dt)
em segundos entre duas execuções consecutivas do loop().

Você DEVE usar esse valor para integração.
---------------------------------------------------------
*/
unsigned long lastTime = 0;

float getDeltaTime() {
    unsigned long now = millis();
    float dt = (now - lastTime) / 1000.0;
    lastTime = now;
    return dt;
}


// =======================================================
// SUA IMPLEMENTAÇÃO
// =======================================================

/*
---------------------------------------------------------
A partir daqui é sua responsabilidade.

Você deve:

1. Criar uma struct de telemetria.
2. Criar variáveis de estado (altura, velocidade, etc.).
3. Definir o parâmetro alpha do filtro complementar.

Dica:
As variáveis de estado precisam manter valor entre
iterações do loop(), portanto NÃO devem ser locais.
---------------------------------------------------------
*/



void setup() {

    Serial.begin(115200);

    // Inicializa comunicação I2C
    Wire.begin();

    // Inicializa BMP180
    bmp.begin();

    // Inicializa controle de tempo
    lastTime = millis();
}



void loop() {

    /*
    -----------------------------------------------------
    ETAPA 1 - LEITURA DOS SENSORES
    -----------------------------------------------------
    */

    float baroHeight = readBaroHeight();
    float accelZ = readAccelZ();
    float dt = getDeltaTime();


    /*
    -----------------------------------------------------
    A partir daqui começa a sua implementação.

    Você tem acesso a:

    baroHeight → altura absoluta em metros
    accelZ     → aceleração em m/s² (inclui gravidade)
    dt         → intervalo de tempo em segundos

    -----------------------------------------------------
    ETAPA 2 - PROCESSAMENTO
    -----------------------------------------------------

    Você deve:

    1. Tratar o sinal de aceleração
    2. Integrar para obter velocidade
    3. Integrar novamente para obter altura integrada
    4. Aplicar filtro complementar

    Perguntas que devem guiar sua implementação:

    - Se o sistema estiver parado, a velocidade deve crescer?
    - Se integrar diretamente accelZ, o que acontece?
    - Qual parte do sinal representa apenas movimento?

    -----------------------------------------------------
    */


    /*
    -----------------------------------------------------
    ETAPA 3 - TELEMETRIA
    -----------------------------------------------------

    Agora você deve:

    1. Criar uma variável do tipo da sua struct.
    2. Preencher os campos que considerar relevantes.
    3. Enviar para a base usando sendToBase().

    -----------------------------------------------------
    */


    delay(10);
}

"""

zarya_code = """
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

// ------------------------------------------------------------
// Constante do número de amostras
// ------------------------------------------------------------
const int N = 150;

// ------------------------------------------------------------
// Função para ler o arquivo de dados do satélite e armazenar
// cada coluna em um vetor diferente para trabalhar.
//
// Retorna true se a leitura bem-sucedida, e false se tiver 
// erro ao abrir ou ler o arquivo
// ------------------------------------------------------------
bool carregarDadosCSV(
    const string& nomeArquivo,
    int time_step[],
    double altitude[],
    double velocity[],
    double temperature[],
    double power[],
    int tamanho
) {
    ifstream arquivo(nomeArquivo);

    if (!arquivo.is_open()) {
        return false;
    }

    string linha;

    // Ignora o cabeçalho
    getline(arquivo, linha);

    int i = 0;

    while (getline(arquivo, linha) && i < tamanho) {
        stringstream ss(linha);
        string campo;

        getline(ss, campo, '\t');
        time_step[i] = stoi(campo);

        getline(ss, campo, '\t');
        altitude[i] = stod(campo);

        getline(ss, campo, '\t');
        velocity[i] = stod(campo);

        getline(ss, campo, '\t');
        temperature[i] = stod(campo);

        getline(ss, campo, '\t');
        power[i] = stod(campo);

        i++;
    }

    arquivo.close();
    return true;
}

int main() {

    int time_step[N];
    double altitude[N];
    double velocity[N];
    double temperature[N];
    double power[N];

    double altitude_filtrada[N];
    double velocity_filtrada[N];
    double temperature_filtrada[N];
    double power_filtrada[N];

    // ------------------------------------------------------------
    // Leitura dos dados do CSV do Zarya; como a função retorna
    // true ou false para o sucesso da operação, essa "resposta""
    // é guardada na variável "carregamento". Se tivermos sucesso,
    // printa "Sucesso ao carregar o arquivo de dados.", senão
    // printa "Erro ao carregar o arquivo de dados." e retorna um
    // número de erro (neste caso, 1) para encerrar o programa.
    // ------------------------------------------------------------
    bool carregamento = carregarDadosCSV("Zarya.csv",
                                time_step,
                                altitude,
                                velocity,
                                temperature,
                                power,
                                N);

    if (!carregamento) {
        cout << "Erro ao carregar o arquivo de dados." << endl;
        return 1;
    } else {
        cout << "Sucesso ao carregar o arquivo de dados." << endl;
    }

    // ------------------------------------------------------------
    // A partir daqui, você deve aplicar o filtro nos vetores que
    // guardam os dados (sugiro que crie uma função para o filtro),
    // guarde as leituras filtradas nos vetores "_filtrada", 
    // verifique a estabilidade (se de um dado pro outro não 
    // tiveram grandes saltos de valores, na qual sinta-se livre
    // pra julgar o que é um salto grande), e ao final, retorne as
    // colunas (altitude, velocidade, etc) que ficaram estaveis e 
    // não estaveis.
    // ------------------------------------------------------------

    return 0;
}

"""


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
        Os dados necessários para resolver o problema se encontram no txt ao final do enunciado. Você contará com uma lista de 20 bairros, cada um acompanhado de uma pontuação de viabilidade entre 0 e 100, sendo permitida a construção de estações apenas nos bairros cuja pontuação seja igual ou superior a 70. Além disso, será fornecida uma matriz de distâncias entre os bairros, com valores que variam de 0 a 20, onde 0 indica ausência de ligação direta e valores maiores representam bairros mais afastados; considere como viáveis apenas as conexões cuja distância seja menor ou igual a 10. Por fim, cada bairro também possui informações sobre os três destinos mais desejados pelos seus moradores, obtidos por meio de pesquisa populacional; se um bairro “A” deseja se deslocar até “B”, essa demanda aumenta a relevância da conexão entre eles.

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

        st.markdown("**Dica: armazene as informações dos bairros em VETORES OU MATRIZES, para facilitar o acesso aos dados, armazenando de uma forma que fique melhor para você trabalhar os mesmos. Não se preocupe com leitura de arquivo aqui, pois não é muito útil (caso fosse, eu também passaria a função que faz isso para não adicionar uma barreira de dificuldade desnecessária).**")
        
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
        st.code(zarya_code, language="cpp")

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
        with open("images/timbu.png", "rb") as f:
            data1 = f.read()
            data1_base64 = base64.b64encode(data1).decode()

        with open("images/quests/cab3.png", "rb") as f: 
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
                Questão 1 - Fusão de Sensores para Estimativa de Altura
            </span>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image("images/quests/imagem13.jpg", width=400)
        
        st.markdown("""

A fusão de sensores é uma técnica amplamente utilizada em sistemas embarcados para combinar medições provenientes de diferentes sensores com o objetivo de obter estimativas mais precisas, estáveis e robustas de uma determinada variável física.

Historicamente, técnicas de fusão de sensores ganharam grande importância em aplicações aeroespaciais e de navegação inercial, onde sistemas como aeronaves, foguetes e satélites precisavam estimar posição, velocidade e orientação combinando sensores com características distintas (alguns mais estáveis, outros beeem mais rápidos).

Hoje, essas técnicas estão presentes em drones, smartphones, robôs móveis, veículos autônomos e sistemas industriais.

Nesta atividade, você implementará um sistema simplificado de fusão de sensores para estimar altura vertical utilizando um filtro complementar para isso.

O sistema utilizará dois sensores conectados via I2C:

- **BMP180** – responsável por fornecer pressão atmosférica, a partir da qual é calculada a altura.
- **MPU6050** – responsável por fornecer aceleração linear nos três eixos.

A leitura dos sensores já está implementada no código base, utilizando:

- Biblioteca Adafruit BMP085/BMP180  
- Biblioteca Wire  

Também será fornecida uma função `sendToBase(...)`, que simula o envio de telemetria para uma base remota.

Sua responsabilidade é implementar o processamento intermediário entre a leitura dos sensores e o envio dos dados.

### Seu objetivo então é:

Estimar a altura vertical do sistema combinando (com Sensor Fuse) as leituras dos sensores do mesmo:

- A altura medida pelo barômetro BMP180 (medição absoluta, porém com ruído e menor frequência de resposta).
- A aceleração vertical medida pelo acelerômetro MPU6050 (medição de alta frequência, porém sujeita a ruído e deriva após integração).

Onde a estimativa final deverá ser obtida por meio de um filtro complementar; e enviar por meio da funcão de envio os dados empacotados para a base, enviando um só pacote de uma vez.

#### O Filtro Complementar

Para o Sensor Fuse, vocês devem utilizar um filtro complementar. O filtro complementar é uma técnica simples de fusão que combina dois sinais explorando as características complementares de cada um.

A estrutura geral do filtro é:
        """)

        st.markdown(r"""
        $$
        h_estimada = α · h_(integrada) + (1 − α) · h_(baro)
        $$
        """)

        st.markdown(""""
Onde:

- `h_integrada` é a altura obtida por integração da aceleração.
- `h_baro` é a altura medida pelo barômetro.
- `α` é um coeficiente entre 0 e 1.

O valor de `α` deve ser escolhido então por você, com base em seus critérios, e justificado/explicado.

- Valores maiores de `α` dão mais peso à estimativa dinâmica (aceleração integrada), resultando em resposta mais rápida.
- Valores menores de `α` dão mais peso ao barômetro, resultando em maior estabilidade e menor deriva.

### Informações Importantes Sobre os Sensores

#### Barômetro – BMP180

O barômetro mede pressão atmosférica. A partir dessa pressão, o código fornecido já calcula a altura utilizando um modelo padrão de atmosfera.

Isso significa que:

- A função `readBaroHeight()` já retorna a altura em metros.
- Você não precisa converter pressão para altura.
- O valor retornado representa uma estimativa direta da altura em relação ao nível de referência adotado no código.
- O sinal pode apresentar pequenas oscilações mesmo quando o sistema está parado (ruído natural do sensor).
- Se o sistema estiver parado sobre uma mesa, por exemplo, a altura retornada deve permanecer aproximadamente constante, variando apenas levemente devido ao ruído.

#### Acelerômetro – MPU6050

O acelerômetro mede aceleração específica. Esse conceito é importante.

O que isso significa na prática?

Quando o sensor está parado sobre uma superfície horizontal, ele não retorna zero. Ele retorna aproximadamente:

+9.81 m/s² no eixo vertical.

Por quê? Porque o sensor mede a acelação da gravidade. Mesmo parado, ele “sente” a força da gravidade atuando sobre ele.

Portanto:
        """)

        st.markdown(r"""
        $$
        Valor medido = aceleração do movimento + gravidade
        $$
        """)

        st.markdown("""
Se o sistema estiver parado:

- aceleração do movimento = 0  
- valor medido ≈ +9.81 m/s²  

Se o sistema estiver subindo com aceleração de +1 m/s²:

- valor medido ≈ 9.81 + 1 = 10.81 m/s²  

Se estiver descendo acelerando:

- valor medido será menor que 9.81 m/s².

Com base nas informações acima, você deverá pegar os dados que estao sendo recebidos pelos sensores, e realizar a fusão de sensores, para que os sensores sejam enviados de uma vez pela funcao SendToBase:
                    
        """)

        st.markdown(r"""
        $$
        sendToBase(packet);
        $$
        """)

        st.markdown("""

A função `sendToBase` já está implementada e simula o envio de telemetria em um sistema real. Você deve utilizá-la exatamente como fornecida.

Abaixo é fornecido o código base para você começar os trabalhos. Não modifique as funções fornecidas de leitura nem a função de envio, pois não é necessário aqui; considerando que é uma emulação do cenário real, as mesmas servem para simular o cenário.
        """)

        st.code(fuse_code, language="cpp")
