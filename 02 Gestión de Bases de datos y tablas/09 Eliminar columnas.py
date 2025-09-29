# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 11:19:29 2025

@author: Denisse Ramirez
"""
# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")


# Establecer conexión
conn = mysql.connect(user="root", password="root", host="localhost", port=3306)
print("Estatus de la conexión:", conn.is_connected())
print("Base de datos:", conn.database)
# Cursor
cursor = conn.cursor()

# Definir la consulta
db = "clientes"
tabla = "agenda_contactos"
columna = "licenciatura"
query = f"ALTER TABLE {db}.{tabla} DROP COLUMN {columna}"#direccion de busqueda

#Verificar estructura
estructura = pd.read_sql(f'DESCRIBE {db}.{tabla}', con=conn)
print("Numero de columnas de la tabla:", estructura.shape[0])#la posicion 0 son las columnas 

#Ejecutar consulta
cursor.execute(query)

#Verificar estructura
estructura = pd.read_sql(f'DESCRIBE {db}.{tabla}', con=conn)
print("Numero de columnas de la tabla:", estructura.shape[0])#la posicion 0 son las columnas 

#Intentar eliminar nuevamente
try:
    cursor.execute(query)
except Exception as error:
    print(error)

#Validar existencia
query=f'SHOW COLUMNS FROM {db}.{tabla}'
columnas = pd.read_sql(sql=query, con=conn)
print(columnas)
#Si la columna existe, borrala, si no, di que ya ha sido borrada 
if columna in columnas['Field']:#Field es la columna del Dataframe donde estan los nombres de las columnas:nombre,apellido,foto,etc
    query = f'ALTER TABLA {db}.{tabla} DROP COLUMN {columna}'
    cursor.execute(query)
else:
    print('La columna ya ha sido eliminada')    
