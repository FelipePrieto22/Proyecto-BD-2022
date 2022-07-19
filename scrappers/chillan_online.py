import random
from requests_html import HTMLSession
import time
import mysql.connector as mariadb
import sys
import datetime

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

session = HTMLSession()

## Simular que estamos utilizando un navegador web
USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
headers = {'user-agent':random.choice(USER_AGENT_LIST) }

#Formatear las fechas
def format_date(date):
    fecha = date.split("T")[0]
    fecha_split = fecha.split("-")
    fecha = datetime.date(int(fecha_split[0]), int(fecha_split[1]), int(fecha_split[2]))

    return(fecha)

def formatoTexto(contenido):
    text = "";
    for i in range(0,len(contenido)):
        text += contenido[i] + "\n"
    return text;

def obtenerDatosUrl(url):
    session = HTMLSession()
    response = session.get("{}".format(url), headers = headers)

    xpath_fecha = "//div[@class='tdb-block-inner td-fix-index']/time/@datetime"
    fecha = response.html.xpath(xpath_fecha)
    if(len(fecha) == 0):
        return
    fecha = format_date(fecha[0])

    xpath_titulo = "//div[@class='tdb-block-inner td-fix-index']/h1/text()"
    titulo = response.html.xpath(xpath_titulo)
    if(len(titulo) == 0):
        return
    titulo = titulo[0]

    xpath_contenido = "//div[@class='tdb-block-inner td-fix-index']/p/text()" 
    contenido = response.html.xpath(xpath_contenido)
    texto = formatoTexto(contenido)

    cur.execute("INSERT INTO noticia(url,titulo,contenido,fecha_publicacion,nombre_medio) VALUES('{0}','{1}','{2}','{3}',{4})".format(url,titulo,texto,fecha,nombre_medio)) #insertar datos en BD

nombre_medio = "Chillan online"

def extraerURL():
    print("Medio de prensa: Chillan Online")
    cur.execute("INSERT INTO medio_de_prensa(comuna,region,regional_o_local,idioma,pais,nombre_medio) VALUES('chillan','ñuble','local','español','chile','{0}')".format(nombre_medio))

    ## URL "SEED" que escrapear
    URL_SEED = "https://www.chillanonline.cl/V6/category/region-de-nuble/page/"
    
    ## Analizar ("to parse") el contenido
    xpath_url = "//div[@class='td-module-meta-info']/h3/a/@href"

    for i in range(1,3): #hasta la 27
        response = session.get("{}{}/".format(URL_SEED,i),headers=headers)
        all_urls = response.html.xpath(xpath_url)
        for url in all_urls:
            cur.execute("DELETE FROM noticia WHERE url = '"+url+"'")
            obtenerDatosUrl(url)
        all_urls.clear()
        print("     Noticias de la pagina {} añadidas a la base de datos".format(i))
            
    conn.commit() 
    conn.close()