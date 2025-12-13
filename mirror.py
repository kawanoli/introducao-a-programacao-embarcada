import streamlit as st
import requests
import json
from streamlit_ace import st_ace
import textwrap

def st_success_multiline(msg: str):
    # Remove indentação da string
    msg = textwrap.dedent(msg)
    
    html = f"""
    <div style="
        background-color: #d4edda;
        color: #155724;
        padding: 5px 10px;
        margin: 5px 0;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
        font-family: sans-serif;
        white-space: pre-line;
        line-height: 1.3;
    ">
        {msg}
        <br>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def st_error_multiline(msg: str):
    msg = textwrap.dedent(msg)
    
    html = f"""
    <div style="
        background-color: #f8d7da;
        color: #721c24;
        padding: 5px 10px;
        margin: 5px 0;
        border-radius: 5px;
        border: 1px solid #f5c6cb;
        font-family: sans-serif;
        white-space: pre-line;
        line-height: 1.3;
    ">
        {msg}
        <br>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)




def editor_cpp(default_code=None, tests=None, key="editor"):
    """
    Editor C++ online com:
    - Tema
    - Slider de fonte
    - Editor Ace
    - Execução via Wandbox API
    - Testes automáticos
    """
    # --- Estado inicial ---
    if "theme" not in st.session_state:
        st.session_state.theme = "dracula"
    if "font_size" not in st.session_state:
        st.session_state.font_size = 15

    # --- Temas com ícones ---
    THEMES = {
        "dracula": "🧛‍♂️ Dracula",
        "monokai": "🟠 Monokai",
        "github": "🐙 GitHub",
        "solarized_dark": "🌑 Solarized Dark",
        "solarized_light": "🌞 Solarized Light",
        "twilight": "🌆 Twilight",
        "chaos": "🌪 Chaos",
        "tomorrow_night": "🌃 Tomorrow Night"
    }

    # --- Controles ---
    col_theme, col_font = st.columns([1, 1])

    with col_theme:
        st.session_state.theme = st.selectbox(
            "🎨 Tema:",
            list(THEMES.keys()),
            format_func=lambda t: THEMES[t],
            index=list(THEMES.keys()).index(st.session_state.theme)
        )

    with col_font:
        st.session_state.font_size = st.slider(
            "🔠 Fonte",
            min_value=8,
            max_value=36,
            value=st.session_state.font_size
        )

    # --- Código padrão ---
    if default_code is None:
        default_code = """#include <iostream>
using namespace std;

int main() {
    cout << "Hello World!" << endl;
    return 0;
}"""

    # --- Editor ---
    code = st_ace(
        value=default_code,
        language="c_cpp",
        theme=st.session_state.theme,
        font_size=st.session_state.font_size,
        tab_size=4,
        height=350,
        show_gutter=True,
        #key="editor",
        key=key,
        auto_update=True,
    )

    # --- Execução ---
    if st.button("▶️ Executar código"):
        placeholder = st.empty()
        placeholder.write("⏳ Executando...")

        # Se houver testes, executa cada um
        if tests:
            results = []
            for idx, (stdin_input, expected_output) in enumerate(tests, 1):
                payload = {
                    "code": code,
                    "compiler": "gcc-head",
                    "options": "warning,gnu++20",
                    "stdin": stdin_input
                }

                try:
                    response = requests.post(
                        "https://wandbox.org/api/compile.json",
                        data=json.dumps(payload),
                        headers={"Content-Type": "application/json"}
                    )
                    data = response.json()
                    output = ""
                    if "program_message" in data and data["program_message"]:
                        output += data["program_message"]
                    if "compiler_error" in data and data["compiler_error"]:
                        output += "\n--- COMPILER ERROR ---\n"
                        output += data["compiler_error"]
                    if "signal" in data and data["signal"]:
                        output += f"\n[Finalizado com sinal: {data['signal']}]"

                    # Normaliza strings para comparar
                    norm_output = output.strip()
                    norm_expected = expected_output.strip()

                    passed = norm_output == norm_expected
                    results.append((idx, passed, stdin_input, norm_output, norm_expected))

                except Exception as e:
                    results.append((idx, False, f"Erro: {e}", expected_output))

            placeholder.empty()
            st.write("### Resultados dos testes")
            for idx, passed, entrada, out, exp in results:
                if passed:
                    st_success_multiline(f"Teste {idx} - Passou ✅\nEntrada: {entrada}\nSaída: {out}\nEsperado: {exp}")
                    st.markdown("")
                else:
                    st_error_multiline(f"Teste {idx} - Falhou ❌\nEntrada: {entrada}\nSaída: {out}\nEsperado: {exp}")

        # Caso não haja testes, apenas executa o código
        else:
            payload = {
                "code": code,
                "compiler": "gcc-head",
                "options": "warning,gnu++20",
                "stdin": ""
            }
            try:
                response = requests.post(
                    "https://wandbox.org/api/compile.json",
                    data=json.dumps(payload),
                    headers={"Content-Type": "application/json"}
                )
                data = response.json()
                output = ""
                if "program_message" in data and data["program_message"]:
                    output += data["program_message"]
                if "compiler_error" in data and data["compiler_error"]:
                    output += "\n--- COMPILER ERROR ---\n"
                    output += data["compiler_error"]
                if "signal" in data and data["signal"]:
                    output += f"\n[Finalizado com sinal: {data['signal']}]"

                placeholder.empty()
                st.code(output if output.strip() else "Nenhuma saída produzida.", language="text")

            except Exception as e:
                placeholder.empty()
                st.error(f"Erro ao conectar à API: {e}")
