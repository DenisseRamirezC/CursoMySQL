# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 10:58:57 2025
author: Denisse Ramirez
"""
#Importar librerias 
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

#Definir funciones 
def establecer_conexion(usuario: str, contrasena: str, host: str, base_datos: str, puerto: int=3306):
   """
    

    Parameters
    ----------
    usuario : str
        Nombre del usuario de MySQL.
    password : str
        Contrasena de MySQL.
    host : str
        Direccion del host
    base_datos : str
        Base de datos a la que queremos conectas
    puerto : int, optional
        The default is 3306.

    Returns
    -------
    None.

    """
    #Establecer los parametros
   config = {
        "user": usuario,
        "password": contrasena,
        "host": host,
        "database": base_datos,
        "port": puerto
        }
   
   #Establecer conexion
   conn = mysql.connect(**config)
   return conn

#Conexion
conn = establecer_conexion(usuario='root', contrasena='root', host='localhost', base_datos=None)
print("Estatus de la conexion:", conn.is_connected())

#Cursor
cursor=conn.cursor()    

def ejecutar_consulta(consulta: str):
    """
    Ejecutar una consulta en la base de datos
    Args:
        consulta (str): Consulta SQL a ejecutar
    Salida: 
        Cursor que contiene los resultados de la consulta
    """
    #Ejecutar 
    cursor.execute(consulta)
    return cursor 

#Distintas consultas
query = "SHOW DATABASES"
db_existentes = ejecutar_consulta(query)
for n, i in enumerate(db_existentes): #n es el numero e i el nombre de la base de datos
    print(f"Base de datos No. {n}: {i[0]}")

#Realizar consulta con pandas
db_existentes_pd = pd.read_sql(sql=query, con=conn)
print (db_existentes_pd)

#Usar una base de datos
db_usar = db_existentes_pd.iloc[-1,0] #tomar la ultima posicion y extraer la cadena de texto
ejecutar_consulta(f'USE {db_usar}')
print("Trabajando con la base de datos:", conn.database)

#Realizar con pandas
try: 
    pd.read_sql_query(sql=f"USE {db_usar}" , con=conn)
except Exception as error: 
    print("No se pudo ejecutar con error:", error)#pandas solo se puede utilizar cuando nuestra consulta devuelva algo en lo que podemos iterar o extraer valores

#Recordatorio:
    #El resultado de nuestra consulta esta almacenado dentro del mismo cursor, debemos extraer
    #dicho contenido para poder trabajar con la informacion. 
