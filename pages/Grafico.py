# pages/grafico.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def hist_qualidade_sono(df, num):
    fig = plt.figure(num, figsize=(10,6))
    plt.hist(df['Qualidade de sono'],bins=6, color='goldenrod')
    plt.title('Histograma qualidade de sono')
    plt.xlabel('Qualidade de sono')
    plt.ylabel('Frequência')
    plt.tight_layout()
    return fig

def plot_qualidade_interrupcoes(df,num):
    fig = plt.figure(num)
    sns.barplot(data=df, x='Interrupções', y='Qualidade de sono', palette='pastel')
    plt.title('Qualidade de sono X Interrupções')
    return fig

st.title('Gráfico de qualidade de sono')

if 'df' not in st.session_state:
    st.session_state.df = pd.read_csv('output.csv',index_col=False)

if not st.session_state.df.empty:
    st.write('Qualidade de sono X Interrupções (verdadeiro ou falso):')
    fig = plot_qualidade_interrupcoes(st.session_state.df, 1)
    st.pyplot(fig)
else:
    st.write('Nenhum dado disponível para gerar o gráfico.')