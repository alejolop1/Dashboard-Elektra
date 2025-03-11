import streamlit as st
import plotly.express as px
from scripts.query_executor import QueryExecutor
import os

# Configuración de la página
st.set_page_config(page_title="Dashboard Solar", page_icon="🌞", layout="wide")
st.title("🌞 Dashboard de Paneles Solares")

# 📂 Configuración de conexión
hidden_folder_path = "/home/alejandro/Documentos/workspace/JI/proyectos/credenciales_elektra"
json_file_name = "credenciales.json"

# 📡 Inicializar el ejecutor de queries
executor = QueryExecutor(hidden_folder_path, json_file_name)

# 📅 Selección de fechas

df["Datetime"] = pd.to_datetime(df["Datetime"])

st.sidebar.subheader("📅 Selecciona el Rango de Fechas")
start_date = st.sidebar.date_input("Fecha inicio", df["Datetime"].min().date())
end_date = st.sidebar.date_input("Fecha fin", df["Datetime"].max().date())


# 🎛️ Selección de analizadores
st.sidebar.subheader("🎛️ Selecciona Analizador")
analizadores = ["Analizador1", "Analizador2"]  # Puedes obtener esto dinámicamente
selected_analizadores = st.sidebar.multiselect("Analizadores:", analizadores, default=analizadores)

# Parámetros para las consultas
params = {
    "start_date": start_date.strftime('%Y-%m-%d'),
    "end_date": end_date.strftime('%Y-%m-%d'),
    "analizadores": ", ".join(f"'{a}'" for a in selected_analizadores)
}

# 📊 Generar gráficos simultáneos
st.subheader("📊 Visualización de Datos")

# Lista de consultas SQL (archivos .sql)
queries = {
    "Serie Temporal": "queries/serie_temporal.sql",
    "Correlación Voc vs Isc": "queries/correlacion_voc_isc.sql",
    "Distribución de Pmax": "queries/distribucion_pmax.sql"
    #"Rendimiento y Eficiencia": "queries/rendimiento_eficiencia.sql",
    #"Comparación de Analizadores": "queries/comparacion_analizadores.sql"
}

# Generar gráficos para cada consulta
for nombre_grafico, ruta_consulta in queries.items():
    st.markdown(f"### {nombre_grafico}")
    
    # Ejecutar consulta
    df = executor.execute_query_from_file(ruta_consulta, params)
    
    if df.empty:
        st.warning(f"No hay datos disponibles para {nombre_grafico} en el rango de fechas seleccionado.")
        continue
    
    # Generar gráficos según el tipo de consulta
    if nombre_grafico == "Serie Temporal":
        for parametro in ["Voc", "Voce", "FF", "Isc", "Pmax", "Vmpp", "Impp", "Vmin", "Imin"]:
            fig = px.line(df, x="Datetime", y=parametro, color="Analizador", title=f"{parametro} vs Tiempo")
            st.plotly_chart(fig, use_container_width=True)
    
    elif nombre_grafico == "Correlación Voc vs Isc":
        fig = px.scatter(df, x="Voc", y="Isc", color="Analizador", title="Voc vs Isc")
        st.plotly_chart(fig, use_container_width=True)
    
    elif nombre_grafico == "Distribución de Pmax":
        fig = px.histogram(df, x="Pmax", color="Analizador", title="Distribución de Pmax")
        st.plotly_chart(fig, use_container_width=True)
    
    elif nombre_grafico == "Rendimiento y Eficiencia":
        df["Eficiencia"] = df["Pmax"] / (df["Voc"] * df["Isc"])  # Ejemplo de cálculo de eficiencia
        fig = px.line(df, x="Datetime", y="Eficiencia", color="Analizador", title="Eficiencia vs Tiempo")
        st.plotly_chart(fig, use_container_width=True)
    
    elif nombre_grafico == "Comparación de Analizadores":
        fig = px.bar(df, x="Analizador", y="Pmax", color="Analizador", title="Comparación de Pmax por Analizador")
        st.plotly_chart(fig, use_container_width=True)