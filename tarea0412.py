#Importar librerías
import streamlit as st
import sqlite3
import pandas as pd

#Conexión a la base de datos
conn = sqlite3.connect("test.db")

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

st.title("Celia Gómez Campelo")
st.text("1. Gráfica de barras, para saber el número de pedidos que tienen la fecha a null, y cuales la tienen bien.")
st.subheader("Pedidos con/sin fecha null")
st.bar_chart(df_grafico_fechas.set_index('Estado'))
col1, col2 = st.columns(2)
with col1:
    st.metric("Pedidos sin fecha", df_sin_fecha['Pedidos_Sin_Fecha'][0])
with col2:
    st.metric("Pedidos con fecha", df_con_fecha['Pedidos_Con_Fecha'][0])

st.subheader("Código consulta 1")
st.text(query_sin_fecha)
st.text(query_con_fecha)
st.divider()
