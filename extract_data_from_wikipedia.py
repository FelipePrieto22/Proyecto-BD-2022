import wikipedia
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

def obtener_info(persona):
    cur = conn.cursor(buffered=True)
    cur.execute("USE medios_de_prensa") #usar la base de datos

    profesion = "asdasd"
    fecha_nacimiento = '10-05-22'
    nacionalidad = "asdasd"
    url = "asd"
    
    #insertar en base de datos...
    cur.execute("INSERT INTO persona(nombre,profesion,fecha_de_nacimiento,nacionalidad,pagina_wikipedia_url) VALUES('{0}','{1}','{2}','{3}','{4}')".format(persona,profesion,fecha_nacimiento,nacionalidad,url))
    conn.commit() 

    fechaP = '10-05-22' #fecha de consulta de la popularidad
    visitas = 12312 
    cur.execute("SELECT id_persona FROM persona WHERE nombre = '{0}';".format(persona))
    id_persona = cur.fetchone()[0]
    cur.execute("INSERT INTO popularidad(fecha,id_persona,visitas) VALUES('{}','{}','{}')".format(fechaP,id_persona,visitas))

    conn.commit() 
    conn.close()
