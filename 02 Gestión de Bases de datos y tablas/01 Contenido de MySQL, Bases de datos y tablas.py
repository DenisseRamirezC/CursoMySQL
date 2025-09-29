# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 14:38:07 2025

author: Denisse Ramirez
"""
#Importar librerias 
import mysql.connector as mysql
import json 

#Realizar conexion 
conn = mysql.connect(
    user='root',
    password='root',
    host='localhost'
    )
print("Estatus de conexion:", conn.is_connected())
#Definir cursor
cursor=conn.cursor()

#Informacion de MySQL
print('Usuario:', conn.user)
print('Version:', conn.get_server_info())
print('Host:', conn.server_host)
print('Puerto:', conn.server_port)

#Consultar base de datos
query = 'SHOW DATABASES'
cursor.execute(query)
dbs=cursor.fetchall()
print('Bases de datos:', dbs)#Imprime todas las bases de datos

#Consultar tablas en cada base
db_muestra = 'world'
query=f'SHOW TABLES FROM {db_muestra}'
cursor.execute(query)
tablas_world = cursor.fetchall()
print('Tablas:', tablas_world)#Imprime las tablas de la base de datos world

#Describir cada tabla 
query='DESCRIBE {base_datos}.{tabla}'.format(base_datos =db_muestra, tabla=tablas_world[0][0])
cursor.execute(query)
contenido_tabla=cursor.fetchall()
print(contenido_tabla)#Imprime la estructura de la primera tabla city

#-----------------------
def obtener_MySQL_info():
    """
    Obtiene la informacion existente dentro de MySQL
    
    Salida:
    Diccionario con informacion de nuestras bases de datos dentro de MySQL
    

    """
    #Almacenar
    db_info = {
        "MySQL":{
            "Server": conn.get_server_info(),
            "Host": conn.server_host,
            "Port": conn.server_port,
            "DBs": {}
                 }
        }
    #Obtener bases de datos
    cursor.execute("SHOW DATABASES")
    for i in cursor:
        db_info["MySQL"]["DBs"][i[0]] = {}
    #Consultar las tablas dentro de cada base
    for i in db_info["MySQL"]["DBs"]:
        query=f"SHOW TABLES FROM {i}"
        cursor.execute(query)
        tablas = cursor.fetchall()
        #Obtener estructura de cada tabla
        for t in tablas:
            cursor.execute(f"DESCRIBE {i}.{t[0]}")
            estructura_tabla = cursor.fetchall()
            db_info["MySQL"]["DBs"][i][t[0]] = estructura_tabla
    return db_info

#Recuperar informacion
mysql_info = obtener_MySQL_info()
print("Informacion de MySQL:", json.dumps(mysql_info, indent=4))


