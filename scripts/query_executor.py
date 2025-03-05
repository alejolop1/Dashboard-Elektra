import pandas as pd
from scripts.connection_elektra import SSHDatabaseConnection

class QueryExecutor:
    def __init__(self, hidden_folder_path, json_file_name):
        """
        Clase para ejecutar consultas SQL y devolver resultados en un DataFrame.
        
        Parámetros:
            hidden_folder_path (str): Ruta a la carpeta que contiene las credenciales.
            json_file_name (str): Nombre del archivo JSON con las credenciales.
        """
        self.hidden_folder_path = hidden_folder_path
        self.json_file_name = json_file_name

    def execute_query(self, sql_file_path):
        """
        Ejecuta una consulta SQL desde un archivo y devuelve un DataFrame con los resultados.

        Parámetros:
            sql_file_path (str): Ruta del archivo SQL que contiene la consulta.

        Retorna:
            pd.DataFrame: DataFrame con los resultados de la consulta.
        """
        conexion = SSHDatabaseConnection(self.hidden_folder_path, self.json_file_name)

        try:
            # Crear túnel y conectar a la base de datos
            conexion.create_tunnel()
            conexion.connect_to_database()

            # Leer la consulta SQL
            with open(sql_file_path, "r", encoding="utf-8") as file:
                query = file.read()

            # Ejecutar consulta y convertir en DataFrame
            df = pd.read_sql(query, conexion.db_connection)

            return df  # Retorna el DataFrame con los datos

        except Exception as e:
            print(f"Error ejecutando la consulta: {e}")
            return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

        finally:
            conexion.close_connections()
