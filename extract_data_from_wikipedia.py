import wikipedia


def obtener_info(persona):
    wikipedia.set_lang("es")
    
    print(wikipedia.summary(persona, sentences=10))

    profesion = ""
    fecha_nacimiento = ""
    popularidad = ""
    rango_fechas_pop = ""
    lista_datos = [profesion,fecha_nacimiento,popularidad,rango_fechas_pop]



    return lista_datos
