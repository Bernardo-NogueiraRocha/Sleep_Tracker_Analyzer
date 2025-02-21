# pages/registro.py
import streamlit as st
import pandas as pd

def insert_register(data: dict, df: pd.DataFrame) -> pd.DataFrame:
    """Adiciona um novo registro a um Pandas DataFrame."""
    new_df = pd.DataFrame([data])
    df = pd.concat([df, new_df], ignore_index=True)
    return df

def formulario_sono():
    with st.form("Qualidade de sono"):
        st.write('Como foi seu sono?')
        data = st.date_input('De que dia é esse registro?')
        valor = st.slider(label='Qualidade do sono', min_value=0, max_value=10)
        interrupcoes = st.checkbox('Teve interrupções no sono (ir ao banheiro, acordar no meio da noite)?')
        hora_dormir = st.time_input('Que horas foi dormir?')
        hora_acordar = st.time_input('Que horas acordou?')
        submitted = st.form_submit_button('Adicionar registro')
        if submitted:
            dados = {
                'Data': data,
                'Qualidade de sono': valor,
                'Interrupções': interrupcoes,
                'Hora de dormir': hora_dormir,
                'Hora de acordar': hora_acordar
            }
            return dados
        else:
            return None

st.title('Registro de dados de sono')

if 'df' not in st.session_state:
    st.session_state.df = pd.read_csv('output.csv',index_col=False)

dados = formulario_sono()

if dados:
    st.session_state.df = insert_register(dados, st.session_state.df)
    st.session_state.df.to_csv('output.csv', index=False)

st.table(st.session_state.df)