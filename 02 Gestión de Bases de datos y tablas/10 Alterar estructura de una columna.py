# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 11:37:10 2025

Author: Denisse Ramirez
    """
# Importar librerías
import mysql.connector as mysql
import pandas as pd
from warnings import filterwarnings
filterwarnings("ignore")

# Definir conexión
conn = mysql.connect(user="root", password="root", database="clientes")
cursor = conn.cursor()

# Consultar estructura actual
query = "DESCRIBE agenda_contactos"
estructura_actual = pd.read_sql_query(sql=query, con=conn)

# Modificar la columna de "nombre"
columna = "nombre"
tabla = "agenda_contactos"
nueva_estructura_col = "VARCHAR(100) NOT NULL COMMENT 'Nombre del Contacto'"
query= f'ALTER TABLE {tabla} MODIFY COLUMN {columna} {nueva_estructura_col}'
cursor.execute(query)

#Validar nueva estructura
query = "DESCRIBE agenda_contactos"
nueva_estructura_actual = pd.read_sql_query(sql=query, con=conn)

