"""
Created on Tue Sep  2 12:41:51 2025

author: Denisse Ramirez
"""

#Importar librerias
import mysql.connector as mysql
import pandas as pd 
from warnings import filterwarnings
filterwarnings("ignore")

#Establecer los parametros
config = {
     "user": "root",
     "password": "root",
     "host": "localhost",
     "database": "world",
     "port": 3306
     }
#Conexion 
conn = mysql.connect(**config)
print('Estatus de conexion:', conn.is_connected())
#Definir cursor
cursor=conn.cursor()

#Mostrar tablas

#Extraccion 1: iterar sobre los resultados
cursor.execute("SHOW TABLES")#muestra las tablas que tiene una base de datos
for i in cursor: 
    print(f"Tabla: {i[0]}")

#Extraccion 2: extraer consulta en una lista
cursor.execute("SHOW TABLES")
tablas = list(cursor)
print(tablas)

#Extraccion 3: metodo fetchall del cursor
cursor.execute("SHOW TABLES")
tablas_fetchall = cursor.fetchall()
print(tablas_fetchall)

#Extraccion 4: usando pandas
tablas_pd = pd.read_sql_query(sql="SHOW TABLES", con=conn)
print(tablas_pd)

#SHOW TABLES es un comando SQL propio de MySQL (no de Python).
#Pertenece a la familia de sentencias SHOW que MySQL implementa para mostrar información del servidor, bases de datos, tablas o configuraciones.

