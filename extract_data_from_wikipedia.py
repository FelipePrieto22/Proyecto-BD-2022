#pip install python-dateutil 
import mysql.connector as mariadb
import sys
import spacy
import datetime
import wikipedia
from dateutil.parser import parse
wikipedia.set_lang("es")
import pageviewapi
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline


ES_MODEL_LANGUAGE="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"
tokenizer_es_language = AutoTokenizer.from_pretrained(ES_MODEL_LANGUAGE)
model_es_language = AutoModelForQuestionAnswering.from_pretrained(ES_MODEL_LANGUAGE)
q_a_es = pipeline("question-answering", model=model_es_language, tokenizer=tokenizer_es_language)

import warnings
warnings.filterwarnings("ignore")
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

def obtener_info(persona, url_noticia):
    conn.reconnect()
    cur = conn.cursor()
    cur.execute("USE medios_de_prensa") #usar la base de datos

    try:
        print("Agregando nombre <{}> a la base de datos...".format(persona))
        cur.execute("INSERT INTO persona(nombre) VALUES('{0}')".format(persona))
        conn.commit()
        cur.execute("SELECT id_persona FROM persona WHERE nombre = '{0}';".format(persona))
        id_persona = cur.fetchone()[0]
        cur.execute("INSERT INTO menciona(id_persona,url) VALUES('{}','{}')".format(id_persona,url_noticia))
        conn.commit()
         
    except mariadb.IntegrityError:
        print("{} ya fue añadido a la base de Datos".format(persona))
        return
        
    try:
        print("Obteniendo informacion desde wikipedia: {}".format(persona))
        summary = wikipedia.summary(persona, sentences = 1, auto_suggest = False)
    except wikipedia.exceptions.PageError:
        print("Esta persona <{}> no tiene pagina de wikipedia".format(persona))
        return

    except wikipedia.exceptions.DisambiguationError:
        print("El resultado de la busqueda es ambiguo...".format(persona))
        return
    except wikipedia.exceptions.RedirectError:
        print("{} GG!".format(persona))
        return 

    #preguntas
    result = q_a_es(question = "¿En qué año nació el o ella?", context = summary)
    fecha_nacimiento = result["answer"]
    
    fecha_nacimiento = datetime.date(int(fecha_nacimiento.split(" ")[0]), 1, 1)

    result = q_a_es(question = "¿Cuál es su profesión?", context = summary)
    profesion = result["answer"]

    result = q_a_es(question="¿Cuál es su nacionalidad?", context=summary)
    nacionalidad = result["answer"]


    url = wikipedia.page(persona).url
    
    #insertar en base de datos...
    print("Agregando datos a la base de datos...")
    cur.execute("SELECT id_persona FROM persona WHERE nombre = '{0}';".format(persona))
    id_persona = cur.fetchone()[0]
    cur.execute("UPDATE persona SET profesion = '{0}',fecha_de_nacimiento = '{1}',nacionalidad = '{2}',pagina_wikipedia_url = '{3}' WHERE id_persona = '{4}'".format(profesion,fecha_nacimiento,nacionalidad,url,id_persona))

    conn.commit() 

    result = pageviewapi.per_article('es.wikipedia', persona, '20220601', '20220630',
                       access='all-access', agent='all-agents', granularity='daily')

    for item in result.items():
        for article in item[1]:
            views=article['views']
            visitas = str(views)
            fechaP = article['timestamp'] 
            dt = parse(fechaP[:8])
            fecha = dt.strftime('%d-%m-%Y')
            fecha = datetime.date(int(fecha[6:]), int(fecha[3:5]), int(fecha[:2]))
            cur.execute("SELECT id_persona FROM persona WHERE nombre = '{0}';".format(persona))
            id_persona = cur.fetchone()[0]
            cur.execute("INSERT INTO popularidad(fecha,id_persona,visitas) VALUES('{}','{}','{}')".format(fecha,id_persona,visitas))
            

    conn.commit() 
    conn.close()    