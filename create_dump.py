import os #modulo para interactuar con el sistema operativo 

user = "root"
password = "root"
host = "localhost"
database = "medios_de_prensa"
filename = "respaldo_base_datos"

os.popen("mysqldump -u%s -p%s -h %s -e --opt -c %s  > %s.sql" % (user, password, host, database, filename))
