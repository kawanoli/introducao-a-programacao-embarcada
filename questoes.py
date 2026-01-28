import streamlit as st
from mirror import editor_cpp

def questao1(key=None):
    st.markdown('<a name="q1"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 1")
    st.markdown(
        """
        Este será seu primeiro programa! Construa um programa que receba um número inteiro e armazena-o na variavel X, e mostre-o corretamente na saída.
        """
    )

    default_code_q1 = """#include <iostream>
using namespace std;

int main() {
    int x; //esta será sua variavel. armazene um valor nela!

    return 0;
}"""

    tests_q1 = [
        ("2", "2"),
        ("5", "5"),
        ("0", "0")
    ]

    editor_cpp(default_code=default_code_q1, tests=tests_q1, key="q1")

def questao2(key=None):
    st.markdown('<a name="q2"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 2")
    st.markdown(
        """
        Construa um programa (sem usar IF) que receba um número inteiro e retorne TRUE se o número for par e FALSE se o número for ímpar.
        """
    )

    default_code_q2 = """#include <iostream>
using namespace std;

int main() {
    cout << boolalpha; //nao apague essa linha, ela será importante

    return 0;
}"""

    tests_q2 = [
        ("2", "true"),
        ("5", "false"),
        ("0", "true")
    ]

    editor_cpp(default_code=default_code_q2, tests=tests_q2, key="q2")


def questao3(key=None):
    st.markdown('<a name="q3"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 3")
    st.markdown(
        """
        Escreva um programa que:

        - Declare uma variável `float` contendo uma temperatura em Celsius;
        - Converta esse valor para Fahrenheit;
        - Exiba o resultado.

        Fórmula: `F = C * 1.8 + 32`

        """
    )

    default_code_q3 = None

    tests_q3 = [
        ("0", "32"),
        ("100", "212"),
        ("-40", "-40"),
        ("25.5", "77.9")
    ]

    editor_cpp(default_code=default_code_q3, tests=tests_q3, key="q3")


def questao4(key=None):
    st.markdown('<a name="q4"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 4")
    st.markdown(
        """
        Escreva um programa que imprima o tamanho (em bytes) de:

        - `char`
        - `int`
        - `long`
        - `float`
        - `double`
        - `bool`

        Dica: use `sizeof(tipo)`.
        """
    )

    default_code_q4 = """#include <iostream>
using namespace std;

int main() {
    int x;
    cout << sizeof(x);

    return 0;
}"""

    tests_q4 = [
        ("", "1\n4\n8\n4\n8\n1")
    ]

    editor_cpp(default_code=default_code_q4, tests=tests_q4, key="q4")

def questao5(key=None):
    st.markdown('<a name="q5"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 5")
    st.markdown(
        """
        Leia três valores `int` e imprima a média usando um `float`.
        """
    )

    default_code_q5 = None

    tests_q5 = [
        ("1 2 3", "2"),
        ("10 20 30", "20"),
        ("0 0 1", "0.333333"),
        ("5 5 6", "5.33333")
    ]

    editor_cpp(default_code=default_code_q5, tests=tests_q5, key="q5")

def questao6(key=None):
    st.markdown('<a name="q6"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 6")
    st.markdown(
        """
        Considere que um ADC de 10 bits gera valores de 0 a 1023.

Escreva um programa que:

- leia um valor inteiro de ADC;
- converta para tensão (0–5 V) usando `float`;
- imprima o resultado.

Fórmula: `V = (adc * 5.0) / 1023.0`
        """
    )

    default_code_q6 = None

    tests_q6 = [
        ("0", "0.00"),
        ("1023", "5.00"),
        ("512", "2.50"),
        ("256", "1.25"),
        ("100", "0.49")
    ]

    editor_cpp(default_code=default_code_q6, tests=tests_q6, key="q6")

def questao7(key=None):
    st.markdown('<a name="q7"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 7")
    st.markdown(
        """
        Escreva um programa que:

- declare uma variável `unsigned char` representando um duty cycle (0–255);
- leia um valor do usuário;
- limite o valor para 0–255 (saturação);
- exiba o duty cycle final.
        """
    )

    default_code_q7 = None

    tests_q7 = [
        ("100", "100"),
        ("0", "0"),
        ("255", "255"),
        ("300", "255"),
        ("-20", "0")
    ]

    editor_cpp(default_code=default_code_q7, tests=tests_q7, key="q7")

def questao8(key=None):
    st.markdown('<a name="q8"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 8")
    st.markdown(
        """
        Dado um byte representando um registrador, escreva um programa que:

- ligue o bit 2;
- desligue o bit 5;
- inverta o bit 0.

Entrada: um `unsigned char`.  
Saída: o novo valor modificado.
        """
    )

    default_code_q8 = None

    tests_q8 = [
        ("0", "5"),
        ("255", "219"),
        ("32", "4"),
        ("1", "4"),
        ("36", "5")
    ]

    editor_cpp(default_code=default_code_q8, tests=tests_q8, key="q8")

def questao9(key=None):
    st.markdown('<a name="q9"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 9")
    st.markdown(
        """
        Crie uma `struct` com:

- `unsigned char id`
- `unsigned short leitura`
- `bool erro`

Depois, escreva um programa que:

- preencha um objeto dessa struct;
- imprima todos os valores.
        """
    )

    default_code_q9 = None

    tests_q9 = [
        ("1 100 0", "1 100 0"),
        ("255 65535 1", "255 65535 1"),
        ("10 500 1", "10 500 1"),
        ("0 0 0", "0 0 0")
    ]

    editor_cpp(default_code=default_code_q9, tests=tests_q9, key="q9")

def questao10(key=None):
    st.markdown('<a name="q10"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 10")
    st.markdown(
        """
        Escreva um programa que:

- leia repetidamente 5 valores `int` de um sensor;
- calcule a média inteira;
- armazene a média em uma variável `unsigned int`;
- imprima o valor final.
        """
    )

    default_code_q10 = None

    tests_q10 = [
        ("10 20 30 40 50", "30"),
        ("1 1 1 1 1", "1"),
        ("0 0 0 0 0", "0"),
        ("5 6 7 8 9", "7"),
        ("100 0 100 0 100", "60")
    ]

    editor_cpp(default_code=default_code_q10, tests=tests_q10, key="q10")

def questao11(key=None):
    st.markdown('<a name="q11"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 11")
    st.markdown(
        """
        Você quer representar temperaturas com **uma casa decimal**, usando apenas inteiros.

Escreva um programa que:

- leia um `float`;
- converta para inteiro multiplicando por 10;
- armazene o valor em uma variável `int`;
- reconstrua e exiba a temperatura dividindo por 10.0.
        """
    )

    default_code_q11 = None

    tests_q11 = [
        ("25.3", "25.3"),
        ("0.0", "0.0"),
        ("-10.7", "-10.7"),
        ("36.6", "36.6"),
        ("12.99", "12.9")
    ]

    editor_cpp(default_code=default_code_q11, tests=tests_q11, key="q11")


def questao12(key=None):
    st.markdown('<a name="q12"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 12")
    st.markdown(
        """
        Faça um programa que:

- leia um valor do ADC;
- converta para tensão (`float`);
- aplique saturação entre 0 e 4.5 V;
- imprima o resultado.
        """
    )

    default_code_q12 = None

    tests_q12 = [
        ("0", "0.00"),
        ("512", "2.50"),
        ("920", "4.50"),
        ("1023", "4.50"),
        ("100", "0.49")
    ]

    editor_cpp(default_code=default_code_q12, tests=tests_q12, key="q12")


def questao13(key=None):
    st.markdown('<a name="q13"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 13")
    st.markdown(
        """
        Crie uma `struct` contendo:

- comando (`unsigned char`);
- parâmetro (`unsigned int`);
- checksum (`unsigned char`).

O programa deve:

- ler comando e parâmetro;
- calcular o checksum como a soma dos bytes módulo 256;
- imprimir o pacote completo.
        """
    )

    default_code_q13 = None

    tests_q13 = [
        ("1 1", "1 1 2"),
        ("10 256", "10 256 11"),
        ("255 0", "255 0 255"),
        ("5 1025", "5 1025 11"),
        ("1 16909060", "1 16909060 11")
    ]

    editor_cpp(default_code=default_code_q13, tests=tests_q13, key="q13")


def questao14(key=None):
    st.markdown('<a name="q14"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 14")
    st.markdown(
        """
        Dado um valor inteiro entre 0 e 1023, converta para duty cycle de 0 a 255:

`duty = adc / 4;`

Escreva um programa que:

- leia o valor de `adc`;
- converta;
- armazene em um `unsigned char`;
- exiba o resultado.
        """
    )

    default_code_q14 = None

    tests_q14 = [
        ("0", "0"),
        ("4", "1"),
        ("255", "63"),
        ("512", "128"),
        ("1023", "255")
    ]

    editor_cpp(default_code=default_code_q14, tests=tests_q14, key="q14")


def questao15(key=None):
    st.markdown('<a name="q15"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 15")
    st.markdown(
        """
        Leia três valores inteiros e determine o maior deles usando apenas if/else.  
Não utilize funções prontas.
        """
    )

    default_code_q15 = None

    tests_q15 = [
        ("1 2 3", "3"),
        ("10 5 7", "10"),
        ("-1 -2 -3", "-1"),
        ("5 5 3", "5"),
        ("7 7 7", "7")
    ]

    editor_cpp(default_code=default_code_q15, tests=tests_q15, key="q15")


def questao16(key=None):
    st.markdown('<a name="q16"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 16")
    st.markdown(
        """
        Crie um sistema que leia um estado inteiro e execute:
0 – INICIALIZANDO 
1 – OPERANDO 
2 – ERRO 
3 – DESLIGADO

Escreva usando switch.
        """
    )

    default_code_q16 = None

    tests_q16 = [
        ("0", "INICIALIZANDO"),
        ("1", "OPERANDO"),
        ("2", "ERRO"),
        ("3", "DESLIGADO"),
        ("5", "ESTADO INVALIDO")
    ]

    editor_cpp(default_code=default_code_q16, tests=tests_q16, key="q16")


def questao17(key=None):
    st.markdown('<a name="q17"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 17")
    st.markdown(
        """
        Leia um caractere que representa um comando:  
'L' = ligar, 'D' = desligar, 'R' = reiniciar.  
Use switch para determinar a ação.

Trate também caracteres inválidos.
        """
    )

    default_code_q17 = None

    tests_q17 = [
        ("L", "LIGAR"),
        ("D", "DESLIGAR"),
        ("R", "REINICIAR"),
        ("X", "COMANDO INVALIDO"),
        ("l", "COMANDO INVALIDO")
    ]

    editor_cpp(default_code=default_code_q17, tests=tests_q17, key="q17")


def questao18(key=None):
    st.markdown('<a name="q18"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 18")
    st.markdown(
        """
        Escreva um programa que:
    - leia um valor para um unsigned short;
    - some outro valor a ele;
    - detecte se ocorreu overflow (valor ultrapassou 65535);
    - exiba uma mensagem indicando o resultado.
        """
    )

    default_code_q18 = None

    tests_q18 = [
        ("100 200", "RESULTADO 300"),
        ("65535 0", "RESULTADO 65535"),
        ("65535 1", "OVERFLOW"),
        ("60000 5535", "OVERFLOW"),
        ("0 65535", "RESULTADO 65535")
    ]

    editor_cpp(default_code=default_code_q18, tests=tests_q18, key="q18")


def questao19(key=None):
    st.markdown('<a name="q19"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 19")
    st.markdown(
        """
        Um microcontrolador possui três modos:  
0 – MANUAL, 
1 – AUTOMÁTICO, 
2 – CALIBRAÇÃO.  

Crie um programa que:
- Leia o modo  
- Se modo inválido (<0 ou >2), exiba “Modo inválido”  
- Caso válido, execute ação correspondente  

Atente-se à:
- Deixe como padrão o modo Automático caso seja digitado um modo inválido.

Implemente usando switch e trate o default adequadamente.
        """
    )

    default_code_q19 = None

    tests_q19 = [
        ("0", "MANUAL"),
        ("1", "AUTOMÁTICO"),
        ("2", "CALIBRAÇÃO"),
        ("-1", "Modo inválido\nAUTOMÁTICO"),
        ("5", "Modo inválido\nAUTOMÁTICO")
    ]

    editor_cpp(default_code=default_code_q19, tests=tests_q19, key="q19")


def questao20(key=None):
    st.markdown('<a name="q20"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 20")
    st.markdown(
        """Crie uma struct com:
    - int corrente (0--20000 mA);
    - unsigned int tensao_x10 (ex: 127 representa 12.7 V);
    - bool ligado;
    - unsigned short status;

O programa deve:
    1. preencher os dados da telemetria;
    2. validar faixas (corrente $>$ 20000 indica erro, e a tensão deve ser maior do que 3.3V e menor do que 5V);
    3. converter \texttt{tensao\_x10} para volts reais e imprimir.
    4. caso o status seja "ligado" e uma das faixas esteja fora do esperado, mude o status para desligado
    5. printe ao final do preenchimento dos dados o status junto das informações do dispositivo
        """
    )

    default_code_q20 = None

    tests_q20 = [
        ("10000 45 1 1", "10000 4.5 1 1"),
        ("21000 45 1 1", "21000 4.5 0 0"),
        ("15000 30 1 2", "15000 3.0 0 0"),
        ("15000 40 0 3", "15000 4.0 0 3"),
        ("20000 49 1 5", "20000 4.9 1 5")
    ]

    editor_cpp(default_code=default_code_q20, tests=tests_q20, key="q20")


def questao21(key=None):
    st.markdown('<a name="q21"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 21")
    st.markdown(
        """
        Faça uma calculadora que leia um valor ou um caractere (+, -, *, /, =) representando a operação. Permita que hajam múltiplas operações por vez (exemplo: 2 + 6 - 3), executando o cálculo final apenas após o sinal de igualdade (=) ser lido.
    - Se o caractere for inválido, exiba mensagem de erro  
    - Se a operação for divisão, verifique divisão por zero 
    - Permita um novo cálculo ser realizado após mostrar o resultado de um cálculo anterior enviando novamente o sinal de igualdade (=).
    - Permita configurar a calculadora para realizar contas inteiras ou decimais.
        """
    )

    default_code_q21 = None

    tests_q21 = [
        ("1\n2 + 6 - 3 =", "5.00"),
        ("0\n10 / 3 =", "3"),
        ("1\n10 / 4 =", "2.50"),
        ("0\n5 / 0 =", "ERRO"),
        ("1\n2 + 3 * 4 =", "20.00"),
        ("1\n2 + x =", "ERRO")
    ]

    editor_cpp(default_code=default_code_q21, tests=tests_q21, key="q21")


def questao22(key=None):
    st.markdown('<a name="q22"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 22")
    st.markdown(
        """
        Escreva um programa que leia continuamente um valor de um sensor (simando as entradas com um cin), processe esse valor e exiba no console a cada iteração.  
O programa deve rodar utilizando um laço while() até que o sensor começe a dar entradas ruidosas (entradas negativas).
        """
    )

    default_code_q22 = None

    tests_q22 = [
        ("10 20 30 -1", "10\n20\n30"),
        ("0 5 0 -3", "0\n5\n0"),
        ("100 -1", "100"),
        ("-1", ""),
        ("3 2 1 0 -5", "3\n2\n1\n0")
    ]

    editor_cpp(default_code=default_code_q22, tests=tests_q22, key="q22")


def questao23(key=None):
    st.markdown('<a name="q23"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 23")
    st.markdown(
        """
        Faça um programa que utilize o laço for para piscar um LED 10 vezes.  
A cada iteração, o LED deve ligar por 500 ms e desligar por 500 ms.
        """
    )

    default_code_q23 = None

    tests_q23 = [
        ("", 
        "LED ON\nLED OFF\n"
        "LED ON\nLED OFF\n"
        "LED ON\nLED OFF\n"
        "LED ON\nLED OFF\n"
        "LED ON\nLED OFF\n"
        "LED ON\nLED OFF\n"
        "LED ON\nLED OFF\n"
        "LED ON\nLED OFF\n"
        "LED ON\nLED OFF\n"
        "LED ON\nLED OFF")
    ]

    editor_cpp(default_code=default_code_q23, tests=tests_q23, key="q23")


def questao24(key=None):
    st.markdown('<a name="q24"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 24")
    st.markdown(
        """
        Implemente um filtro de média simples usando um laço for.  
O programa deve ler o ADC 8 vezes, somar os valores e calcular a média inteira.
        """
    )

    default_code_q24 = None

    tests_q24 = [
        ("100 100 100 100 100 100 100 100", "100"),
        ("0 0 0 0 0 0 0 0", "0"),
        ("10 20 30 40 50 60 70 80", "45"),
        ("1 2 3 4 5 6 7 8", "4"),
        ("1023 1023 1023 1023 1023 1023 1023 1023", "1023")
    ]

    editor_cpp(default_code=default_code_q24, tests=tests_q24, key="q24")


def questao25(key=None):
    st.markdown('<a name="q25"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 25")
    st.markdown(
        """
        Escreva um programa que:
    - crie um array de char com tamanho 20;
    - leia uma string do usuário;
    - copie para o array sem usar std::string;
    - exiba caractere por caractere até encontrar \\0.
        """
    )

    default_code_q25 = None

    tests_q25 = [
        ("abc", "a\nb\nc"),
        ("HELLO", "H\nE\nL\nL\nO"),
        ("a", "a"),
        ("teste123", "t\ne\ns\nt\ne\n1\n2\n3"),
        ("Zyx", "Z\ny\nx")
    ]

    editor_cpp(default_code=default_code_q25, tests=tests_q25, key="q25")


def questao26(key=None):
    st.markdown('<a name="q26"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 26")
    st.markdown(
        """
        Considere 8 registradores de 8 bits simulados em um vetor uint8_t registradores[8].  
- Inicialize cada registrador com valores diferentes.  
- Crie uma rotina que zere os registradores de índice par e dobre os registradores de índice ímpar.  
- Imprima todos os valores após a modificação.  
Explique como o vetor permite manipulação direta de memória sem overhead de estruturas complexas.
        """
    )

    default_code_q26 = None

    tests_q26 = [
        ("", "0\n4\n0\n8\n0\n12\n0\n16")
    ]

    editor_cpp(default_code=default_code_q26, tests=tests_q26, key="q26")


def questao27(key=None):
    st.markdown('<a name="q27"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 27")
    st.markdown(
        """
        Crie um vetor de 10 elementos \texttt{uint16\_t buffer[10]}.  
- Leia valores simulados de 0 a 12000.  
- Caso um valor seja maior que 10000, limite-o a 10000 (saturação).  
- Imprima os valores finais.  
        """
    )

    default_code_q27 = None

    tests_q27 = [
        ("0 5000 10000 12000 9999 10001 8000 15000 100 42",
        "0\n5000\n10000\n10000\n9999\n10000\n8000\n10000\n100\n42"),
        ("12000 12000 12000 12000 12000 12000 12000 12000 12000 12000",
        "10000\n10000\n10000\n10000\n10000\n10000\n10000\n10000\n10000\n10000"),
        ("0 1 2 3 4 5 6 7 8 9",
        "0\n1\n2\n3\n4\n5\n6\n7\n8\n9")
    ]

    editor_cpp(default_code=default_code_q27, tests=tests_q27, key="q27")


def questao28(key=None):
    st.markdown('<a name="q28"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 28")
    st.markdown(
        """
        Crie um vetor de 10 elementos do tipo inteiro para simular uma leitura de um sensor.  
- Leia valores simulados de 0 a 255.  
- A cada novo número lido, compare esse número lido com a média simples das três leituras anteriores; caso a diferença da nova leitura para essa média seja maior do que 20, some a nova leitura com essa média e divida por dois para substituir essa leitura ruidosa.  
- Como com os três primeiros valores não será possível aplicar esse filtro, apenas leia-os normalmente.
- Imprima o array final da leitura do sensor.  
        """
    )

    default_code_q28 = None

    tests_q28 = [
        (
            "10 12 11 50 13 14 80 15 16 17",
            "10\n12\n11\n30\n13\n14\n48\n15\n16\n17"
        ),
        (
            "100 100 100 200 100 100 100 200 100 100",
            "100\n100\n100\n150\n100\n100\n100\n150\n100\n100"
        ),
        (
            "0 0 0 50 0 0 0 50 0 0",
            "0\n0\n0\n25\n0\n0\n0\n25\n0\n0"
        )
    ]
    

    editor_cpp(default_code=default_code_q28, tests=tests_q28, key="q28")


def questao29(key=None):
    st.markdown('<a name="q29"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 29")
    st.markdown(
        """
        Crie uma função float converterADC(int leitura) que receba um valor de 0 a 1023 e retorne a tensão correspondente em volts (0--5V).  

No main(), leia três valores de ADC, chame a função para cada um e imprima o resultado.
        """
    )

    default_code_q29 = None

    tests_q29 = [
        ("0 512 1023", "0\n2.50244\n5"),
        ("1023 0 0", "5\n0\n0"),
        ("256 512 768", "1.25122\n2.50244\n3.75367")
    ]

    editor_cpp(default_code=default_code_q29, tests=tests_q29, key="q29")


def questao30(key=None):
    st.markdown('<a name="q30"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 30")
    st.markdown(
        """
        Implemente uma função int saturar(int valor, int minimo, int maximo) que limite o valor ao intervalo dado.  
Use a função para saturar leituras simuladas de um sensor entre 0 e 1000.  

Mostre valores antes e depois da saturação.
        """
    )

    default_code_q30 = None

    tests_q30 = [
        (
            "-100 0 500 1200 1000",
            "-100 0\n0 0\n500 500\n1200 1000\n1000 1000"
        ),
        (
            "2000 -50 300 999 1001",
            "2000 1000\n-50 0\n300 300\n999 999\n1001 1000"
        )
    ]

    editor_cpp(default_code=default_code_q30, tests=tests_q30, key="q30")

def questao31(key=None):
    st.markdown('<a name="q31"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 31")
    st.markdown(
        """
        Crie uma função float media(int v[], int tamanho) que calcule a média dos valores de um vetor de inteiros.  

No main(), preencha um vetor com 10 leituras simuladas e exiba a média resultante.
        """
    )

    default_code_q31 = None

    tests_q31 = [
        ("10 10 10 10 10 10 10 10 10 10", "10"),
        ("0 1 2 3 4 5 6 7 8 9", "4.5"),
        ("100 200 300 400 500 600 700 800 900 1000", "550"),
        ("1 2 3 4 5 6 7 8 9 10", "5.5")
    ]

    editor_cpp(default_code=default_code_q31, tests=tests_q31, key="q31")


def questao32(key=None):
    st.markdown('<a name="q32"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 32")
    st.markdown(
        """
        Crie uma função bool debounce(bool leituraAtual, bool leituraAnterior) que retorne verdadeiro somente se o valor atual for igual ao anterior.  

Simule uma sequência de leituras ruidosas de botão em um vetor e exiba o valor "filtrado" a cada iteração.
        """
    )

    default_code_q32 = """
bool leituras[10] = {0, 1, 0, 1, 1, 1, 0, 0, 1, 1};
"""

    tests_q32 = [
        ("", "0\n0\n0\n0\n1\n1\n0\n1\n0\n1")
    ]

    editor_cpp(default_code=default_code_q32, tests=tests_q32, key="q32")


def questao33(key=None):
    st.markdown('<a name="q33"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 33")
    st.markdown(
        """
        Crie uma struct Pacote com:  
    - unsigned char comando
    - unsigned int parametro
    - unsigned char checksum

Implemente uma função unsigned char calcularChecksum(Pacote p) que retorne a soma de seus campos módulo 256.

Crie um pacote no main(), calcule o checksum e exiba o resultado.
        """
    )

    default_code_q33 = None

    tests_q33 = [
        ("1 100", "101"),
        ("10 500", "254"),
        ("255 1", "0"),
        ("0 0", "0")
    ]

    editor_cpp(default_code=default_code_q33, tests=tests_q33, key="q33")


def questao34(key=None):
    st.markdown('<a name="q34"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 34")
    st.markdown(
        """
        Implemente:

- int lerCorrente() -- retorna 0 a 20000 mA.  
- bool correnteAlta(int c) -- retorna true se acima de 15000 mA.  
- void emitirAlerta() -- imprime 'ALERTA: CORRENTE ALTA'.  

Leia 5 valores e acione o alerta quando necessário usando os módulos.
        """
    )

    default_code_q34 = None

    tests_q34 = [
        (
            "10000 16000 14000 18000 20000",
            "ALERTA: CORRENTE ALTA\nALERTA: CORRENTE ALTA\nALERTA: CORRENTE ALTA"
        ),
        (
            "0 5000 10000 15000 15000",
            ""
        ),
        (
            "16001 16002 16003 16004 16005",
            "ALERTA: CORRENTE ALTA\nALERTA: CORRENTE ALTA\nALERTA: CORRENTE ALTA\nALERTA: CORRENTE ALTA\nALERTA: CORRENTE ALTA"
        )
    ]

    editor_cpp(default_code=default_code_q34, tests=tests_q34, key="q34")


def questao35(key=None):
    st.markdown('<a name="q35"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 35")
    st.markdown(
        """
        Crie três funções para simular procesamento de firmware:

- int lerSensorRuido() → retorna valores aleatórios entre 0 e 1023.  
- int filtroMediaSimples(int atual, int anterior) → retorna a média.  
- float converterTensao(int adc) → converte para 0--5 V.

Simule 10 leituras aplicando o pipeline: ler → filtrar → converter.
        """
    )

    default_code_q35 = "int dadosSimulados[10] = {100, 300, 600, 400, 800, 200, 1023, 500, 250, 750};"

    tests_q35 = [
        (
        "",
        "0.488759\n"
        "0.977517\n"
        "2.19922\n"
        "2.44379\n"
        "2.93255\n"
        "2.44379\n"
        "3.50049\n"
        "3.67605\n"
        "1.83109\n"
        "2.44379"
    )
    ]

    editor_cpp(default_code=default_code_q35, tests=tests_q35, key="q35")


def questao36(key=None):
    st.markdown('<a name="q36"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 36")
    st.markdown(
        """
        Crie a struct Telemetria contendo:

- int corrente;  
- unsigned int tensao_x10;  
- unsigned short flags;  
- bool erro;

Funções:

- Telemetria lerDados()  
- bool validar(Telemetria t)  
- void imprimir(Telemetria t)

Simule a leitura de 5 pacotes de telemetria e indique quais são válidos.
        """
    )

    default_code_q36 = """Telemetria dadosSimulados[5] = {
    {12000, 45, 0x01, false},
    {22000, 40, 0x02, false},
    {8000,  30, 0x03, false},
    {15000, 50, 0x04, true},
    {10000, 42, 0x05, false}
};
"""

    tests_q36 = [
        (
            "",
            "Corrente: 12000 mA\n"
            "Tensao: 4.5 V\n"
            "Flags: 1\n"
            "Erro: NAO\n"
            "Pacote VALIDO\n"
            "-------------------\n"
            "Corrente: 22000 mA\n"
            "Tensao: 4 V\n"
            "Flags: 2\n"
            "Erro: NAO\n"
            "Pacote INVALIDO\n"
            "-------------------\n"
            "Corrente: 8000 mA\n"
            "Tensao: 3 V\n"
            "Flags: 3\n"
            "Erro: NAO\n"
            "Pacote INVALIDO\n"
            "-------------------\n"
            "Corrente: 15000 mA\n"
            "Tensao: 5 V\n"
            "Flags: 4\n"
            "Erro: SIM\n"
            "Pacote INVALIDO\n"
            "-------------------\n"
            "Corrente: 10000 mA\n"
            "Tensao: 4.2 V\n"
            "Flags: 5\n"
            "Erro: NAO\n"
            "Pacote VALIDO\n"
            "-------------------"
        )
    ]

    editor_cpp(default_code=default_code_q36, tests=tests_q36, key="q36")


def questao37(key=None):
    st.markdown('<a name="q37"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 37")
    st.markdown(
        """
        Use um vetor de 10 posições para simular um buffer circular.
Funções:

- void inserir(int buf[], int \&indice, int valor)  
- void imprimirBuffer(int buf[], int tamanho)

O índice deve retornar a zero quando chegar ao fim.
Insira 20 valores simulados (de 1 a 20) no buffer.

Dica: usar operador % para "voltar ao início".
        """
    )

    default_code_q37 = None

    tests_q37 = [
        (
            "",
            "10 11 12 13 14 15 16 17 18 19"
        )
    ]

    editor_cpp(default_code=default_code_q37, tests=tests_q37, key="q37")


def questao38(key=None):
    st.markdown('<a name="q38"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 38")
    st.markdown(
        """
        Implemente:

- void lerAmostras(int v[], int n)  
- int mediaJanela(int v[], int pos, int janela)
- void exibirAmostraFiltrada(int valor)

Simule um filtro de média móvel com janela 3 em 20 amostras seguidas.
Calcule a média apenas quando houver janela completa.
        """
    )

    default_code_q38 = None

    tests_q38 = [
        (
            "",
            "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18"
        )
    ]

    editor_cpp(default_code=default_code_q38, tests=tests_q38, key="q38")


def questao39(key=None):
    st.markdown('<a name="q39"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 39")
    st.markdown(
        """
        Crie as funções:

- void tarefaSensor() 
- void tarefaDisplay()  
- void tarefaComunicacao()

No main(), simule 20 'ticks' de tempo.
Execute cada tarefa em intervalos diferentes:

- Sensor a cada 1 tick  
- Display a cada 2 ticks  
- Comunicação a cada 5 ticks
        """
    )

    default_code_q39 = None

    tests_q39 = [
        (
            "",
            "Tick 1: SENSOR\n"
            "Tick 2: SENSOR\n"
            "Tick 2: DISPLAY\n"
            "Tick 3: SENSOR\n"
            "Tick 4: SENSOR\n"
            "Tick 4: DISPLAY\n"
            "Tick 5: SENSOR\n"
            "Tick 5: COMUNICACAO\n"
            "Tick 6: SENSOR\n"
            "Tick 6: DISPLAY\n"
            "Tick 7: SENSOR\n"
            "Tick 8: SENSOR\n"
            "Tick 8: DISPLAY\n"
            "Tick 9: SENSOR\n"
            "Tick 10: SENSOR\n"
            "Tick 10: DISPLAY\n"
            "Tick 10: COMUNICACAO\n"
            "Tick 11: SENSOR\n"
            "Tick 12: SENSOR\n"
            "Tick 12: DISPLAY\n"
            "Tick 13: SENSOR\n"
            "Tick 14: SENSOR\n"
            "Tick 14: DISPLAY\n"
            "Tick 15: SENSOR\n"
            "Tick 15: COMUNICACAO\n"
            "Tick 16: SENSOR\n"
            "Tick 16: DISPLAY\n"
            "Tick 17: SENSOR\n"
            "Tick 18: SENSOR\n"
            "Tick 18: DISPLAY\n"
            "Tick 19: SENSOR\n"
            "Tick 20: SENSOR\n"
            "Tick 20: DISPLAY\n"
            "Tick 20: COMUNICACAO"
        )
    ]

    editor_cpp(default_code=default_code_q39, tests=tests_q39, key="q39")


def questao40(key=None):
    st.markdown('<a name="q40"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 40")
    st.markdown(
        """
        Implemente um firmware simulado contendo:

Módulos:    
- Leitura de 3 sensores  
- Filtro simples (média de 3)  
- Conversão para unidades reais (°C, V, mA)  
- Verificação de faixas de segurança  
- Exibição formatada  

Use funções para cada módulo.  
Simule 15 ciclos completos do sistema.

O resultado deve indicar quando algum sensor está fora da faixa.
        """
    )

    default_code_q40 = None

    tests_q40 = [
        (
            "",
            "Ciclo 0: OK\n"
            "Ciclo 1: OK\n"
            "Ciclo 2: OK\n"
            "Ciclo 3: OK\n"
            "Ciclo 4: OK\n"
            "Ciclo 5: OK\n"
            "Ciclo 6: OK\n"
            "Ciclo 7: OK\n"
            "Ciclo 8: OK\n"
            "Ciclo 9: OK\n"
            "Ciclo 10: ALERTA\n"
            "Ciclo 11: ALERTA\n"
            "Ciclo 12: ALERTA\n"
            "Ciclo 13: ALERTA\n"
            "Ciclo 14: ALERTA"
        )
    ]

    editor_cpp(default_code=default_code_q40, tests=tests_q40, key="q40")


def questao41(key=None):
    st.markdown('<a name="q41"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 41")
    st.markdown(
        """
        O programa compila, mas pode causar comportamento indefinido em tempo de execução. Explique o problema e proponha uma solução correta.
        """
    )

    default_code_q41 = """int main() {
    int v[5];
    v[5] = 10;   // erro
}"""

    tests_q41 = [
        ("", "")
    ]

    editor_cpp(default_code=default_code_q41, tests=tests_q41, key="q41")


def questao42(key=None):
    st.markdown('<a name="q42"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 42")
    st.markdown(
        """
        O programa abaixo executa, mas gera um resultado incorreto devido a overflow. Explique e corrija o problema.
        """
    )

    default_code_q42 = """int main() {
    unsigned char contador = 250;
    for (int i = 0; i < 10; i++) {
        contador++;
    }
    cout << (int)contador << endl;
}"""

    tests_q42 = [
        ("", "260")
    ]

    editor_cpp(default_code=default_code_q42, tests=tests_q42, key="q42")


def questao43(key=None):
    st.markdown('<a name="q43"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 43")
    st.markdown(
        """
        O programa tenta converter uma leitura de ADC (10 bits) para tensão em volts.  
Entretanto, o resultado calculado está incorreto. Identifique o erro e corrija.
        """
    )

    default_code_q43 = """int main() {
    unsigned short adc = 900;
    float tensao = (adc * 5) / 1023;  // erro de tipo
    cout << tensao;
}"""

    tests_q43 = [
        ("", "4.39922")
    ]

    editor_cpp(default_code=default_code_q43, tests=tests_q43, key="q43")


def questao44(key=None):
    st.markdown('<a name="q44"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 44")
    st.markdown(
        """
        O código calcula um duty cycle baseado em um valor de sensor.  
Contudo, ele pode gerar estouro em \texttt{unsigned char}.  
Explique o erro e implemente uma saturação segura para 0–255.
        """
    )

    default_code_q44 = """int main() {
    unsigned char pwm;
    int leitura = 400;
    pwm = leitura * 2; // pode passar de 255
    cout << (int)pwm;
}"""

    tests_q44 = [
        ("", "255")
    ]

    editor_cpp(default_code=default_code_q44, tests=tests_q44, key="q44")


def questao45(key=None):
    st.markdown('<a name="q45"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 45")
    st.markdown(
        """
        O código abaixo tenta ativar o bit 3, mas o resultado não está correto.  
Explique o problema e apresente a forma certa de manipular o registrador.
        """
    )

    default_code_q45 = """int main() {
    unsigned char reg = 0b00000000;
    reg = reg | 3;   // ativa bits errados
    cout << (int)reg;
}"""

    tests_q45 = [
        ("", "8")
    ]

    editor_cpp(default_code=default_code_q45, tests=tests_q45, key="q45")


def questao46(key=None):
    st.markdown('<a name="q46"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 46")
    st.markdown(
        """
        Escreva uma função recursiva que encontre o menor valor em um vetor de leituras de ADC (valores de 0 a 1023).
        """
    )

    default_code_q46 = """// menorValorRec(v, n)"""

    tests_q46 = [
        # Teste 1 – Valores variados
        (
            "512 400 300 900 1023 250 600 700 100 800",
            "100"
        ),

        # Teste 2 – Menor valor no início
        (
            "0 200 400 600 800 1023 500 300 700 900",
            "0"
        ),

        # Teste 3 – Todos valores iguais
        (
            "256 256 256 256 256 256 256 256 256 256",
            "256"
        )
    ]

    editor_cpp(default_code=default_code_q46, tests=tests_q46, key="q46")


def questao47(key=None):
    st.markdown('<a name="q47"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 47")
    st.markdown(
        r"""
        Considere o filtro digital recursivo:

$$ 
y[n] = y[n-1] + \alpha (x[n] - y[n-1]) 
$$

Implemente uma função que receba:

- vetor de entradas `x[]`,
- índice atual `n`,
- coeficiente `alpha`,

e calcule recursivamente o valor de `y[n]`.  
Use `y[0] = x[0]` como caso base.
        """
    )

    default_code_q47 = """// filtroIIR(x, n, alpha)"""

    tests_q47 = [
        (
            "5\n100 100 100 100 100\n0.5",
            "100"
        ),
        (
            "5\n0 0 100 100 100\n0.25",
            "57.8125"
        ),
        (
            "4\n0 100 100 100\n0.8",
            "99.2"
        )
    ]

    editor_cpp(default_code=default_code_q47, tests=tests_q47, key="q47")


def questao48(key=None):
    st.markdown('<a name="q48"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 48")
    st.markdown(
        r"""
        Implemente uma função recursiva que calcule um filtro exponencial:

$$ 
y[n] = \alpha x[n] + (1 - \alpha) y[n-1]
$$

Dado um vetor de 8 leituras de temperatura, calcule o valor final `y[7]`.
        """
    )

    default_code_q48 = """// filtroExp(x, n, alpha)"""

    tests_q48 = [
        (
            "8\n10 10 10 10 10 10 10 10\n0.5",
            "10"
        ),
        (
            "8\n0 0 0 0 100 100 100 100\n0.25",
            "57.8125"
        ),
        (
            "8\n20 22 24 26 28 30 32 34\n0.3",
            "30.0426"
        )
    ]

    editor_cpp(default_code=default_code_q48, tests=tests_q48, key="q48")


def questao49(key=None):
    st.markdown('<a name="q49"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 49")
    st.markdown(
        r"""
        Implemente uma rotina recursiva que receba um vetor de leituras ruidosas e retorne a leitura suavizada final usando:

$$ 
y[n] = \frac{x[n] + y[n-1]}{2} 
$$

Faça o caso base: `y[0] = x[0]`.

Explique por que essa implementação não seria ideal em um firmware real.
        """
    )

    default_code_q49 = """// suaviza(x, n)"""

    tests_q49 = [
        (
            "5\n10 10 10 10 10",
            "10"
        ),
        (
            "5\n0 0 100 100 100",
            "87.5"
        ),
        (
            "6\n20 30 40 50 60 70",
            "59.375"
        )
    ]

    editor_cpp(default_code=default_code_q49, tests=tests_q49, key="q49")


def questao50(key=None):
    st.markdown('<a name="q50"></a>', unsafe_allow_html=True)
    st.markdown("## Questão 50")
    st.markdown(
        r"""
        Você deve criar uma função recursiva que aplique o filtro abaixo repetidamente N vezes:


$$
f(v) = \frac{v + \text{ruido}}{2}
$$


onde `ruido` é um inteiro lido do usuário.  
Execute a função 5 vezes e imprima o valor final.

Dica: o caso base é quando `n == 0`.
        """
    )

    default_code_q50 = """// aplicaRuido(v, n)"""

    tests_q50 = [
        (
            "100\n0",
            "3.125"
        ),
        (
            "0\n100",
            "96.875"
        ),
        (
            "50\n50",
            "50"
        )
    ]

    editor_cpp(default_code=default_code_q50, tests=tests_q50, key="q50")


# use \n
"""
ESTRUTURA QUESTAO:

def questaoX(key=None):
    st.markdown('<a name="qX"></a>', unsafe_allow_html=True)
    st.markdown("## Questão X")
    st.markdown(ENUNCIADO ENTRE ASPAS TRIPLA)

    default_code_q2 = CÓDIGO CPP ENTRE ASPAS TRIPLA

    tests_q2 = [
        ("2", "true"),
        ("5", "false"),
        ("0", "true")
    ]

    editor_cpp(default_code=default_code_qX, tests=tests_qX, key="qX")
"""