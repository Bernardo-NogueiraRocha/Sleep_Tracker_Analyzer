# auth.py
import streamlit as st

def criar_usuario(username, password):
    """Cria um novo usuário."""
    if 'usuarios' not in st.session_state:
        st.session_state.usuarios = {}
    st.session_state.usuarios[username] = password

def verificar_usuario(username, password):
    if 'usuarios' in st.session_state and username in st.session_state.usuarios:
        return st.session_state.usuarios[username] == password
    return False

def usuario_logado():
  return 'usuario' in st.session_state

def logout():
  if 'usuario' in st.session_state:
    del st.session_state['usuario']