import create_db as cdb
import insert_manual as im
import scrappers.chillan_online as mdp1 # medio de prensa(mdp)
import scrappers.la_discusion as mdp2
import scrappers.radio_ñuble as mdp3 
import create_dump as cd
import insert_auto as ia

#instalar:
#   pip install python-dateutil 

def main():
    cdb.createDB() # crea la base de datos localmente y en caso de exisitir la elimina y la crea de nuevo

    print("\nInsertando datos de forma manual...")
    im.insertarDatos() #inserta datos manualmente
    print("Datos manuales insertados correctamente")

    print("\nInsertando datos con scrappers...")
    mdp1.extraerURL()
    """ mdp2.extraerURL()
    mdp3.extraerURL() """
    print("Datos insertados correctamente")

    print("Insertando datos de forma automatica...")
    ia.insertarAuto()
    print("Datos insertados de forma correcta")

    print("\nGuardando una copia de seguridad de la base de datos...")
    cd.createDump()
    print("Respaldo de la base de datos creado correctamente")

main()