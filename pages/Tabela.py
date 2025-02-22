import streamlit as st
import pandas as pd

st.title('Dados de sono registrados:')

st.write(st.session_state.df)