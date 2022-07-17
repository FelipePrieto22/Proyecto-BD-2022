#1) SELECT nombre_medio, count(*) FROM medio_de_prensa JOIN noticia ON noticia.nombre_medio = medio_de_prensa.nombre_medio GROUP BY nombre_medio;
#2) SELECT nombre FROM noticia JOIN menciona ON noticia.url = menciona.url WHERE fecha_publicacion = '2022-07-17';
#3) SELECT nombre, fecha, popularidad FROM persona JOIN popularidad ON persona.id_persona = popularidad.id_persona WHERE nombre = "Barack Obama";
#4) SELECT * FROM medio_de_prensa JOIN tiene ON medio_de_prensa.nombre_medio = tiene.nombre_medio WHERE region = "ñuble" ORDER BY fecha_de_adquisicion DESC limit 5;

#añadir al diagrama en la entidad de persona un id_persona que es la clave primaria es mas que nada para simplificar algunas cosas