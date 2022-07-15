import spacy

def extraer_personas(texto):
    nlp = spacy.load("es_core_news_md")
    
    doc = nlp(texto)
    personas = []
    for ent in doc.ents:
        if(ent.label_ == "PER" and (ent.text).count(" ") >=1 ): #al menos un espacio
            personas.append(ent.text)

    return personas