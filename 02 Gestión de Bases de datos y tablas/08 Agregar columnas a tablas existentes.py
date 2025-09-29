# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 11:06:30 2025

@author: Denisse Ramirez
"""
# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Conexión
conn = mysql.connect(
    user = "root",
    password = "root"
    )
cursor = conn.cursor()


# Base de Datos que usaremos
cursor.execute("USE clientes")

#Obtener la estructura de la tabla 
tabla = 'agenda_contactos'
estructura = pd.read_sql(sql=f'DESCRIBE {tabla}', con=conn)
print(f"Numero de columnas = {estructura.shape[0]}")

#Agregar columna 
query=f'ALTER TABLE clientes.{tabla} ADD COLUMN licenciatura VARCHAR (50) NOT NULL COMMENT "Licenciatura Estudiada"'
cursor.execute(query)

#Verificar 
nueva_estructura = pd.read_sql(sql=f'DESCRIBE {tabla}', con=conn)
print(f"Numero de columnas = {nueva_estructura.shape[0]}")