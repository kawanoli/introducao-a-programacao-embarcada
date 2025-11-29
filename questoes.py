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