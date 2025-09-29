# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 12:46:34 2025

@author: Denisse Ramirez
"""
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings('ignore')


config = {
    'user': 'root',
    'password': 'root'
    }
conn = mysql.connect(**config)
print('Estado de la conexion:', conn.is_connected())

cursor = conn.cursor()

#CREAR BASE DE DATOS
db_nombre = "clientes"
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_nombre}")

#ejecuta una consulta SQL con pandas y te regresa el resultado como DataFrame.
#Se obtiene un dataframe (dbs) con una fila por base de datos 
dbs = pd.read_sql(sql="SHOW DATABASES", con=conn)

#Revisa que la base de datos esta en ese dataframe y si si, se imprime
if any(dbs.isin([db_nombre])):
   print("Base de datos creada")

#Usar la base de datos 
cursor.execute(f"USE {db_nombre}")
#Definir la estructura de la tabla dentro de la base de datos
tabla_nombre = 'agenda_contactos'
query = f""" 
    CREATE TABLE IF NOT EXISTS {tabla_nombre} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL COMMENT 'Nombre del contacto',
        apellido VARCHAR(50) NOT NULL COMMENT 'Apellido del contacto',
        telefono VARCHAR(25) NOT NULL UNIQUE COMMENT 'Número de teléfono',
        email VARCHAR(100) UNIQUE COMMENT 'Dirección de correo electrónico',
        direccion VARCHAR(255) COMMENT 'Dirección del contacto',
        ciudad VARCHAR(50) COMMENT 'Ciudad de residencia del contacto',
        estado VARCHAR(50) COMMENT 'Estado de residencia del contacto',
        codigo_postal VARCHAR(10) COMMENT 'Código postal',
        fecha_nacimiento DATE COMMENT 'Fecha de nacimiento del cliente',
        fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha de registro del contacto',
        notas TEXT COMMENT 'Notas adicionales',
        foto LONGBLOB COMMENT 'Fotografía del contacto'
        )
"""
#LONGBLOB es para almacenar datos binarios largos como audios, fotos, videos en bases de datos relacionales
cursor.execute(query)

#Verificar
tablas = pd.read_sql_query(sql=f"SHOW TABLES FROM {db_nombre}", con=conn)

if any(dbs.isin([tabla_nombre])):
    print("Tabla creada dentro de la base de datos", db_nombre)


#Ver estructura de la tabla agenda
estructura = pd.read_sql_query(sql='DESCRIBE clientes.agenda_contactos', con=conn)

#Consulta datos existentes
df = pd.read_sql(sql=f'SELECT * FROM {tabla_nombre}', con=conn)
print(df)





