-- MySQL dump 10.13  Distrib 8.0.26, for macos11 (x86_64)
--
-- Host: localhost    Database: zerobase
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

USE `zerobase`;

--
-- Table structure for table `celeb`
--

DROP TABLE IF EXISTS `celeb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `celeb` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NAME` varchar(32) NOT NULL DEFAULT '',
  `birthday` date DEFAULT NULL,
  `AGE` int DEFAULT NULL,
  `SEX` char(1) DEFAULT NULL,
  `JOB_TITLE` varchar(32) DEFAULT NULL,
  `AGENCY` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `celeb`
--

LOCK TABLES `celeb` WRITE;
/*!40000 ALTER TABLE `celeb` DISABLE KEYS */;
INSERT INTO `celeb` VALUES (1,'아이유','1993-05-16',29,'F','가수, 텔런트','EDAM엔터테이먼트'),(2,'이미주','1994-09-23',28,'F','가수','울림엔터테이먼트'),(3,'송강','1994-04-23',28,'M','텔런트','나무엑터스'),(4,'강동원','1981-01-18',41,'M','영화배우, 텔런트','YG엔터테이먼트'),(5,'유재석','1972-08-14',50,'M','MC, 개그맨','안테나'),(6,'차승원','1970-06-07',48,'M','영화배우, 모델','YG엔터테이먼트'),(7,'이수현','1999-05-04',23,'F','가수','YG엔터테이먼트');
/*!40000 ALTER TABLE `celeb` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `oil_price`
--

DROP TABLE IF EXISTS `oil_price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oil_price` (
  `ID` int DEFAULT NULL,
  `상호` varchar(16) DEFAULT NULL,
  `주소` varchar(255) DEFAULT NULL,
  `가격` int DEFAULT NULL,
  `셀프` char(1) DEFAULT NULL,
  `상표` varchar(16) DEFAULT NULL,
  `구` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oil_price`
--

LOCK TABLES `oil_price` WRITE;
/*!40000 ALTER TABLE `oil_price` DISABLE KEYS */;
INSERT INTO `oil_price` VALUES (1,'타이거주유소','서울 은평구 수색로 188(중산동)',1484,'N','SK에너지','은평구'),(2,'(주)명연에너지','서울 은평구 수색로 236(수색동)',1485,'Y','현대오일뱅크','은평구'),(3,'성락주유소','서울 영등포구 가마산로 414(신길동)',1498,'Y','S-OIL','영등포구'),(4,'(주)MS주유소','서울특별시 영등포구 대림로 230(대림동)',1498,'N','현대오일뱅크','영등포구'),(5,'쌍문주유소','서울특별시 도봉구 도봉로 547(쌍문동)',1509,'Y','S-OIL','도봉구'),(6,'21세기주유소','서울 동작구 시흥대로 616(신대방동)',1598,'Y','SK에너지','동작구'),(7,'살피재주유소','서울 동작구 상도로 334(상도동)',1635,'N','SK에너지','동작구'),(8,'뉴서울(강남)','서울 강남구 언주로 716(논현동)',2160,'N','SK에너지','강남구'),(9,'신길주유소','서울특별시 영등포구 신길로 74(신길동)',1498,'Y','GS칼텍스','영등포구');
/*!40000 ALTER TABLE `oil_price` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `refueling`
--

DROP TABLE IF EXISTS `refueling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `refueling` (
  `ID` int DEFAULT NULL,
  `이름` varchar(32) DEFAULT NULL,
  `주유소` varchar(16) DEFAULT NULL,
  `주유일` date DEFAULT NULL,
  `금액` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `refueling`
--

LOCK TABLES `refueling` WRITE;
/*!40000 ALTER TABLE `refueling` DISABLE KEYS */;
INSERT INTO `refueling` VALUES (1,'유재석','뉴서울(강남)','2021-10-01',50000),(2,'이미주','뉴서울(강남)','2021-10-01',120000),(3,'이효리','제주주유소','2021-10-03',80000),(4,'아이유','타이거주유소','2021-10-03',80000),(5,'유재석','뉴서울(강남)','2021-10-03',60000),(6,'강동원','타이거주유소','2021-10-10',50000),(7,'유재석','쌍문주유소','2021-10-10',60000),(8,'이미주','타이거주유소','2021-10-10',50000),(9,'아이유','뉴서울(강남)','2021-10-14',150000),(10,'아이유','뉴서울(강남)','2021-10-14',120000),(11,'유재석','쌍문주유소','2021-10-14',80000),(12,'유재석','뉴서울(강남)','2021-10-16',110000),(13,'이미주','타이거주유소','2021-10-16',50000),(14,'이효리','제주주유소','2021-10-20',80000),(15,'이상순','제주주유소','2021-10-20',50000),(16,'이상순','타이거주유소','2021-10-20',140000);
/*!40000 ALTER TABLE `refueling` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-13 17:38:21
