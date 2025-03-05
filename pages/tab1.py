# import streamlit as st
# import pandas as pd
# from scripts.query_executor import QueryExecutor

# st.set_page_config(page_title="Información General", page_icon="📊", layout="wide")

# st.title("📊 Visualización de Datos Base de Datos SIU")

# # Ruta de credenciales
# hidden_folder_path = "/home/alejandro/Documentos/workspace/JI/proyectos/credenciales_elektra"
# json_file_name = "credenciales.json"

# # Ruta del archivo SQL
# sql_file_path = "queries/query2.sql"

# # Crear instancia del QueryExecutor
# executor = QueryExecutor(hidden_folder_path, json_file_name)

# # Ejecutar la consulta
# df = executor.execute_query(sql_file_path)

# # Mostrar los resultados en Streamlit
# if not df.empty:
#     st.subheader("Tabla resumen")
#     st.dataframe(df)
# else:
#     st.error("No se pudieron recuperar datos de la base de datos.")

import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.query_executor import QueryExecutor

st.set_page_config(page_title="Información General", page_icon="📊", layout="wide")
st.title("📊 Visualización de Datos de la Base de Datos SIU")

# 📂 Configuración de conexión
hidden_folder_path = "/home/alejandro/Documentos/workspace/JI/proyectos/credenciales_elektra"
json_file_name = "credenciales.json"
sql_file_path = "queries/query2.sql"

# 📡 Obtener los datos de la base de datos
executor = QueryExecutor(hidden_folder_path, json_file_name)
df = executor.execute_query(sql_file_path)

# ✅ Verificar si hay datos
if df.empty:
    st.error("No se pudieron recuperar datos de la base de datos.")
    st.stop()

# 🛠️ Convertir columna de fecha a datetime
df["Datetime"] = pd.to_datetime(df["Datetime"])

# 🎛️ **Seleccionar rango de fechas**
st.sidebar.subheader("📅 Selecciona el Rango de Fechas")
start_date = st.sidebar.date_input("Fecha inicio", df["Datetime"].min().date())
end_date = st.sidebar.date_input("Fecha fin", df["Datetime"].max().date())

# Filtrar por fecha
df_filtered = df[(df["Datetime"].dt.date >= start_date) & (df["Datetime"].dt.date <= end_date)]

# 🎛️ **Seleccionar Analizador**
st.sidebar.subheader("🎛️ Selecciona Analizador")
analizadores = df_filtered["Analizador"].unique()
selected_analizadores = st.sidebar.multiselect("Analizadores:", analizadores, default=analizadores)

# Filtrar por analizador
df_filtered = df_filtered[df_filtered["Analizador"].isin(selected_analizadores)]

# 🎨 **Seleccionar Tipo de Gráfico**
st.sidebar.subheader("📊 Tipo de Gráfico")
tipo_grafico = st.sidebar.selectbox("Selecciona el tipo de gráfico:", ["Líneas", "Barras", "Dispersión"])

# 📌 **Seleccionar Parámetro a Graficar**
st.sidebar.subheader("📌 Parámetro a Graficar")
parametros = ["Voc", "Voce", "FF", "Isc", "Pmax", "Vmpp", "Impp", "Vmin", "Imin"]
parametro_seleccionado = st.sidebar.selectbox("Parámetro:", parametros)

# 🎨 **Generar Gráfico**
st.subheader(f"📊 Gráfico de {parametro_seleccionado} en función del tiempo")

if tipo_grafico == "Líneas":
    fig = px.line(df_filtered, x="Datetime", y=parametro_seleccionado, color="Analizador", title=f"{parametro_seleccionado} vs Tiempo")
elif tipo_grafico == "Barras":
    fig = px.bar(df_filtered, x="Datetime", y=parametro_seleccionado, color="Analizador", title=f"{parametro_seleccionado} vs Tiempo")
elif tipo_grafico == "Dispersión":
    fig = px.scatter(df_filtered, x="Datetime", y=parametro_seleccionado, color="Analizador", title=f"{parametro_seleccionado} vs Tiempo")

st.plotly_chart(fig)

# 📌 **Mostrar la Tabla de Datos Filtrada**
#st.subheader("📋 Datos Filtrados")
#st.dataframe(df_filtered)




