# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 12:43:08 2025

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

#Metodo 1: Intentar cambiar el parametro interno 
conn.database = dbs[-1][0]
print("Base de datos actual:", conn.database)

#Metodo 2: Mediante consulta
query = f"USE {dbs[-2][0]}"
cursor.execute(query)
print("Base de datos actual:", conn.database)

#Metodo 3: Establecer una nueva conexion, es poco eficiente
config = {
    'user': 'root',
    'password': 'root',
    'database': dbs[-3][0]
    }
conn = mysql.connect(**config)
print("Base de datos actual:", conn.database)


#Cerrar conexion 
conn.close()

#Recordatorio: el cambio entre base de datos es posible
#y nos permite trabajar con multiples bases

