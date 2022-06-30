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

cur.execute("USE medios_de_prensa") #usar la base de datos

#Añadir a tabla medio de prensa
cur.execute("DELETE FROM medio_de_prensa WHERE nombre_medio = 'mega'")
cur.execute("INSERT INTO medio_de_prensa(nombre_medio, region,comuna, regional_o_local, idioma,pais) VALUES('mega','metropolitana','santiago',1,'español','chile')")

#Añadir a tabla noticia
cur.execute("DELETE FROM noticia WHERE url = 'https://www.meganoticias.cl/nacional/379541-ipc-chile-mayo-2022-inflacion-en-chile-08-06-2022.html'")
cur.execute("INSERT INTO noticia(url,fecha_Publicación,contenido,titulo) VALUES('https://www.meganoticias.cl/nacional/379541-ipc-chile-mayo-2022-inflacion-en-chile-08-06-2022.html','08-05-22','TEXTO','Inflación acumulada más alta en 28 años: IPC anota alza de 1,2%')")

#Añadir a tabla dueño
cur.execute("DELETE FROM dueño WHERE nombre_dueño ='Arnold Schwarzenegger'")
cur.execute("INSERT INTO dueño(es_persona,nombre_dueño) VALUES(TRUE,'Arnold Schwarzenegger')")

#Añadir a tabla persona
cur.execute("DELETE FROM persona WHERE nombre = 'hola soy german'")
cur.execute("INSERT INTO persona(nombre,profesion,nacionalidad,pagina_wikipedia_url) VALUES('hola soy german', 'youtuber','chilena','https://es.wikipedia.org/wiki/Germán_Garmendia#:~:text=Germán%20Alejandro%20Garmendia%20Aranis%20(Copiapó,más%20adelante%20también%20a%20JuegaGerman.')")

#Añadir a tabla popularidad
cur.execute("DELETE FROM popularidad WHERE fecha = '10-05-22'")
cur.execute("INSERT INTO popularidad(fecha,visitas) VALUES('10-05-22',300000000)")

#Añadir a tabla tiene
cur.execute("DELETE FROM tiene WHERE nombre_dueño = 'Arnold Schwarzenegger'")
cur.execute("INSERT INTO tiene(nombre_dueño, nombre_medio, si_o_no, fecha_de_adquisicion) VALUES('Arnold Schwarzenegger','mega',1,'10-01-10')")

conn.commit() 
conn.close()