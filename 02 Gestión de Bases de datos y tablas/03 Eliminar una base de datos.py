# -*- coding: utf-8 -*-
"""
3 de septiembre de 2025, 11:53 am 
Autor: Denisse Ramirez 
"""
import mysql.connector as mysql
import time 

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': 3306,
    'database': None,
    }
conn = mysql.connect(**config)
print('Estado de la conexion:', conn.is_connected())

cursor = conn.cursor()

db_nombre = "base_datos_prueba"
query = f'CREATE DATABASE IF NOT EXISTS {db_nombre}' 
cursor.execute("SHOW DATABASES")
print("Bases de datos:", list(cursor))

#Eliminar base de datos
print("Cuidado, estas por eliminar una base de datos. Tienes 10 segundos para detener el proceso")
time.sleep(10)
query=f'DROP DATABASE {db_nombre}'
cursor.execute(query)
print("La Base de datos ha sido eliminada")

#Verificar que ya no existe 
cursor.execute("SHOW DATABASES")
print("Bases de datos:", list(cursor))

#Eliminar por segunda ocasion nuestra base de datos 
#Si se intenta eliminar una base que no existe o que ya se borro 
try:
    query = f'DROP DATABASE {db_nombre}'
    cursor.execute(query)
except Exception as error:
    print("Error", error)
    
query = "DROP DATABASE IF EXISTS {db_nombre}"
cursor.execute(query)

#Eliminar una base de datos es una accion irreversible 
#No tendremos privilegios de administrador pero debemos tener cuidado
#porque danariamos la totalidad de los datos








