""" import mariadb """
import mysql.connector as mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute("SHOW DATABASES like 'medios_de_prensa'")

registro=cur.fetchall()
if registro:             #Condicion si existe algo o no, si exite algo 
    print("Existe la base de datos")
    # Create Database
    cur.execute("DROP DATABASE medios_de_prensa") #eliminar base de datos creada anteriormente
    print("Borrando base de datos existente...")
    query_create = "CREATE DATABASE medios_de_prensa" # comando para crear la base de datos
    cur.execute(query_create) # crear la base de datos
    print("Nueva base de datos creada exitosamente...")

else:     
    print("No existe la base de datos")
    # Create Database
    query_create = "CREATE DATABASE medios_de_prensa" # comando para crear la base de datos
    cur.execute(query_create) # crear la base de datos
    print("Base de datos creada exitosamente...")

cur.execute("USE medios_de_prensa") #usar la base de datos

#Tabla medio de prensa
cur.execute("CREATE TABLE medio_de_prensa(nombre_medio VARCHAR(32) NOT NULL, region VARCHAR(16), comuna VARCHAR(64), regional_o_local ENUM ('regional','local'), idioma VARCHAR(16), pais VARCHAR(16), PRIMARY KEY(nombre_medio))")

#Table noticia
cur.execute("CREATE TABLE noticia(url VARCHAR(256), fecha_publicacion DATE, contenido TEXT, titulo VARCHAR(128), PRIMARY KEY(url))")

#Tabla dueño
cur.execute("CREATE TABLE dueño(es_persona BOOL, nombre_dueño VARCHAR(32), PRIMARY KEY(nombre_dueño))")

#Tabla persona
cur.execute("CREATE TABLE persona(id_persona INT, nombre VARCHAR(32), profesion VARCHAR(16), nacionalidad VARCHAR(16), fecha_de_nacimiento DATE, pagina_wikipedia_url VARCHAR(256), PRIMARY KEY(id_persona))")

#Tabla popularidad
cur.execute("CREATE TABLE popularidad(id_persona INT, fecha DATE, visitas INT, FOREIGN KEY(id_persona) REFERENCES persona(id_persona))")

#Tabla tiene
cur.execute("CREATE TABLE tiene(nombre_dueño VARCHAR(32), nombre_medio VARCHAR(32) NOT NULL, si_o_no BOOL, fecha_de_adquisicion DATE, FOREIGN KEY(nombre_dueño) REFERENCES dueño(nombre_dueño), FOREIGN KEY(nombre_medio) REFERENCES medio_de_prensa(nombre_medio))")

conn.commit() 
conn.close()