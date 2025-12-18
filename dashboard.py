#IMPORTAR DEPENDENCIAS
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

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
query_total_mes = """
select
    date(su.transaction_date) as dia,
    sum(su.quantity) as total_vendido
from sales_uuid su
where strftime('%Y-%m', su.transaction_date) = (
    select strftime('%Y-%m', max(transaction_date))
    from sales_uuid
    where transaction_date is not null
)
group by date(su.transaction_date)
order by dia;
"""
df_total_mes = pd.read_sql_query(query_total_mes, conn)
df_total_mes['dia'] = pd.to_datetime(df_total_mes['dia'])

#QUERYS Y DATAFRAMES EJ 3: diferentes categorías de productos que se vendieron desde que tenemos histórico de datos (incluyendo fechas nulas)
query_categorias = """
select
    pu.category AS categoria,
    sum(su.quantity) as total_vendido
from sales_uuid su
join  products_uuid pu on su.product_id = pu.product_id
group by pu.category
order by total_vendido desc;
"""

df_categorias = pd.read_sql_query(query_categorias, conn)

#VISUALIZACIÓN DE DATOS

st.title("Dashboard - Celia Gómez Campelo")

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
st.bar_chart(df_total_mes.set_index('dia')['total_vendido'])

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Vendido", f"{df_total_mes['total_vendido'].sum():,.0f}")
with col2:
    st.metric("Promedio Diario", f"{df_total_mes['total_vendido'].mean():,.1f}")
with col3:
    max_dia = df_total_mes.loc[df_total_mes['total_vendido'].idxmax(), 'dia']
    st.metric("Día con Más Ventas", max_dia.strftime('%d/%m'))

st.subheader("Código Consulta 2")
st.text(query_total_mes)
st.divider()

#VISUALIZACIÓN EJ 3
st.text("3. Diferentes categorías de productos que se vendieron desde que tenemos histórico de datos (incluyendo fechas nulas)")
st.subheader("Todas las categorías de datos vendidas")
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    df_categorias['total_vendido'], 
    labels=df_categorias['categoria'],
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.Set3.colors
)
ax.axis('equal')

st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Categorías", len(df_categorias))
with col2:
    st.metric("Total Vendido", f"{df_categorias['total_vendido'].sum():,.0f}")

st.subheader("Código Consulta 3")
st.text(query_categorias)
st.divider()