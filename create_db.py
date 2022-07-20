import mysql.connector as mariadb
import sys

def createDB():
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

    registro = cur.fetchall() #Para si existe la base de datos
    if registro:             #Condicion si existe algo o no, si exite algo 
        print("La base de datos ya existe")
        # Create Database
        cur.execute("DROP DATABASE medios_de_prensa") #eliminar base de datos creada anteriormente
        print("Borrando base de datos existente...")
        query_create = "CREATE DATABASE medios_de_prensa" # comando para crear la base de datos
        cur.execute(query_create) # crear la base de datos
        print("Nueva base de datos creada exitosamente")
    else:     
        print("La base de datos no existe")
        # Create Database
        query_create = "CREATE DATABASE medios_de_prensa" # comando para crear la base de datos
        cur.execute(query_create) # crear la base de datos
        print("Base de datos creada exitosamente")


    cur.execute("USE medios_de_prensa") #usar la base de datos

    #Tabla medio de prensa
    cur.execute("CREATE TABLE medio_de_prensa(nombre_medio VARCHAR(32) NOT NULL, region VARCHAR(16), comuna VARCHAR(64), regional_o_local ENUM ('regional','local'), idioma VARCHAR(16), pais VARCHAR(16), PRIMARY KEY(nombre_medio))")

    #Tabla dueño
    cur.execute("CREATE TABLE dueño(es_persona BOOL, nombre_dueño VARCHAR(32), PRIMARY KEY(nombre_dueño))")

    #Tabla tiene
    cur.execute("CREATE TABLE tiene(nombre_dueño VARCHAR(32), nombre_medio VARCHAR(32) NOT NULL, fecha_de_adquisicion DATE, FOREIGN KEY(nombre_dueño) REFERENCES dueño(nombre_dueño), FOREIGN KEY(nombre_medio) REFERENCES medio_de_prensa(nombre_medio), PRIMARY KEY(fecha_de_adquisicion,nombre_medio))")
    
    #Table noticia
    cur.execute("CREATE TABLE noticia(url VARCHAR(256),nombre_medio VARCHAR(32), fecha_publicacion DATE, contenido TEXT, titulo VARCHAR(256), PRIMARY KEY(url), FOREIGN KEY(nombre_medio) REFERENCES medio_de_prensa(nombre_medio))")

    #Tabla persona
    cur.execute("CREATE TABLE persona(id_persona INT AUTO_INCREMENT, nombre VARCHAR(256) UNIQUE, profesion VARCHAR(256), nacionalidad VARCHAR(16), fecha_de_nacimiento DATE, pagina_wikipedia_url VARCHAR(256), PRIMARY KEY(id_persona))")

    #Tabla menciona
    cur.execute("CREATE TABLE menciona(id_persona INT AUTO_INCREMENT, url VARCHAR(256),FOREIGN KEY(id_persona) REFERENCES persona(id_persona),FOREIGN KEY(url) REFERENCES noticia(url) ,PRIMARY KEY(id_persona,url))")

    #Tabla popularidad
    cur.execute("CREATE TABLE popularidad(id_persona INT AUTO_INCREMENT, fecha DATE, visitas INT, FOREIGN KEY(id_persona) REFERENCES persona(id_persona), PRIMARY KEY(id_persona,fecha))")

    conn.commit() 
    conn.close()