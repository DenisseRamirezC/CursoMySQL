# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 12:12:08 2025

Autor: Denisse Ramirez 
"""

import mysql.connector as mysql

config = {
    'user': 'root',
    'password': 'root',
    'database': None
    }
conn = mysql.connect(**config)
print('Estado de la conexion:', conn.is_connected())

cursor = conn.cursor()

#Seleccionar una base
query = 'SHOW DATABASES'
cursor.execute(query)
dbs = list(cursor)
db_final = dbs[-1][0]

#Metodo 1: Intentar cambiar el parametro interno 
conn.database = db_final
print("Base de datos actual:", conn.database)

#Metodo 2: Mediante consulta
query = f"USE {db_final}"
cursor.execute(query)
print("Base de datos actual:", conn.database)

#Metodo 3: Establecer una nueva conexion, es poco eficiente
config = {
    'user': 'root',
    'password': 'root',
    'database': db_final
    }
conn = mysql.connect(**config)
print("Base de datos actual:", conn.database)


#Cerrar conexion 
conn.close()












