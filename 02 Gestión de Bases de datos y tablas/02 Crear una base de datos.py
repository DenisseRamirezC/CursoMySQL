# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 15:29:48 2025

author: Denisse
"""
#Importar librerias 
import mysql.connector as mysql

#Establecer conexion 
conn = mysql.connect(
    user='root',
    password='root',
    host='localhost'
    )
print("Estatus de conexion:", conn.is_connected())
#Definir cursor
cursor=conn.cursor()

#Declarar nombre de la base de datos
nombre = "base_datos_prueba"
query = f"CREATE DATABASE {nombre}"
cursor.execute(query)

#Consultar su existencia
cursor.execute("SHOW DATABASES")
dbs = cursor.fetchall()
print(dbs)

try:
    cursor.execute(query)
except Exception as error:
    print("Error al crear la base de datos:", error)
    

query = f"CREATE DATABASE IF NOT EXISTS {nombre}"
cursor.execute(query)
