# main.py
import streamlit as st
import auth

st.title('Registro e análise de dados de sono')

if not auth.usuario_logado():
    username = st.text_input('Usuário')
    password = st.text_input('Senha', type='password')
    if st.button('Login'):
        if auth.verificar_usuario(username, password):
            st.session_state.usuario = username
            st.success('Login realizado com sucesso!')
        else:
            st.error('Usuário ou senha incorretos.')
    if st.button('Criar usuário'):
        auth.criar_usuario(username, password)
        st.success('Usuário criado com sucesso, realize o login')
else:
    st.write(f'Bem-vindo, {st.session_state.usuario}!')
    if st.button('Logout'):
        auth.logout()
        st.rerun()
    st.write('Selecione uma página na barra lateral.')