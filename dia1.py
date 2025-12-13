import streamlit as st
from questoes import *

# Mapeamento: "Questão X" -> função correspondente
questoes = {
    "Questão 1": questao1,
    "Questão 2": questao2,
    "Questão 3": questao3,
    "Questão 4": questao4,
    "Questão 5": questao5,
    "Questão 6": questao6,
    "Questão 7": questao7,
    "Questão 8": questao8,
    "Questão 9": questao9,
    "Questão 10": questao10,
    "Questão 11": questao11,
    "Questão 12": questao12,
    "Questão 13": questao13,
    "Questão 14": questao14,
    "Questão 15": questao15,
    "Questão 16": questao16,
    "Questão 17": questao17,
    "Questão 18": questao18,
    "Questão 19": questao19,
    "Questão 20": questao20,
    "Questão 21": questao21,
    "Questão 22": questao22,
    "Questão 23": questao23,
    "Questão 24": questao24,
    "Questão 25": questao25,
    "Questão 26": questao26,
    "Questão 27": questao27,
    "Questão 28": questao28,
    "Questão 29": questao29,
    "Questão 30": questao30,
    "Questão 31": questao31,
    "Questão 32": questao32,
    "Questão 33": questao33,
    "Questão 34": questao34,
    "Questão 35": questao35,
    "Questão 36": questao36,
    "Questão 37": questao37,
    "Questão 38": questao38,
    "Questão 39": questao39,
    "Questão 40": questao40,
    "Questão 41": questao41,
    "Questão 42": questao42,
    "Questão 43": questao43,
    "Questão 44": questao44,
    "Questão 45": questao45,
    "Questão 46": questao46,
    "Questão 47": questao47,
    "Questão 48": questao48,
    "Questão 49": questao49,
    "Questão 50": questao50,
}

def dia_um():
    questao = st.selectbox("Selecione a questão:", list(questoes.keys()))

    # Chama a função correspondente passando a key
    questoes[questao](key=f"q{questao.split()[-1]}")

    
