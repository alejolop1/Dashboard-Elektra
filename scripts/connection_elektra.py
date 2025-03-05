import os
import json
import logging
from sshtunnel import SSHTunnelForwarder
import pymysql
import pandas as pd

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SSHDatabaseConnection:
    
    """
    Una clase para manejar la conexión a un servidor MySQL a través de un túnel SSH.

    Métodos:
        load_credentials():
            Carga las credenciales del archivo JSON.
        
        create_tunnel():
            Establece un túnel SSH utilizando las credenciales cargadas.
        
        connect_to_server(database_name=None):
            Conecta al servidor MySQL.
        
        close_connections():
            Cierra la conexión con la base de datos y el túnel SSH.
    
    Atributos:
        hidden_folder_path (str): Ruta a la carpeta donde se encuentra el archivo JSON con las credenciales.
        json_file_name (str): Nombre del archivo JSON que contiene las credenciales.
        credentials (dict): Diccionario con las credenciales cargadas.
        tunnel (SSHTunnelForwarder): Objeto que representa el túnel SSH.
        db_connection (pymysql.Connection): Conexión a la base de datos MySQL.
    """
    def __init__(self, hidden_folder_path, json_file_name, direct_conection = False):
        self.direct_conection = direct_conection
        self.hidden_folder_path = hidden_folder_path
        self.json_file_name = json_file_name
        self.credentials = self.load_credentials()
        self.tunnel = None
        self.db_connection = None
        

    def load_credentials(self):
        """Carga las credenciales del archivo JSON."""
            
        try:
            json_path = os.path.join(self.hidden_folder_path, self.json_file_name)
            with open(json_path, 'r') as json_file:
                credentials = json.load(json_file)
            logging.info("Credenciales cargadas correctamente.")
            return credentials
        except Exception as e:
            logging.error(f"Error leyendo el archivo JSON: {e}")
            return None
    

    def create_tunnel(self):
        """Establece un túnel SSH utilizando las credenciales cargadas."""
        
        if not self.direct_conection:
            try:
                if 'ssh_remote_bind_address' not in self.credentials:
                    raise KeyError("Falta la clave 'ssh_remote_bind_address' en las credenciales.")
                
                self.tunnel = SSHTunnelForwarder(
                    (self.credentials['ssh_ip_address'], self.credentials['ssh_port']),
                    ssh_username=self.credentials['ssh_p_username'],
                    ssh_password=self.credentials['ssh_password'],
                    remote_bind_address=(self.credentials['dbr_server_ip'], self.credentials['dbr_server_port'])
                )
                self.tunnel.start()
                logging.info("Túnel SSH creado exitosamente.")
            except Exception as e:
                logging.error(f"Error al crear el túnel SSH: {e}")
        else:
            try:
                if 'ssh_remote_bind_address' not in self.credentials:
                    raise KeyError("Falta la clave 'ssh_remote_bind_address' en las credenciales.")
                
                self.tunnel = SSHTunnelForwarder(
                    (self.credentials['ssh_ip_direct'], self.credentials['ssh_port']),
                    ssh_username=self.credentials['ssh_p_username'],
                    ssh_password=self.credentials['ssh_password'],
                    remote_bind_address=(self.credentials['dbr_server_ip'], self.credentials['dbr_server_port'])
                )
                self.tunnel.start()
                logging.info("Túnel SSH creado exitosamente.")
            except Exception as e:
                logging.error(f"Error al crear el túnel SSH: {e}")

    def connect_to_database(self, database_name=None):
        """Conecta al servidor MySQL."""
        try:
            if not self.tunnel:
                raise ConnectionError("El túnel SSH no se ha creado correctamente.")
            
            self.db_connection = pymysql.connect(
                host='localhost',
                user=self.credentials['dbr_user'],
                password=self.credentials['dbr_user_password'],
                port=self.tunnel.local_bind_port,
                database=self.credentials["dbr_name"]
            )
            logging.info("Conexión al servidor MySQL exitosa.")
        except Exception as e:
            logging.error(f"Error al conectar al servidor MySQL: {e}")

    def close_connections(self):
        """Cierra la conexión con la base de datos y el túnel SSH."""
        if self.db_connection:
            self.db_connection.close()
            logging.info("Conexión al servidor MySQL cerrada.")
        if self.tunnel:
            self.tunnel.stop()
            logging.info("Túnel SSH cerrado.")