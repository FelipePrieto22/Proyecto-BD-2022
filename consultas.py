#1) SELECT m.nombre_medio, count(*) FROM medio_de_prensa m 
#   JOIN noticia ON m.nombre_medio = noticia.nombre_medio GROUP BY nombre_medio;
#2) SELECT nombre,fecha_publicacion FROM noticia JOIN menciona ON noticia.url = menciona.url 
#   JOIN persona ON persona.id_persona=menciona.id_persona WHERE fecha_publicacion = "2022-07-19";
#3) SELECT nombre, fecha, visitas FROM persona JOIN popularidad ON persona.id_persona = popularidad.id_persona WHERE nombre = "Miguel Hernández";
#4) SELECT * FROM medio_de_prensa JOIN tiene ON medio_de_prensa.nombre_medio = tiene.nombre_medio 
#   WHERE region = "metropolitana" ORDER BY fecha_de_adquisicion DESC limit 5;
