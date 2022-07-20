import spacy

def extraer_personas(texto):
    nlp = spacy.load("es_core_news_md")
    doc = nlp(texto)
    personas = []
    for ent in doc.ents:
        if(ent.label_ == "PER" and (ent.text).count(" ") >=1 ): #al menos un espacio
            # print("T1: {} , T2: {}".format(len(ent.text), len(ent.text.replace(".", ""))))
            personas.append(ent.text.strip().replace(".",""))

    return personas