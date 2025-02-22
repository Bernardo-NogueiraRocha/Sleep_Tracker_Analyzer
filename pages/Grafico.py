# pages/grafico.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import datetime

def hist_qualidade_sono(df, num):
    st.hist()
    fig = plt.figure(num, figsize=(10,6))
    plt.hist(df['Qualidade de sono'],bins=6, color='goldenrod')
    plt.title('Histograma qualidade de sono')
    plt.xlabel('Qualidade de sono')
    plt.ylabel('Frequência')
    plt.tight_layout()
    return fig

def plot_qualidade_interrupcoes(df:pd.DataFrame):
    st.plotly_chart(px.box(data_frame=df,x='Interrupções',y='Qualidade de sono', color='Interrupções'))

def plot_horas_dormidas(df:pd.DataFrame):
    df['Horas dormidas'] = pd.to_datetime(df['Horas dormidas'])
    st.plotly_chart(
        px.bar(df,x='Data',y='Horas dormidas', title='Data X Horas dormidas', width=1280, height=720, color='Data')
        )

def data_qualidade(df:pd.DataFrame):
    st.plotly_chart(
        px.bar(df,x='Data',y='Qualidade de sono',title='Data X Qualidade de Sono' , width=1280 , height= 720, color='Data')
        )

st.title('Gráfico de qualidade de sono')

if 'df' not in st.session_state:
    st.session_state.df = pd.read_csv('output.csv',index_col=False)

if not st.session_state.df.empty:
    st.write('Qualidade de sono X Interrupções (verdadeiro ou falso):')
    plot_qualidade_interrupcoes(st.session_state.df)
    plot_horas_dormidas(st.session_state.df)
    data_qualidade(st.session_state.df)

else:
    st.write('Nenhum dado disponível para gerar o gráfico.')