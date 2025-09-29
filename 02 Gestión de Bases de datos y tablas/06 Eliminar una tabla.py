# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 15:34:37 2025

author: Denisse Ramirez
"""
# Importar librerías
import mysql.connector as mysql


# Definir conexión
conn = mysql.connect(
    user="root",
    password="root",
    host="localhost"
    )
cursor = conn.cursor()

# Establecer la base de datos que se va a usar
cursor.execute("USE clientes")

#Crear tabla pequena porque esa es la que se borrara 
cursor.execute("""
               CREATE TABLE IF NOT EXISTS tabla_eliminacion
               (
                   identificador INT AUTO_INCREMENT PRIMARY KEY,
                   nombre VARCHAR(100) NOT NULL
                   )
               """)
#Verificar existencia
cursor.execute("SHOW TABLES")
print(list(cursor))

#Eliminar tabla
query="DROP TABLE IF EXISTS tabla_eliminacion"
cursor.execute(query)
#Validar que se elimino
cursor.execute("SHOW TABLES")
tablas_existencia = [i[0] for i in cursor]#posicion 0 en la tupla 
if "tabla_elimnacion" not in tablas_existencia:
    print("La tabla se elimino exitosamente")
else:
    raise ValueError("La tabla no se ha eliminado ")
    
    
#Respaldar informacion antes de borrar tabla si se requiere 
#Es importante checar que no existan otras tablas dependientes de la que se ha
#eliminado y que los datos que habían en esa tabla eliminada no afecte a otras 
