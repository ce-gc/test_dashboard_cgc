#IMPORTAR DEPENDENCIAS
import streamlit as st
import sqlite3
import pandas as pd

#CONEXIÓN A LA BASE DE DATOS

conn = sqlite3.connect("test.db")

#QUERYS Y DATAFRAMES EJ 1: número de pedidos que tienen la fecha a null, y cuales la tienen bien.

query_sin_fecha = """select 
    count(*) as Pedidos_Sin_Fecha
from sales_uuid su 
where su.transaction_date is NULL 
"""
df_sin_fecha = pd.read_sql_query(query_sin_fecha, conn)

query_con_fecha = """select 
    count(*) as Pedidos_Con_Fecha
from sales_uuid su 
where su.transaction_date is NOT NULL 
"""
df_con_fecha = pd.read_sql_query(query_con_fecha, conn)

df_grafico_fechas = pd.DataFrame({
    'Estado': ['Sin fecha', 'Con fecha'],
    'Cantidad': [
        df_sin_fecha['Pedidos_Sin_Fecha'][0],
        df_con_fecha['Pedidos_Con_Fecha'][0]
    ]
})

#QUERYS Y DATAFRAMES EJ 2: cantidades totales vendidas en cada día del último mes disponible de datos.



#QUERYS Y DATAFRAMES EJ 3: diferentes categorías de productos que se vendieron desde que tenemos histórico de datos (incluyendo fechas nulas)


#VISUALIZACIÓN DE DATOS

st.title("Celia Gómez Campelo")

#VISUALIZACIÓN EJ 1

st.text("1. Gráfica de barras, para saber el número de pedidos que tienen la fecha a null, y cuales la tienen bien.")
st.subheader("Pedidos con/sin fecha null")
st.bar_chart(df_grafico_fechas.set_index('Estado'))
col1, col2 = st.columns(2)
with col1:
    st.metric("Pedidos sin fecha", df_sin_fecha['Pedidos_Sin_Fecha'][0])
with col2:
    st.metric("Pedidos con fecha", df_con_fecha['Pedidos_Con_Fecha'][0])

st.subheader("Código Consulta 1")
st.text(query_sin_fecha)
st.text(query_con_fecha)
st.divider()

#VISUALIZACIÓN EJ 2

st.text("2. Cantidades totales vendidas en cada día del último mes disponible de datos.")
st.subheader("Total vendido diariamente en el último mes")
st.subheader("Código Consulta 2")
st.divider()

#VISUALIZACIÓN EJ 3

st.text("3. Diferentes categorías de productos que se vendieron desde que tenemos histórico de datos (incluyendo fechas nulas)")
st.subheader("Todas las categorías de datos vendidas")
st.subheader("Código Consulta 3")
st.divider()