import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.query_executor import QueryExecutor

# Configuración de la página
st.set_page_config(page_title="Visualizaciones", page_icon="📈", layout="wide")
st.title("📈 Visualización de Parámetros de Paneles Solares")

# Path a las credenciales
hidden_folder_path = "/home/alejandro/Documentos/workspace/JI/proyectos/credenciales_elektra"
json_file_name = "credenciales.json"

# Inicializar el ejecutor de consultas
query_executor = QueryExecutor(hidden_folder_path, json_file_name)

# Selección de analizador
analizadores = ["Anp01", "Anp02", "Anp03", "Anp04", "Anp05"]  # Ejemplo de analizadores
selected_analizador = st.selectbox("Seleccione el analizador", analizadores)

# Cargar datos históricos (sin filtrar por fechas)
@st.cache_data
def cargar_datos_historicos(analizador):
    params = {
        'analizador': analizador
    }
    df = query_executor.execute_query_from_file("queries/query_historico.sql", params)
    return df

# Cargar datos
df_historico = cargar_datos_historicos(selected_analizador)

# Verificar si hay datos
if not df_historico.empty:
    # Convertir la columna 'Datetime' a tipo datetime
    df_historico["Datetime"] = pd.to_datetime(df_historico["Datetime"])

    # Ordenar los datos por fecha (de más antiguo a más reciente)
    df_historico = df_historico.sort_values(by="Datetime")

    # Obtener las fechas mínima y máxima disponibles
    min_date = df_historico["Datetime"].min().date()
    max_date = df_historico["Datetime"].max().date()

    # Selección de rango de fechas
    st.sidebar.subheader("📅 Selecciona el Rango de Fechas")
    start_date = st.sidebar.date_input("Fecha inicio", min_date, min_value=min_date, max_value=max_date)
    end_date = st.sidebar.date_input("Fecha fin", max_date, min_value=min_date, max_value=max_date)

    # Filtrar el DataFrame según el rango de fechas seleccionado
    df_filtrado = df_historico[
        (df_historico["Datetime"].dt.date >= start_date) & 
        (df_historico["Datetime"].dt.date <= end_date)
    ]

    # Paginación
    st.sidebar.subheader("📄 Paginación")
    page_size = st.sidebar.slider("Tamaño de la página (filas)", min_value=100, max_value=100000, value=1000, step=100)
    total_rows = len(df_filtrado)
    num_pages = (total_rows // page_size) + (1 if total_rows % page_size > 0 else 0)

    if num_pages > 1:
        page_number = st.sidebar.number_input("Número de página", min_value=1, max_value=num_pages, value=1)
    else:
        page_number = 1

    # Calcular el rango de filas para la página actual
    start_row = (page_number - 1) * page_size
    end_row = start_row + page_size
    df_paginated = df_filtrado.iloc[start_row:end_row]

    # Mostrar gráficos
    if not df_paginated.empty:
        st.subheader(f"Histórico de Parámetros para {selected_analizador} ({start_date} a {end_date})")
        st.write(f"Mostrando página {page_number} de {num_pages} ({len(df_paginated)} filas)")

        # Gráfico de Voltaje en Circuito Abierto (Voc)
        fig_voc = px.line(df_paginated, x='Datetime', y='Voc', title='Voltaje en Circuito Abierto (Voc)')
        st.plotly_chart(fig_voc, use_container_width=True)

        # Gráfico de Voce (Variante de Voc)
        if 'Voce' in df_paginated.columns:
            fig_voce = px.line(df_paginated, x='Datetime', y='Voce', title='Voce (Variante de Voc)')
            st.plotly_chart(fig_voce, use_container_width=True)

        # Gráfico de Factor de Forma (FF)
        if 'FF' in df_paginated.columns:
            fig_ff = px.line(df_paginated, x='Datetime', y='FF', title='Factor de Forma (FF)')
            st.plotly_chart(fig_ff, use_container_width=True)

        # Gráfico de Corriente de Cortocircuito (Isc)
        fig_isc = px.line(df_paginated, x='Datetime', y='Isc', title='Corriente de Cortocircuito (Isc)')
        st.plotly_chart(fig_isc, use_container_width=True)

        # Gráfico de Potencia Máxima (Pmax)
        fig_pmax = px.line(df_paginated, x='Datetime', y='Pmax', title='Potencia Máxima (Pmax)')
        st.plotly_chart(fig_pmax, use_container_width=True)

        # Gráfico de Voltaje en el Punto de Máxima Potencia (Vmpp)
        if 'Vmpp' in df_paginated.columns:
            fig_vmpp = px.line(df_paginated, x='Datetime', y='Vmpp', title='Voltaje en el Punto de Máxima Potencia (Vmpp)')
            st.plotly_chart(fig_vmpp, use_container_width=True)

        # Gráfico de Corriente en el Punto de Máxima Potencia (Impp)
        if 'Impp' in df_paginated.columns:
            fig_impp = px.line(df_paginated, x='Datetime', y='Impp', title='Corriente en el Punto de Máxima Potencia (Impp)')
            st.plotly_chart(fig_impp, use_container_width=True)

        # Gráfico de Voltaje Mínimo (Vmin)
        if 'Vmin' in df_paginated.columns:
            fig_vmin = px.line(df_paginated, x='Datetime', y='Vmin', title='Voltaje Mínimo (Vmin)')
            st.plotly_chart(fig_vmin, use_container_width=True)

        # Gráfico de Corriente Mínima (Imin)
        if 'Imin' in df_paginated.columns:
            fig_imin = px.line(df_paginated, x='Datetime', y='Imin', title='Corriente Mínima (Imin)')
            st.plotly_chart(fig_imin, use_container_width=True)

    else:
        st.warning("No hay datos disponibles para el rango de fechas seleccionado.")
else:
    st.warning("No se encontraron datos para el analizador seleccionado.")
# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from scripts.query_executor import QueryExecutor

# # Configuración de la página
# st.set_page_config(page_title="Visualizaciones", page_icon="📈", layout="wide")
# st.title("📈 Visualización de Parámetros de Paneles Solares")

# # Path a las credenciales
# hidden_folder_path = "/home/alejandro/Documentos/workspace/JI/proyectos/credenciales_elektra"
# json_file_name = "credenciales.json"

# # Inicializar el ejecutor de consultas
# query_executor = QueryExecutor(hidden_folder_path, json_file_name)

# # Función para obtener la lista de analizadores disponibles
# @st.cache_data
# def obtener_analizadores():
#     df_analizadores = query_executor.execute_query_from_file("queries/query_analizadores.sql")
#     return df_analizadores["Analizador"].tolist()

# # Obtener la lista de analizadores disponibles
# analizadores = obtener_analizadores()

# # Selección múltiple de analizadores
# selected_analizadores = st.multiselect(
#     "Seleccione uno o más analizadores", 
#     analizadores, 
#     default=analizadores  # Selecciona todos los analizadores por defecto
# )

# # Selección de rango de fechas
# st.sidebar.subheader("📅 Selecciona el Rango de Fechas")
# start_date = st.sidebar.date_input("Fecha inicio", pd.to_datetime("2022-01-01"))
# end_date = st.sidebar.date_input("Fecha fin", pd.to_datetime("2023-01-01"))

# # Cargar datos históricos para los analizadores seleccionados y el rango de fechas
# @st.cache_data
# def cargar_datos_historicos(analizadores, start_date, end_date):
#     dfs = []
#     for analizador in analizadores:
#         params = {
#             'analizador': analizador,
#             'fecha_inicio': start_date.strftime('%Y-%m-%d'),
#             'fecha_fin': end_date.strftime('%Y-%m-%d')
#         }
#         df = query_executor.execute_query_from_file("queries/query_historico.sql", params)
#         dfs.append(df)
#     return pd.concat(dfs, ignore_index=True)

# # Cargar datos
# df_historico = cargar_datos_historicos(selected_analizadores, start_date, end_date)

# # Verificar si hay datos
# if not df_historico.empty:
#     # Convertir la columna 'Datetime' a tipo datetime
#     df_historico["Datetime"] = pd.to_datetime(df_historico["Datetime"])

#     # Ordenar los datos por fecha (de más antiguo a más reciente)
#     df_historico = df_historico.sort_values(by="Datetime")

#     # Verificar que la columna 'Analizador' esté presente
#     if 'Analizador' not in df_historico.columns:
#         st.error("La columna 'Analizador' no está presente en los datos.")
#     else:
#         # Mostrar gráficos
#         st.subheader(f"Histórico de Parámetros para {', '.join(selected_analizadores)} ({start_date} a {end_date})")

#         # Gráfico de Voltaje en Circuito Abierto (Voc)
#         fig_voc = px.line(df_historico, x='Datetime', y='Voc', color='Analizador', title='Voltaje en Circuito Abierto (Voc)')
#         st.plotly_chart(fig_voc, use_container_width=True)

#         # Gráfico de Voce (Variante de Voc)
#         if 'Voce' in df_historico.columns:
#             fig_voce = px.line(df_historico, x='Datetime', y='Voce', color='Analizador', title='Voce (Variante de Voc)')
#             st.plotly_chart(fig_voce, use_container_width=True)

#         # Gráfico de Factor de Forma (FF)
#         if 'FF' in df_historico.columns:
#             fig_ff = px.line(df_historico, x='Datetime', y='FF', color='Analizador', title='Factor de Forma (FF)')
#             st.plotly_chart(fig_ff, use_container_width=True)

#         # Gráfico de Corriente de Cortocircuito (Isc)
#         fig_isc = px.line(df_historico, x='Datetime', y='Isc', color='Analizador', title='Corriente de Cortocircuito (Isc)')
#         st.plotly_chart(fig_isc, use_container_width=True)

#         # Gráfico de Potencia Máxima (Pmax)
#         fig_pmax = px.line(df_historico, x='Datetime', y='Pmax', color='Analizador', title='Potencia Máxima (Pmax)')
#         st.plotly_chart(fig_pmax, use_container_width=True)

#         # Gráfico de Voltaje en el Punto de Máxima Potencia (Vmpp)
#         if 'Vmpp' in df_historico.columns:
#             fig_vmpp = px.line(df_historico, x='Datetime', y='Vmpp', color='Analizador', title='Voltaje en el Punto de Máxima Potencia (Vmpp)')
#             st.plotly_chart(fig_vmpp, use_container_width=True)

#         # Gráfico de Corriente en el Punto de Máxima Potencia (Impp)
#         if 'Impp' in df_historico.columns:
#             fig_impp = px.line(df_historico, x='Datetime', y='Impp', color='Analizador', title='Corriente en el Punto de Máxima Potencia (Impp)')
#             st.plotly_chart(fig_impp, use_container_width=True)

#         # Gráfico de Voltaje Mínimo (Vmin)
#         if 'Vmin' in df_historico.columns:
#             fig_vmin = px.line(df_historico, x='Datetime', y='Vmin', color='Analizador', title='Voltaje Mínimo (Vmin)')
#             st.plotly_chart(fig_vmin, use_container_width=True)

#         # Gráfico de Corriente Mínima (Imin)
#         if 'Imin' in df_historico.columns:
#             fig_imin = px.line(df_historico, x='Datetime', y='Imin', color='Analizador', title='Corriente Mínima (Imin)')
#             st.plotly_chart(fig_imin, use_container_width=True)

# else:
#     st.warning("No se encontraron datos para los analizadores seleccionados.")