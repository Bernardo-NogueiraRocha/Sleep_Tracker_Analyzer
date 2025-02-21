# pages/grafico.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import auth

def plot_idades(df, num):
    fig = plt.figure(num, figsize=(10,6))
    plt.hist(df['Qualidade de sono'],bins=6, color='goldenrod')
    plt.title('Histograma qualidade de sono')
    plt.xlabel('Qualidade de sono')
    plt.ylabel('Frequência')
    plt.tight_layout()
    return fig

if not auth.usuario_logado():
    st.warning('Por favor, faça login para acessar esta página.')
    st.stop()

st.title('Gráfico de qualidade de sono')

if 'df' not in st.session_state:
    st.session_state.df = pd.read_csv('output.csv',index_col=False)

if not st.session_state.df.empty:
    fig = plot_idades(st.session_state.df, 1)
    st.pyplot(fig)
else:
    st.write('Nenhum dado disponível para gerar o gráfico.')