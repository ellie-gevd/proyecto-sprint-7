import pandas as pd
import plotly.express as px
import streamlit as st

#Leer dataset
df = pd.read_csv('vehicles_us.csv')
#encabezado
st.header('Análisis de vehículos en Estados Unidos')
#botón histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Histograma del odómetro')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig)
#botón dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Relación entre precio y año')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig)
                        