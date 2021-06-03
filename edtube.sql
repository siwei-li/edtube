-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: edtube0
-- ------------------------------------------------------
-- Server version	5.7.29-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add profile',7,'add_profile'),(26,'Can change profile',7,'change_profile'),(27,'Can delete profile',7,'delete_profile'),(28,'Can view profile',7,'view_profile'),(29,'Can add video',8,'add_video'),(30,'Can change video',8,'change_video'),(31,'Can delete video',8,'delete_video'),(32,'Can view video',8,'view_video'),(33,'Can add comment',9,'add_comment'),(34,'Can change comment',9,'change_comment'),(35,'Can delete comment',9,'delete_comment'),(36,'Can view comment',9,'view_comment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (2,'',NULL,0,'auth0.5fe2cffe08284b006bb4ff09','','','',0,1,'2020-12-27 12:55:56.022235'),(3,'',NULL,0,'auth0.5ff72e9d54ea200069c886d9','','','',0,1,'2021-01-07 15:55:22.725633'),(4,'pbkdf2_sha256$216000$oLzSh9PV5E8t$IjbmWNxmmacHyqu1gm/Usa6gPuuYU83owWKE8SA2MJ8=','2021-06-03 02:33:14.538511',1,'sylvi','','','superuser@a.com',1,1,'2021-03-08 12:21:58.804178'),(5,'',NULL,0,'jG0FfwqhKeFQQwKpHD0LyTZX4bc2UJX5@clients','','','',0,1,'2021-04-20 04:33:39.377420');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `likes` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `user_id_id` int(11) DEFAULT NULL,
  `video_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comment_comment_parent_id_b612524c_fk_comment_comment_id` (`parent_id`),
  KEY `comment_comment_video_id_id_d81745cd_fk_videos_id` (`video_id_id`),
  KEY `comment_comment_user_id_id_c36a737d_fk_auth_user_id` (`user_id_id`),
  CONSTRAINT `comment_comment_parent_id_b612524c_fk_comment_comment_id` FOREIGN KEY (`parent_id`) REFERENCES `comments` (`id`),
  CONSTRAINT `comment_comment_user_id_id_c36a737d_fk_auth_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `comment_comment_video_id_id_d81745cd_fk_videos_id` FOREIGN KEY (`video_id_id`) REFERENCES `videos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (4,'oh v6',0,'2021-05-05 12:01:24.323736',NULL,2,6),(5,'v6-rep',0,'2021-05-05 12:01:40.049904',4,5,6),(6,'v5',0,'2021-05-05 12:02:03.790855',NULL,3,5);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-03-08 12:26:43.362668','3','Profile of user admin',1,'[{\"added\": {}}]',7,4),(2,'2021-03-08 12:27:06.322720','4','Profile of user auth0.5fe2cffe08284b006bb4ff09',1,'[{\"added\": {}}]',7,4),(3,'2021-03-08 12:27:39.834381','1','admin',3,'',4,4),(4,'2021-03-08 12:32:56.098833','2','Video 2@YT#fwQci1cRiFU',1,'[{\"added\": {}}]',8,4),(5,'2021-05-05 09:20:36.465356','1','Comment object (1)',1,'[{\"added\": {}}]',9,4),(6,'2021-05-05 09:21:03.052989','2','Comment object (2)',1,'[{\"added\": {}}]',9,4),(7,'2021-05-05 11:45:11.655269','3','Comment 3 on Video 5@YT#l5XJdHfPc5o: for video 5',1,'[{\"added\": {}}]',9,4),(8,'2021-05-05 11:54:42.388270','1','Comment 1 on Video 6@YT#DivuT0HpazQ: Testing.',3,'',9,4),(9,'2021-05-05 11:54:42.396147','2','Comment 2 on Video 6@YT#DivuT0HpazQ: Oh',3,'',9,4),(10,'2021-05-05 11:54:42.412149','3','Comment 3 on Video 5@YT#l5XJdHfPc5o: for video 5',3,'',9,4),(11,'2021-05-05 12:01:24.326512','4','Comment 4 on Video 6@YT#DivuT0HpazQ: oh v6',1,'[{\"added\": {}}]',9,4),(12,'2021-05-05 12:01:40.053891','5','Comment 5 on Video 6@YT#DivuT0HpazQ: v6-rep',1,'[{\"added\": {}}]',9,4),(13,'2021-05-05 12:01:49.413044','5','Comment 5 on Video 6@YT#DivuT0HpazQ: v6-rep',2,'[{\"changed\": {\"fields\": [\"Parent\"]}}]',9,4),(14,'2021-05-05 12:02:03.793845','6','Comment 6 on Video 5@YT#l5XJdHfPc5o: v5',1,'[{\"added\": {}}]',9,4);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(9,'comment','comment'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'usr_auth0','profile'),(8,'video','video');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-12-27 12:49:05.338587'),(2,'auth','0001_initial','2020-12-27 12:49:05.789956'),(3,'admin','0001_initial','2020-12-27 12:49:07.069796'),(4,'admin','0002_logentry_remove_auto_add','2020-12-27 12:49:07.371248'),(5,'admin','0003_logentry_add_action_flag_choices','2020-12-27 12:49:07.386907'),(6,'contenttypes','0002_remove_content_type_name','2020-12-27 12:49:07.647413'),(7,'auth','0002_alter_permission_name_max_length','2020-12-27 12:49:07.850910'),(8,'auth','0003_alter_user_email_max_length','2020-12-27 12:49:07.897736'),(9,'auth','0004_alter_user_username_opts','2020-12-27 12:49:07.897736'),(10,'auth','0005_alter_user_last_login_null','2020-12-27 12:49:08.024169'),(11,'auth','0006_require_contenttypes_0002','2020-12-27 12:49:08.024169'),(12,'auth','0007_alter_validators_add_error_messages','2020-12-27 12:49:08.040023'),(13,'auth','0008_alter_user_username_max_length','2020-12-27 12:49:08.180420'),(14,'auth','0009_alter_user_last_name_max_length','2020-12-27 12:49:08.332038'),(15,'auth','0010_alter_group_name_max_length','2020-12-27 12:49:08.354975'),(16,'auth','0011_update_proxy_permissions','2020-12-27 12:49:08.370473'),(17,'auth','0012_alter_user_first_name_max_length','2020-12-27 12:49:08.518893'),(18,'sessions','0001_initial','2020-12-27 12:49:08.596203'),(19,'usr_auth0','0001_initial','2021-01-07 12:17:50.139074'),(20,'video','0001_initial','2021-03-08 09:58:52.175238'),(21,'video','0002_auto_20210309_1104','2021-03-09 03:04:27.921883'),(22,'video','0003_auto_20210425_2117','2021-04-25 13:17:17.900341'),(23,'video','0004_auto_20210505_1715','2021-05-05 09:15:35.582832'),(24,'comment','0001_initial','2021-05-05 09:15:35.689573'),(25,'comment','0002_auto_20210505_1955','2021-05-05 11:55:55.569506'),(26,'comment','0003_auto_20210505_2317','2021-05-05 15:17:52.210677');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3x0ah45jqqg3kwoz7ael18kacah4gdsd','.eJxVjEEOwiAQRe_C2hA6A1Jcuu8ZCDCDVA0kpV0Z765NutDtf-_9l_BhW4vfOi9-JnERWpx-txjSg-sO6B7qrcnU6rrMUe6KPGiXUyN-Xg_376CEXr41gjbKgmMD1tjBEgOfc7IDZmDNiCkm5RxD1HHkQKgz2jxqCEo5QifeH8jNN30:1lRcgE:3NOBRK8aC5GAd_sLKYdbKonZ72G-y-k1T0ZhX7Q-o10','2021-04-14 15:22:50.727633'),('65q511pbw1cd702aufwvf78eqn22audx','e30:1lJEhr:f9j8-cWRKT5lObujp3Wblcyvdvhy3H_vCPwtJIUxa2k','2021-03-22 12:09:51.475139'),('7zs5bf7kvpmb3dzy6omlu81p5p3359fb','.eJxVjDkOwjAUBe_iGlleYsdQ0nMG62_gALKlOKkQd4dIKaB9M_NeKsO6lLx2mfPE6qSsOvxuCPSQugG-Q701Ta0u84R6U_ROu740lud5d_8OCvTyrcU7QbEcmBI6YnIJQxQ3RoAjmGhSGk0AF3GwxhNbT_4qxgTLmOIwqPcH_AU35A:1ktVau:NjpnjfMqw7dQoZ7BXdWBVgFX4mvae71i9eJh-nMVhEQ','2021-01-10 12:56:20.010557'),('agochyb2f961ofeacjir9ual93cnlebm','e30:1lJCfl:7FUfLzaBMfUU_o3ZEEqID_79FTrst3x5kkIQ5B2rW7Q','2021-03-22 09:59:33.831913'),('akz7aa7zoqzepxvg6nakg8n2jp6yfng7','.eJxVjEEOwiAQRe_C2hA6A1Jcuu8ZCDCDVA0kpV0Z765NutDtf-_9l_BhW4vfOi9-JnERWpx-txjSg-sO6B7qrcnU6rrMUe6KPGiXUyN-Xg_376CEXr41gjbKgmMD1tjBEgOfc7IDZmDNiCkm5RxD1HHkQKgz2jxqCEo5QifeH8jNN30:1lJEuJ:b62WglVUtC9o0TaQUIP4wlQ5XxRFRw-1XK7QzW0xnjQ','2021-03-22 12:22:43.368766'),('cyhthgnr2aexd3643c13pb0976l40ii9','e30:1lJCgS:ZQbbtsL-jcMoXz4QVkK3Q0w4OjAq4qi4KUvihrZYbtg','2021-03-22 10:00:16.556300'),('o3vgvwt97r70400ygsidha1aux0zfdm2','.eJxVjEEOwiAQRe_C2hA6A1Jcuu8ZCDCDVA0kpV0Z765NutDtf-_9l_BhW4vfOi9-JnERWpx-txjSg-sO6B7qrcnU6rrMUe6KPGiXUyN-Xg_376CEXr41gjbKgmMD1tjBEgOfc7IDZmDNiCkm5RxD1HHkQKgz2jxqCEo5QifeH8jNN30:1leDde:EOvt2YHLBnvKuFDxKMqLQCSXaBfuxnwZEEfb1AfWHS4','2021-05-19 09:16:14.215420'),('qnuy97r2523xf6wuql792t80h9aqagyt','.eJxVjEEOwiAQRe_C2hA6A1Jcuu8ZCDCDVA0kpV0Z765NutDtf-_9l_BhW4vfOi9-JnERWpx-txjSg-sO6B7qrcnU6rrMUe6KPGiXUyN-Xg_376CEXr41gjbKgmMD1tjBEgOfc7IDZmDNiCkm5RxD1HHkQKgz2jxqCEo5QifeH8jNN30:1lodAY:eNe9fEvxWtsR_Z191sSrAwwd3-Qo4hxMc9fbEgr-RGc','2021-06-17 02:33:14.617049');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bio` longtext NOT NULL,
  `birth_date` date DEFAULT NULL,
  `gender` smallint(6) NOT NULL,
  `auth0_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth0_user_id` (`auth0_user_id`),
  CONSTRAINT `profile_auth0_user_id_156856eb_fk_auth_user_id` FOREIGN KEY (`auth0_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
INSERT INTO `profile` VALUES (1,'',NULL,0,3),(2,'',NULL,0,4),(4,'',NULL,1,2),(5,'string','2021-05-02',0,5);
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `videos`
--

DROP TABLE IF EXISTS `videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `videos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `source` varchar(2) NOT NULL,
  `platform_id` varchar(30) NOT NULL,
  `title` varchar(100) NOT NULL,
  `duration` bigint(20) NOT NULL,
  `description` longtext NOT NULL,
  `pub_date` datetime(6) NOT NULL,
  `category_id` int(11) NOT NULL,
  `channel_id` varchar(50) NOT NULL,
  `channel_title` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `videos`
--

LOCK TABLES `videos` WRITE;
/*!40000 ALTER TABLE `videos` DISABLE KEYS */;
INSERT INTO `videos` VALUES (2,'YT','fwQci1cRiFU','Effective Ways to Practice Arpeggios',690000000,'➡ Thank you for supporting me on Patreon!\\nhttps://www.patreon.com/nahresol\\n\\nNew Warm-Ups in ii-V-I: https://youtu.be/jKMNIB9sk18\\n\\nIn today\'s Practice Notes 59, I share ways to practice arpeggios that I believe are effective and efficient.  Although this video is very piano specific, there are some concepts that can translate over to other instruments as well.  These points of conscious practicing really helped me improve my piano technique over the years.\\n\\nThe two pieces of music I use to demonstrate these practice methods is Chopin\'s Etude Op. 10 No. 1 and Exercise 8A from my Modified Chopin Exercises book.\\n\\n➡ Get the Modified Chopin Exercises Book:  https://bit.ly/2HBpOk1\\n\\nHere are the time stamps for the video to help you navigate and reference the different sections:\\n00:45 -- Rhythms and Accenting\\n02:50 -- Why Rhythms and Accenting are Effective\\n03:44 -- Organizing Hand Positions\\n04:15 -- Blocking\\n05:43 -- Micro-Adjustments and Relaxation\\n06:29 -- Elbow Movement\\n08:34 -- Kill Two Birds w/ One Stone\\n09:00 -- Teeter-Totter\\n10:09 -- Looping\\n10:45 -- Repeating Notes\\n\\nRhythm drills for practice: https://www.youtube.com/watch?v=sTq92MkSWQ4\\n\\nInstagram @nahresol\\nTwitter @nahresol\\nFacebook @practicenotes\\n\\nKeyboard: https://amzn.to/2NbPjYA\\nCamera: https://amzn.to/2BE54X3\\nLens: https://amzn.to/2NaQiby\\n\\nSubscribe to the channel to follow my uploads:\\nPRACTICE NOTES: https://www.youtube.com/playlist?list=PL0UfT1ar7nMclK9fh4hVcbwB-GJcUVzvY\\nSOUND BANK: https://www.youtube.com/playlist?list=PL0UfT1ar7nMc-RQEUNIo0kRIBohUizwFn\\nORIGINALS: https://www.youtube.com/playlist?list=PL0UfT1ar7nMdpYHYL2dw07s_W4xCMobpV\\n\\nAs always, thank you so much for watching, and thank you to all of you that leave comments.\\n\\nThis video is not sponsored and features no sponsored products but some links above are affiliate links (you don\'t pay more, but I earn a small commission for my recommendation).','2018-05-06 08:19:13.000000',10,'UC8R8FRt1KcPiR-rtAflXmeg','Nahre Sol'),(3,'YT','LZie2QC5Jbc','Quantum Operators',1306000000,'Quantum Operators for measurements of Energy, Position, and Momentum in Quantum Physics.  My Patreon page is at https://www.patreon.com/EugeneK','2016-03-28 12:57:11.000000',28,'UCJ0yBou72Lz9fqeMXh9mkog','Physics Videos by Eugene Khuto'),(4,'YT','WJownYnZ1ZQ','Maker: The Art of Terry Borman',1507000000,'A film that explores the life and work of world renowned luthier Terry Borman.  https://www.bormanviolins.com\n\n\nMusic in this video\nSong: The Tale of Tsar Saltan, Op. 57: Flight of the Bumble Bee\nArtist:  Scottish National Orchestra\nAlbum:  Russian Masterpieces\nLicensed to YouTube by:  NaxosofAmerica (on behalf of Chandos); UMPI, UMPG Publishing, BMG Rights Management, Warner Chappell, and 6 Music Rights Societies','2020-01-15 19:00:05.000000',10,'UCisoaS5VIOtmZL74_jPWCmQ','BormanViolins'),(5,'YT','l5XJdHfPc5o','Bach\'s C major prelude, deconstructed',587000000,'Bach\'s prelude in C major from book one of \'The Well-Tempered Clavier\' is one of the most recognisable pieces of piano music ever written. In this essay, I deconstruct the history, rhythm and harmony to try and work out why it has captivated musicians and listeners for centuries.\n\n▶ Support my channel: https://www.patreon.com/listeningin\n▶ Subscribe: https://bit.ly/2PlVaMS\n____________________\n▶ Website: http://www.barnabymartin.com\n▶ Twitter: https://twitter.com/BarnabyMartin\n\nFURTHER READING/RESEARCH\nKlavierbüchlein für Wilhelm Friedemann Bach: http://tinyurl.com/154z8h8a\nBach\'s Well-Tempered Clavier: The 48 Preludes and Fugues: https://www.amazon.co.uk/Bachs-Well-Tempered-Clavier-Preludes-Fugues/dp/0300178956/ref=sr_1_1?dchild=1&keywords=bach%27s+well-tempered+clavier+ledbetter&qid=1612254538&sr=8-1\n\nFURTHER WATCHING\nThat famous cello prelude, deconstructed [Vox]: https://www.youtube.com/watch?v=UIge2mYdTtM&t=526s\nAndrás Schiff on the recording of Bach\'s „The Well-Tempered Clavier\": https://www.youtube.com/watch?v=TdzLWKuo0YA','2021-02-02 15:31:35.000000',10,'UCiawGYzxoZSPDLReSFETqeQ','Listening In'),(6,'YT','DivuT0HpazQ','Dr Quantum   Double Slit Experiment   YouTube 1',342000000,'','2019-10-29 20:50:52.000000',22,'UCXFXosD6iYS2hhlT2lmQpJQ','Vadim Chernov');
/*!40000 ALTER TABLE `videos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-03 11:42:46
