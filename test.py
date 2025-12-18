# import streamlit as st
# import sqlite3
# import pandas as pd

# conn = sqlite3.connect("test.db")

# #conn.execute("select count(*) from sales_uuid")

# query = """select
# 	product_name as Producto,
# 	sum(quantity) as Suma
# from sales_uuid su
# inner join products_uuid pu on pu.product_id = su.product_id 
# group by product_name"""

# df = pd.read_sql_query(query, conn)

# st.title("Unidades Totales Vendidas")

# df = df.sort_values("Suma", ascending=False)
# df = df.set_index("Producto")
# df.index = pd.CategoricalIndex(
#     df.index, 
#     categories=df.index.tolist(), 
#     ordered=True
# )

# st.bar_chart(df["Suma"])
# st.divider()
# st.header("Tabla completa de datos")
# #st.subheader()
# st.dataframe(df["Suma"])
# st.divider()
# st.subheader("Código de consulta")
# st.text(query)

# #print(df)
