-- MariaDB dump 10.19  Distrib 10.6.7-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: medios_de_prensa
-- ------------------------------------------------------
-- Server version	10.6.7-MariaDB-2ubuntu1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dueño`
--

DROP TABLE IF EXISTS `dueño`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dueño` (
  `es_persona` tinyint(1) DEFAULT NULL,
  `nombre_dueño` varchar(32) NOT NULL,
  PRIMARY KEY (`nombre_dueño`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dueño`
--

LOCK TABLES `dueño` WRITE;
/*!40000 ALTER TABLE `dueño` DISABLE KEYS */;
INSERT INTO `dueño` (`es_persona`, `nombre_dueño`) VALUES (1,'Arnold Schwarzenegger');
/*!40000 ALTER TABLE `dueño` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medio_de_prensa`
--

DROP TABLE IF EXISTS `medio_de_prensa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medio_de_prensa` (
  `nombre_medio` varchar(32) NOT NULL,
  `region` varchar(16) DEFAULT NULL,
  `comuna` varchar(64) DEFAULT NULL,
  `regional_o_local` enum('regional','local') DEFAULT NULL,
  `idioma` varchar(16) DEFAULT NULL,
  `pais` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`nombre_medio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medio_de_prensa`
--

LOCK TABLES `medio_de_prensa` WRITE;
/*!40000 ALTER TABLE `medio_de_prensa` DISABLE KEYS */;
INSERT INTO `medio_de_prensa` (`nombre_medio`, `region`, `comuna`, `regional_o_local`, `idioma`, `pais`) VALUES ('mega','metropolitana','santiago','regional','español','chile');
/*!40000 ALTER TABLE `medio_de_prensa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menciona`
--

DROP TABLE IF EXISTS `menciona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menciona` (
  `id_persona` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(256) NOT NULL,
  PRIMARY KEY (`id_persona`,`url`),
  KEY `url` (`url`),
  CONSTRAINT `menciona_ibfk_1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`),
  CONSTRAINT `menciona_ibfk_2` FOREIGN KEY (`url`) REFERENCES `noticia` (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menciona`
--

LOCK TABLES `menciona` WRITE;
/*!40000 ALTER TABLE `menciona` DISABLE KEYS */;
/*!40000 ALTER TABLE `menciona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `noticia`
--

DROP TABLE IF EXISTS `noticia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `noticia` (
  `url` varchar(256) NOT NULL,
  `nombre_medio` varchar(32) DEFAULT NULL,
  `fecha_publicacion` date DEFAULT NULL,
  `contenido` text DEFAULT NULL,
  `titulo` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`url`),
  KEY `nombre_medio` (`nombre_medio`),
  CONSTRAINT `noticia_ibfk_1` FOREIGN KEY (`nombre_medio`) REFERENCES `medio_de_prensa` (`nombre_medio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `noticia`
--

LOCK TABLES `noticia` WRITE;
/*!40000 ALTER TABLE `noticia` DISABLE KEYS */;
INSERT INTO `noticia` (`url`, `nombre_medio`, `fecha_publicacion`, `contenido`, `titulo`) VALUES ('https://www.meganoticias.cl/nacional/379541-ipc-chile-mayo-2022-inflacion-en-chile-08-06-2022.html','mega','2008-05-22','TEXTO','Inflación acumulada más alta en 28 años: IPC anota alza de 1,2%');
/*!40000 ALTER TABLE `noticia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `persona` (
  `id_persona` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(32) DEFAULT NULL,
  `profesion` varchar(16) DEFAULT NULL,
  `nacionalidad` varchar(16) DEFAULT NULL,
  `fecha_de_nacimiento` date DEFAULT NULL,
  `pagina_wikipedia_url` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id_persona`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` (`id_persona`, `nombre`, `profesion`, `nacionalidad`, `fecha_de_nacimiento`, `pagina_wikipedia_url`) VALUES (1,'hola soy german','youtuber','chilena',NULL,'https://es.wikipedia.org/wiki/Germán_Garmendia#:~:text=Germán%20Alejandro%20Garmendia%20Aranis%20(Copiapó,más%20adelante%20también%20a%20JuegaGerman.');
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `popularidad`
--

DROP TABLE IF EXISTS `popularidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `popularidad` (
  `id_persona` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `visitas` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_persona`,`fecha`),
  CONSTRAINT `popularidad_ibfk_1` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id_persona`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `popularidad`
--

LOCK TABLES `popularidad` WRITE;
/*!40000 ALTER TABLE `popularidad` DISABLE KEYS */;
INSERT INTO `popularidad` (`id_persona`, `fecha`, `visitas`) VALUES (1,'2010-05-22',300000000);
/*!40000 ALTER TABLE `popularidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tiene`
--

DROP TABLE IF EXISTS `tiene`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tiene` (
  `nombre_dueño` varchar(32) DEFAULT NULL,
  `nombre_medio` varchar(32) NOT NULL,
  `fecha_de_adquisicion` date NOT NULL,
  PRIMARY KEY (`fecha_de_adquisicion`,`nombre_medio`),
  KEY `nombre_dueño` (`nombre_dueño`),
  KEY `nombre_medio` (`nombre_medio`),
  CONSTRAINT `tiene_ibfk_1` FOREIGN KEY (`nombre_dueño`) REFERENCES `dueño` (`nombre_dueño`),
  CONSTRAINT `tiene_ibfk_2` FOREIGN KEY (`nombre_medio`) REFERENCES `medio_de_prensa` (`nombre_medio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tiene`
--

LOCK TABLES `tiene` WRITE;
/*!40000 ALTER TABLE `tiene` DISABLE KEYS */;
INSERT INTO `tiene` (`nombre_dueño`, `nombre_medio`, `fecha_de_adquisicion`) VALUES ('Arnold Schwarzenegger','mega','2010-01-10');
/*!40000 ALTER TABLE `tiene` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-19 16:29:45
