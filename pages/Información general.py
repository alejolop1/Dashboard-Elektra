import streamlit as st
import pandas as pd
from scripts.connection_elektra import SSHDatabaseConnection  



st.set_page_config(page_title="Información General", page_icon="📊", layout="wide")

st.title("📊 Visualización de Datos Base de Datos SIU")

# Path a las credenciales
hidden_folder_path = "/home/alejandro/Documentos/workspace/JI/proyectos/credenciales_elektra"  
json_file_name = "credenciales.json" 

# Ruta del archivo SQL
sql_file_path = "queries/query1.sql"

# Crear conexión
conexion = SSHDatabaseConnection(hidden_folder_path, json_file_name)

try:
    # Crear el túnel SSH
    conexion.create_tunnel()
    st.success("Túnel SSH establecido correctamente.")

    # Conectar a la base de datos
    conexion.connect_to_database()
    st.success("Conexión a la base de datos establecida correctamente.")

    # Leer la consulta SQL desde el archivo
    with open(sql_file_path, "r", encoding="utf-8") as file:
        query = file.read()

    # Ejecutar la consulta SQL
    df = pd.read_sql(query, conexion.db_connection)

    # Mostrar los resultados en Streamlit
    st.subheader("Tabla resumen")
    st.dataframe(df) 

    #st.subheader("Estadísticas básicas")
    #st.write(df.describe())

except Exception as e:
    st.error(f"Error: {e}")

finally:
    conexion.close_connections()
    st.success("Conexión a la base de datos y túnel SSH cerrados correctamente.")
