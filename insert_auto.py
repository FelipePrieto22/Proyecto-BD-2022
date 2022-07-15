import extract_persons as ep
import extract_data_from_wikipedia as edw
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

cur.execute("SELECT contenido FROM noticia limit 3;")
for row in cur.fetchall(): #todos: fetchall , el primero fetchone
    lista_personas = ep.extraer_personas(row[0])
    for persona in lista_personas:
        print(persona)
        informacion_persona = edw.obtener_info(persona)
        #insertar en base de datos...
        print(informacion_persona)
