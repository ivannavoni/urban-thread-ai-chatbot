# interfaz de web

import streamlit as st
from rag_core import build_rag, preguntar

st.title("Urban Thread - Asistente Virtual")

if "db" not in st.session_state:
    st.session_state.db, st.session_state.client = build_rag()

pregunta = st.chat_input("Escribí tu pregunta...")
if pregunta:
    respuesta = preguntar(st.session_state.db, st.session_state.client, pregunta)
    st.write(respuesta)