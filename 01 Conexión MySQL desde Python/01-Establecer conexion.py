"""
Curso MySQL

Autor: Denisse Ramirez
"""
#importar librerias
import mysql.connector as mysql 
#Establecer parametros de conexion
config = {
    'user': 'root',
    'password': 'root',
    'host': "localhost", #Direccion del host de MySQL, podria ser una direccion ip o el nombre de un host
    'database': None, #nombre de la base a la que te quieres conectar
    'raise_on_warnings': True #Esta configuracion hara que se lancen excepciones en caso de advertencias
    }

#Establecer la conexion
conn = mysql.connect(**config)
print('Conexion exitosa')

#Imprimir informacion de conexion
print('-----Informacion de Conexion----------')
print("Version de MySQL:", conn.get_server_info())
print("ID de la conexion:", conn.connection_id)
print("Servidor Host:", conn.server_host)
print("Puerto del servidor:", conn.server_port)#3306 por default
print("Base de datos:", conn.database)
print("Usuario:", conn.user)
print("Password", conn._password)
print("Conexion Activa:", conn.is_connected())
print("Conexion Cerrada:", conn.is_closed())
print("-"*20 )


#Definir el cursor
cursor = conn.cursor()
#Identificar las bases de datos actuales
cursor.execute("SHOW DATABASES")
#Estraer resultados
for i in cursor: 
    print(i)
    
#Cerrar conexion
conn.close()
#Corroborar que la conexion no sigue activa 
print("Conexion Activa:", conn.is_connected())

#Recordatorio:
    #Se puede establecer la conexion a MySQL desde Python
    #Debemos tener cuidado en todo momento con la posible
    #filtracion de nuestras credenciales