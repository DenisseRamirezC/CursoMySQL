# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 15:57:38 2025

@author: Denisse Ramirez
"""
# Importar librerías
import mysql.connector as mysql

# Definir la conexión
conn = mysql.connect(
    user="root",
    password="root",
    host="localhost"
    )

print("Estatus:", conn.is_connected())

# Definir cursor
cursor = conn.cursor()
db='clientes'
#Definir base de datos
cursor.execute(f"USE {db}")

#Modificar nombre
viejo = "agenda_contactos"
nuevo = "contactos"
query = f"ALTER TABLE {viejo} RENAME TO {nuevo}"
cursor.execute(query)

#Verificar
cursor.execute("SHOW TABLES")
print(list(cursor))

#Regresar nombre
query = f"ALTER TABLE {nuevo} RENAME TO {viejo}"
cursor.execute(query)
#Verificar
cursor.execute("SHOW TABLES")
print(list(cursor))
