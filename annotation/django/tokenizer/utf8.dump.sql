-- MySQL dump 10.13  Distrib 5.6.24, for osx10.8 (x86_64)
--
-- Host: boson.ckxiwph2m7md.us-west-2.rds.amazonaws.com    Database: boson_file_state
-- ------------------------------------------------------
-- Server version	5.6.23-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'adjudicator'),(1,'annotator');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_7ef6aa1c402fbb4d_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_7ef6aa1c402fbb4d_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_280e51ce6fd82d14_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_1d4f4f24025b5a9c_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add status',7,'add_status'),(20,'Can change status',7,'change_status'),(21,'Can delete status',7,'delete_status'),(22,'Can add text file',8,'add_textfile'),(23,'Can change text file',8,'change_textfile'),(24,'Can delete text file',8,'delete_textfile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$TwlU2WV0b7U8$d4a8HdqClOvVlwRQXWQ7IOd+toGcrH/Gt7gkfV9hVTg=','2015-08-11 17:46:36.600659',0,'test','','','',0,1,'2015-08-04 23:47:03.034451'),(2,'pbkdf2_sha256$20000$TfRLiT21XxZP$H42amD8DGCJGoAxW11bs5aoNvk6e205jdMIjYmRMgC8=','2015-08-12 05:01:43.429128',0,'handong','','','',0,1,'2015-08-04 23:52:14.000000'),(3,'pbkdf2_sha256$20000$XnkfnxFquYAt$ouHc5nLxomv5zu3pfVv2dK8iPhX3VrvVHaF351SkxYs=','2015-08-12 04:17:47.341368',0,'nanfang','','','',0,1,'2015-08-04 23:52:15.000000'),(4,'pbkdf2_sha256$20000$2UyLA1zlIJeS$8mFVW77Vv5Tn52LqnVVixQgk2HT9pVo4nowRjlVbKKM=','2015-08-10 04:25:05.444506',0,'nina','','','',0,1,'2015-08-04 23:52:16.000000'),(5,'pbkdf2_sha256$20000$lY7v4Y37ACCT$4BxNVhPoWQ7apcS3F9LeBnRbsyUWQ3L8wGp68p5UeOk=','2015-08-10 04:25:12.263017',0,'yue','','','',0,1,'2015-08-04 23:52:17.000000'),(6,'pbkdf2_sha256$20000$jx4nOYgKoRTT$4J0asrSRQPtdUeyPlrS07ndk4pXPHXY3Z6bktwr2UsA=','2015-08-12 04:11:28.931952',0,'zhou','','','',0,1,'2015-08-04 23:52:18.577108'),(7,'pbkdf2_sha256$20000$YR6b7K5QfA5P$4dG36Jc9YYzDO2fEjDx5PpDe8glfFvdQR9ijwNxB/dU=','2015-08-11 17:37:55.084481',0,'junyan','','','',0,1,'2015-08-04 23:52:19.000000'),(8,'pbkdf2_sha256$20000$Arx6vtYW6I6U$LvfwDi50JprjSkVVWNtsYjXq/YkRoMyKCT72ZYJf9EY=','2015-08-12 04:23:13.099036',0,'shaodian','','','',0,1,'2015-08-04 23:52:20.000000'),(9,'pbkdf2_sha256$20000$Uf0h9Yc5jeSv$wy8yZZyQ+G7m3mcI9Y3c5yqPOlw7yTWkED9/Y6ttu/8=','2015-08-11 00:48:07.657412',0,'ying','','','',0,1,'2015-08-04 23:52:21.000000'),(10,'pbkdf2_sha256$20000$Si6wkqkRDUWL$SSNvtT70KJkQzW39fLKHArXA/GJCZxpZmBcZOEBclw0=','2015-08-10 18:57:01.722481',0,'jinsen','','','',0,1,'2015-08-04 23:52:22.000000'),(12,'pbkdf2_sha256$20000$a5sa2C6QP4uk$cXuxN+Z2OySuM6Bxlgafvpi50+Ek0fPZLE3vBhc9Tqo=','2015-08-12 03:19:20.612969',1,'admin','','','',1,1,'2015-08-05 02:10:02.976650'),(13,'pbkdf2_sha256$20000$FVXYaBNf9izx$lfx00pLpI+73hsEqp0QshzHyTnBnZTwlLyiChJ6zTPI=','2015-08-12 04:17:19.866072',0,'tester','','','',0,1,'2015-08-12 02:49:47.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_1f3a8d94ab961d27_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_1f3a8d94ab961d27_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_8fc6eb19da31bb5_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (12,2,1),(15,3,1),(16,3,2),(17,4,1),(21,5,1),(5,6,1),(14,7,1),(18,8,1),(19,8,2),(20,9,1),(13,10,1),(25,13,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_us_permission_id_d84f7202756c8ef_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_us_permission_id_d84f7202756c8ef_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_5210e1ae07d55204_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  KEY `djang_content_type_id_295e2fc36e9302c1_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_3de2adff4e71346d_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_295e2fc36e9302c1_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_3de2adff4e71346d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-08-05 02:11:07.990811','2','handong',2,'Changed groups.',4,12),(2,'2015-08-05 02:11:24.376504','10','jinsen',2,'Changed groups.',4,12),(3,'2015-08-05 02:11:42.856830','7','junyan',2,'Changed groups.',4,12),(4,'2015-08-05 02:11:57.553889','3','nanfang',2,'Changed groups.',4,12),(5,'2015-08-05 02:12:16.143316','4','nina',2,'Changed groups.',4,12),(6,'2015-08-05 02:12:41.270795','8','shaodian',2,'Changed groups.',4,12),(7,'2015-08-05 02:12:58.111723','9','ying',2,'Changed groups.',4,12),(8,'2015-08-05 02:13:19.286380','5','yue',2,'Changed groups.',4,12),(9,'2015-08-12 02:49:47.271994','13','tester1',1,'',4,12),(10,'2015-08-12 02:50:06.547282','14','tester2',1,'',4,12),(11,'2015-08-12 02:50:23.191566','14','tester2',2,'Changed groups.',4,12),(12,'2015-08-12 02:50:43.457703','13','tester1',2,'Changed groups.',4,12),(13,'2015-08-12 02:57:15.158582','14','tester2',3,'',4,12),(14,'2015-08-12 02:57:43.943984','13','tester',2,'Changed username.',4,12),(15,'2015-08-12 03:18:08.044233','1','test',2,'Changed password.',4,12),(16,'2015-08-12 03:19:51.388129','1','test',2,'Changed password.',4,12),(17,'2015-08-12 03:20:18.072567','13','tester',2,'Changed password.',4,12),(18,'2015-08-12 03:20:29.507988','13','tester',2,'No fields changed.',4,12);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_4543668ce1f32478_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'editor','status'),(8,'editor','textfile'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-08-04 23:46:53.445544'),(2,'auth','0001_initial','2015-08-04 23:46:55.612571'),(3,'admin','0001_initial','2015-08-04 23:46:56.374635'),(4,'contenttypes','0002_remove_content_type_name','2015-08-04 23:46:57.266946'),(5,'auth','0002_alter_permission_name_max_length','2015-08-04 23:46:57.750604'),(6,'auth','0003_alter_user_email_max_length','2015-08-04 23:46:58.234974'),(7,'auth','0004_alter_user_username_opts','2015-08-04 23:46:58.609767'),(8,'auth','0005_alter_user_last_login_null','2015-08-04 23:46:59.123871'),(9,'auth','0006_require_contenttypes_0002','2015-08-04 23:46:59.486355'),(10,'editor','0001_initial','2015-08-04 23:47:00.937934'),(11,'editor','0002_auto_20150802_1853','2015-08-04 23:47:02.023809'),(12,'editor','0003_auto_20150803_0346','2015-08-04 23:47:02.669335'),(13,'editor','0004_initialize_development_data','2015-08-04 23:47:03.890325'),(14,'sessions','0001_initial','2015-08-04 23:47:04.548905');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('01n3fa7m4gi7ty66og4br8osydmof76h','M2E0NmVmYjgwMTlhYmJiYjQwY2IwMTdlNGUxZjM5ZjBjMzUzNzk3OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ5NjY2ZjFmN2FkZjEzZTBhZGM3MTNkNzYwMTkxNGQ1YzVjY2VlYmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2015-08-25 17:27:25.418397'),('19uk1y117aed5bvlfnbo1bnrl0i0cf4x','MTBiY2QyODcyNjRjZGFhZWQ3NGJhNGIwOTM0ZTRhNDk4YTgyNzBjNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjRlZWE3YjZkMzI3OTM4MDk0NjNlMTQyYTMwNmNkN2FlYmJlYzIwMDYiLCJfYXV0aF91c2VyX2lkIjoiNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-08-25 17:37:55.125279'),('1g2qxygj15hn9zv3qp5s8ytpwy53jtll','M2E0NmVmYjgwMTlhYmJiYjQwY2IwMTdlNGUxZjM5ZjBjMzUzNzk3OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ5NjY2ZjFmN2FkZjEzZTBhZGM3MTNkNzYwMTkxNGQ1YzVjY2VlYmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2015-08-26 04:23:13.107006'),('1gej99aovd497dy37l8bnv3nwpcf5k0g','ODI4NTA1NmE4ZWU0YWY1OTcyZTQ1NDk1ZDU4MGQ2YzA4N2MwYzhiOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjdmNGUzMjkwMjFiN2YwYTFmY2E4YTJjY2ExN2YzOTJhZDQ0MjdiYjUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI5In0=','2015-08-25 00:48:10.417507'),('1j92wor4w4gd5gfdu3wr4osouu0s5oft','NzVkMGFjNzVhODYyMzM5NzM1ZWQ3YzQ0ZjdjMTVkYzY1ODk3NTliZTp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk5ZjEzZjA4MDQ1ZTdjMDZmMDM4Nzg1N2UxZmE0OWFjNzIxY2I5NDIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2015-08-22 18:27:46.485500'),('40wlaclnz9xlxjesapnkwjis3dubpdbl','ZjNjNTM0YjI3MjAyOGRmMjAwYmFlZDFmNDM1MWE1YTcyOTVlZDkwMDp7Il9hdXRoX3VzZXJfaGFzaCI6IjAxM2I5YTJkNzU4ZmEyNjE0YzQwZjdiY2VjMmUzNzM0NTk3YzZjNjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-08-19 18:36:40.831672'),('4nubfjtysqn3smij4udyn4hu3a3j1bot','M2E0NmVmYjgwMTlhYmJiYjQwY2IwMTdlNGUxZjM5ZjBjMzUzNzk3OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ5NjY2ZjFmN2FkZjEzZTBhZGM3MTNkNzYwMTkxNGQ1YzVjY2VlYmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2015-08-25 17:27:24.398451'),('6q5fxupb3n6jk4akdad90dykz4mltspz','MmUyYjUxZWExNDUzYjI4ZWY1MGQzMjUyZjExYjg0ZTI4M2Q4NjVjNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjdhMjBkYmZiNGY5MmZhNDI4M2U4M2YzMDc5MWM0NjhhNzEwYjk5NTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2015-08-19 09:34:13.161304'),('754elvwnht3xl2kogbt01hfkk9pwpn1r','Yzg3MWUwYTk0ZjRhNjM5N2MxNWM1YWI2ZGI2ODg5OTgyOTZlNDhhNTp7Il9hdXRoX3VzZXJfaGFzaCI6Ijg1MzNiOWQyNWE5YmUyMTIwZTM3NTczMDQ4MDAyZDg3MjM2MTJiY2UiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-08-22 04:31:05.074824'),('7e1xs6hiuapzw0pce5250ck72ucwxljy','YTQyOWIyMWQyZWJhMDZjNjliZTYzNjZkM2ZiYjhlMDg0OGM5M2VkNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjdhMjBkYmZiNGY5MmZhNDI4M2U4M2YzMDc5MWM0NjhhNzEwYjk5NTQiLCJfYXV0aF91c2VyX2lkIjoiMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-08-22 07:26:12.177526'),('7ykab7x5sacvtqjua4dms78vdravvpo1','ODBhMjA1ZDg4M2VkMWIyZjE0MGE2NGYwYTFlNWExNjRlNTM4MDNiOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjRlZWE3YjZkMzI3OTM4MDk0NjNlMTQyYTMwNmNkN2FlYmJlYzIwMDYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI3In0=','2015-08-24 05:09:45.185131'),('a38ui5u07k47pkglx1b6vxqk07yv2eyr','M2E0NmVmYjgwMTlhYmJiYjQwY2IwMTdlNGUxZjM5ZjBjMzUzNzk3OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ5NjY2ZjFmN2FkZjEzZTBhZGM3MTNkNzYwMTkxNGQ1YzVjY2VlYmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2015-08-25 17:27:24.944758'),('cq0kii4yqkrvqdrx9hoze1ne6s9i0iuo','M2E0NmVmYjgwMTlhYmJiYjQwY2IwMTdlNGUxZjM5ZjBjMzUzNzk3OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ5NjY2ZjFmN2FkZjEzZTBhZGM3MTNkNzYwMTkxNGQ1YzVjY2VlYmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2015-08-25 17:27:25.262245'),('dhcjck509ak5tk40zgfe7r0byws9u7lg','ZjNjNTM0YjI3MjAyOGRmMjAwYmFlZDFmNDM1MWE1YTcyOTVlZDkwMDp7Il9hdXRoX3VzZXJfaGFzaCI6IjAxM2I5YTJkNzU4ZmEyNjE0YzQwZjdiY2VjMmUzNzM0NTk3YzZjNjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-08-23 00:06:05.602678'),('fybrjqzt81kw7zov87ip0ulkynnp063v','MmUyYjUxZWExNDUzYjI4ZWY1MGQzMjUyZjExYjg0ZTI4M2Q4NjVjNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjdhMjBkYmZiNGY5MmZhNDI4M2U4M2YzMDc5MWM0NjhhNzEwYjk5NTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2015-08-19 23:40:27.156136'),('iqw5w2fxiyiekbmyx6idmoxydcmn7wdt','M2E0NmVmYjgwMTlhYmJiYjQwY2IwMTdlNGUxZjM5ZjBjMzUzNzk3OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ5NjY2ZjFmN2FkZjEzZTBhZGM3MTNkNzYwMTkxNGQ1YzVjY2VlYmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2015-08-25 17:41:02.555523'),('kkgrvei0yqj29jjt8hfmliy2wj56x53n','YjYwYjY0NTRlMDA4NDY4ZjA2ZDg0NTNlMDU2NzZiYTM3MGNkMTk2OTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9oYXNoIjoiN2EyMGRiZmI0ZjkyZmE0MjgzZTgzZjMwNzkxYzQ2OGE3MTBiOTk1NCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-08-20 02:41:49.232084'),('mpalh7bjltzgkwa8eqrvbswo44er2p5e','M2E0NmVmYjgwMTlhYmJiYjQwY2IwMTdlNGUxZjM5ZjBjMzUzNzk3OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ5NjY2ZjFmN2FkZjEzZTBhZGM3MTNkNzYwMTkxNGQ1YzVjY2VlYmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2015-08-25 17:27:24.588985'),('nyi1hna3e0c6cz0w2mwl71k70gjnpqk3','YTEzNjNkZmFlM2FkNjFiMGEyNTY1OGI1MmM2YzM4YjNlNGZhNWUyZjp7Il9hdXRoX3VzZXJfaGFzaCI6IjMzNWJjYjVjNjViMGJlMzIxNzAxZDFjN2MzYzExZGNmOGVmMDFlYjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI2In0=','2015-08-23 04:19:13.235098'),('pymwxtsyhcyeh64z5h5zzk1er5cjl6fx','M2E0NmVmYjgwMTlhYmJiYjQwY2IwMTdlNGUxZjM5ZjBjMzUzNzk3OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ5NjY2ZjFmN2FkZjEzZTBhZGM3MTNkNzYwMTkxNGQ1YzVjY2VlYmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2015-08-25 17:27:25.106764'),('qbsmrbzpw3p2ie4b9rvhalvrq21weqdu','M2E0NmVmYjgwMTlhYmJiYjQwY2IwMTdlNGUxZjM5ZjBjMzUzNzk3OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ5NjY2ZjFmN2FkZjEzZTBhZGM3MTNkNzYwMTkxNGQ1YzVjY2VlYmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2015-08-25 17:27:24.767375'),('u3b0d5x84m29wrpf8brnh8uz9vk3ffsx','NzVkMGFjNzVhODYyMzM5NzM1ZWQ3YzQ0ZjdjMTVkYzY1ODk3NTliZTp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk5ZjEzZjA4MDQ1ZTdjMDZmMDM4Nzg1N2UxZmE0OWFjNzIxY2I5NDIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2015-08-26 05:01:57.547085'),('ubxt8pumj8xvsnsfny6wdr60gbfwr5fm','M2E0NmVmYjgwMTlhYmJiYjQwY2IwMTdlNGUxZjM5ZjBjMzUzNzk3OTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ5NjY2ZjFmN2FkZjEzZTBhZGM3MTNkNzYwMTkxNGQ1YzVjY2VlYmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI4In0=','2015-08-19 03:53:25.257119'),('wb88o105alm7r987ucefifvivkkzx4n7','NzVkMGFjNzVhODYyMzM5NzM1ZWQ3YzQ0ZjdjMTVkYzY1ODk3NTliZTp7Il9hdXRoX3VzZXJfaGFzaCI6Ijk5ZjEzZjA4MDQ1ZTdjMDZmMDM4Nzg1N2UxZmE0OWFjNzIxY2I5NDIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2015-08-23 03:33:20.265163'),('x0j9q8j2qtfeinukuvn2djtqo5kk6a8x','YTEzNjNkZmFlM2FkNjFiMGEyNTY1OGI1MmM2YzM4YjNlNGZhNWUyZjp7Il9hdXRoX3VzZXJfaGFzaCI6IjMzNWJjYjVjNjViMGJlMzIxNzAxZDFjN2MzYzExZGNmOGVmMDFlYjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI2In0=','2015-08-26 04:11:24.612465'),('z6dyrssyz3cf27ab4u1wqpls2fkmyqhl','ZTYzZDAwZmUzOWZkMGZjM2IyMzhkMWUxZmY0ZDJhNDJkMDJhYWYwYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM0Yzc0MjUwZWQ1MmJhMTY2MDNhN2U4Njg0NGIyZmNjYzU3YjlmMTAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxMyJ9','2015-08-26 04:05:26.037819');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editor_status`
--

DROP TABLE IF EXISTS `editor_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `editor_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state_text` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editor_status`
--

LOCK TABLES `editor_status` WRITE;
/*!40000 ALTER TABLE `editor_status` DISABLE KEYS */;
INSERT INTO `editor_status` VALUES (1,'NA'),(2,'IN'),(3,'DONE'),(4,'DIRTY');
/*!40000 ALTER TABLE `editor_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editor_textfile`
--

DROP TABLE IF EXISTS `editor_textfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `editor_textfile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(50) NOT NULL,
  `file_location` varchar(200) NOT NULL,
  `first_worker_id` int(11) NOT NULL,
  `first_worker_state_id` int(11) NOT NULL,
  `judge_id` int(11) NOT NULL,
  `jurisdiction_state_id` int(11) NOT NULL,
  `second_worker_id` int(11) NOT NULL,
  `second_worker_state_id` int(11) NOT NULL,
  `first_worker_comment` longtext NOT NULL,
  `second_worker_comment` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `editor_textfile_first_worker_id_53450ef57279263a_fk_auth_user_id` (`first_worker_id`),
  KEY `edito_first_worker_state_id_12923674b9504ae1_fk_editor_status_id` (`first_worker_state_id`),
  KEY `editor_textfile_judge_id_19d3d4b65132d731_fk_auth_user_id` (`judge_id`),
  KEY `edito_jurisdiction_state_id_2ed93eaf1b96f8fc_fk_editor_status_id` (`jurisdiction_state_id`),
  KEY `editor_textfil_second_worker_id_70c9b44bae3cbd79_fk_auth_user_id` (`second_worker_id`),
  KEY `edito_second_worker_state_id_aa51c98c802666f_fk_editor_status_id` (`second_worker_state_id`),
  CONSTRAINT `edito_first_worker_state_id_12923674b9504ae1_fk_editor_status_id` FOREIGN KEY (`first_worker_state_id`) REFERENCES `editor_status` (`id`),
  CONSTRAINT `edito_jurisdiction_state_id_2ed93eaf1b96f8fc_fk_editor_status_id` FOREIGN KEY (`jurisdiction_state_id`) REFERENCES `editor_status` (`id`),
  CONSTRAINT `edito_second_worker_state_id_aa51c98c802666f_fk_editor_status_id` FOREIGN KEY (`second_worker_state_id`) REFERENCES `editor_status` (`id`),
  CONSTRAINT `editor_textfil_second_worker_id_70c9b44bae3cbd79_fk_auth_user_id` FOREIGN KEY (`second_worker_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `editor_textfile_first_worker_id_53450ef57279263a_fk_auth_user_id` FOREIGN KEY (`first_worker_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `editor_textfile_judge_id_19d3d4b65132d731_fk_auth_user_id` FOREIGN KEY (`judge_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editor_textfile`
--

LOCK TABLES `editor_textfile` WRITE;
/*!40000 ALTER TABLE `editor_textfile` DISABLE KEYS */;
INSERT INTO `editor_textfile` VALUES (1,'A 00 (1).txt','editor/data/original/A 00 (1).txt',1,1,1,1,1,1,'',''),(2,'A 00 (6).txt','',10,3,3,2,7,3,'','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>\n<p><span style=\"font-size: medium;\">患者 一 日 来 干 双下肢 无力？ 暂分如此</span></p>'),(3,'A 00 (7).txt','',6,4,1,1,4,2,'<p><span style=\"font-size: medium;\">脐周</span></p>\n<p><font size=\"3\">我院 vs 外院</font></p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(4,'A 00 (8).txt','',7,3,1,1,9,2,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>\n<p>有些地方我觉得是扫描缺失字比如</p>\n<p>这里：&nbsp;<span style=\"font-size: medium;\">直接</span><span style=\"font-size: medium;\">对光反射 灵敏</span></p>\n<p><span style=\"font-size: medium;\">而例文中是：&nbsp;</span><span style=\"color: #333333; font-family: \'Helvetica Neue\', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px;\">直接对光反 灵敏</span></p>\n<p><span style=\"color: #333333; font-family: \'Helvetica Neue\', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px;\">少了一个射字</span></p>\n<p><span style=\"font-size: medium;\">食管胃底静脉曲张 可能 大 （感觉是可能性大）</span></p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(5,'A 00 (9).txt','',9,3,1,1,2,4,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(6,'A 00 (10).txt','',4,2,1,1,10,2,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(7,'A 00 (11).txt','',3,4,1,1,2,4,'<p>血常规，尿常规是否需要分开成：血 常规；</p>\n<p>影像学检查里的描述语，如&ldquo;肠管样低回声&rdquo;，分成&ldquo;肠管样 低回声&rdquo;还是&ldquo;肠管样 低 回声&rdquo;或者当成一个词；</p>\n<p>&nbsp;</p>\n<p>&ldquo;入院诊断&rdquo;、&ldquo;出院诊断&rdquo;、&ldquo;入院记录&rdquo;、&ldquo;准予今日出院&rdquo;、&ldquo;不适随诊&rdquo;、&ldquo;药物过敏史&rdquo;，&ldquo;毒物接触史&rdquo;；</p>\n<p class=\"MsoNormal\"><span style=\"font-family: 宋体; mso-ascii-font-family: Calibri; mso-ascii-theme-font: minor-latin; mso-fareast-font-family: 宋体; mso-fareast-theme-font: minor-fareast; mso-hansi-font-family: Calibri; mso-hansi-theme-font: minor-latin;\">&ldquo;巩膜无黄染&rdquo;、&ldquo;双侧瞳孔等大等圆&rdquo;、&ldquo;肛门、外生殖器未查&rdquo;、&ldquo;双肺呼吸音清&rdquo;、&ldquo;淋巴结肿大&rdquo;；</span></p>\n<p class=\"MsoNormal\"><span style=\"font-family: 宋体; mso-ascii-font-family: Calibri; mso-ascii-theme-font: minor-latin; mso-fareast-font-family: 宋体; mso-fareast-theme-font: minor-fareast; mso-hansi-font-family: Calibri; mso-hansi-theme-font: minor-latin;\">&ldquo;未触及&rdquo;、&ldquo;未扪及&rdquo;、&ldquo;未闻及&rdquo;，&ldquo;未见&rdquo;可以不分开吗？</span></p>\n<p>&nbsp;</p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(8,'A 00 (12).txt','',8,3,3,2,6,3,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','<p>&nbsp;测试提交即保存。测试提交后刷新页面，更新页面参数。</p>'),(9,'A 00 (13).txt','',2,4,1,1,9,2,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(10,'A 00 (14).txt','',3,4,1,1,2,4,'<p>&ldquo;吸烟嗜好&rdquo;、&ldquo;饮酒嗜好&rdquo;可否不分？</p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(11,'A 00 (15).txt','',3,4,1,1,7,3,'<p>&ldquo;AMA（+）&rdquo;中间是否需要分开</p>\n<p>&nbsp;</p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下</p>\n<p>。</p>\n<p><span style=\"font-size: medium;\">脾大 估计是一个词</span></p>'),(12,'A 00 (16).txt','',2,4,1,1,9,2,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(13,'A 00 (17).txt','',5,3,1,1,10,2,'<p><span style=\"font-size: medium;\">病案号,&nbsp;</span><span style=\"font-size: medium;\">已婚,&nbsp;</span><span style=\"font-size: medium;\">北京市,&nbsp;</span><span style=\"font-size: medium;\">昨日</span></p>\n<p><span style=\"font-size: medium;\">109/L,&nbsp;</span><span style=\"font-size: medium;\">78.5%</span></p>\n<p><span style=\"font-size: medium;\">血气分析,&nbsp;</span><span style=\"font-size: medium;\">心酶三项</span></p>\n<p><span style=\"font-size: medium;\">肺感染,&nbsp;</span><span style=\"font-size: medium;\">肺部感染,&nbsp;</span><span style=\"font-size: medium;\">肺动脉高压</span></p>\n<p><span style=\"font-size: medium;\">解痉平喘,&nbsp;</span><span style=\"font-size: medium;\">速尿利尿</span></p>\n<p><span style=\"font-size: medium;\">普米克令舒雾化吸入</span></p>\n<p><span style=\"font-size: medium;\">心脑肾等慢性病史</span></p>\n<p><span style=\"font-size: medium;\">胃振水音</span></p>\n<p><span style=\"font-size: medium;\">胆囊切除术后</span></p>\n<p><span style=\"font-size: medium;\">慢支、肺气肿</span></p>\n<p><span style=\"font-size: medium;\">行术后切除治疗</span></p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(14,'A 00 (18).txt','',3,4,1,1,4,2,'<p>q8h需要分隔吗？</p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(15,'A 00 (19).txt','',8,3,1,1,9,2,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(16,'A 00 (20).txt','',6,4,1,1,5,3,'<p>大小便失禁 &nbsp;大便失禁 小便失禁</p>\n<p><span style=\"font-size: medium;\">冠状动脉粥样硬化性 心脏病&nbsp;</span><br style=\"font-size: medium;\" /><span style=\"font-size: medium;\">陈旧性 脑梗塞&nbsp;</span></p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(17,'A 00 (21).txt','',7,3,1,1,9,2,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(18,'A 00 (22).txt','',4,2,1,1,3,4,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','<p>若为&ldquo;抗炎支持治疗&rdquo;，应分开为&ldquo;抗炎 支持 治疗&rdquo;，&ldquo;脱水治疗&rdquo;&ldquo;支持治疗&rdquo;&ldquo;抗炎治疗&rdquo;单独出现时是否分开？</p>'),(19,'A 00 (23).txt','',8,3,1,1,6,4,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','<p>统一一下，全腹，右上腹部。。。。</p>'),(20,'A 00 (24).txt','',9,2,1,1,2,4,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(21,'A 00 (25).txt','',5,3,1,1,2,4,'<p><span style=\"font-size: medium;\">右侧小脑半球小片状低密度影</span></p>\n<p><span style=\"font-size: medium;\">双肺叩清</span></p>\n<p><span style=\"font-size: medium;\">全腹软</span></p>\n<p><span style=\"font-size: medium;\">全腹未扪及包块</span></p>\n<p><span style=\"font-size: medium;\">胃振水音</span></p>\n<p><span style=\"font-size: medium;\">复测血压</span></p>\n<p><span style=\"font-size: medium;\">糖加胰岛素治疗</span></p>\n<p><span style=\"font-size: medium;\">介入科</span></p>\n<p><span style=\"font-size: medium;\">头颅CT</span></p>\n<p><span style=\"font-size: medium;\">保守治疗</span></p>\n<p><span style=\"font-size: medium;\">明日</span></p>\n<p><span style=\"font-size: medium;\">随诊</span></p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(22,'A 00 (26).txt','',9,2,1,1,8,3,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(23,'A 00 (27).txt','',10,3,1,1,6,4,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','<p>所有的 &nbsp; &ldquo;不详&rdquo;</p>\n<p>双肺 左肺 右肺 。。。</p>\n<p><span style=\"font-size: medium;\">&ldquo;普米克 1 mg * 25 支/雾化 tid 可必特 2.5 ml * 30支 / 2.5 ml 雾化 tid&nbsp;</span><span style=\"font-size: medium;\">杜密克 10 g * 12 / 10 g bid 加斯清5 mg * 20 /5 mgqd&rdquo; &nbsp;倒数第一行</span></p>'),(24,'A 00 (28).txt','',2,4,1,1,6,4,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','<p><span style=\"font-size: medium;\">&ldquo;心包 积液&rdquo; &nbsp;统一分词方法</span></p>'),(25,'A 00 (29).txt','',4,2,1,1,7,3,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(26,'A 00 (30).txt','',7,3,1,1,4,2,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>\n<p><span style=\"font-size: medium;\">控制 可 ? 暂且分2词</span></p>\n<p><span style=\"font-size: medium;\">全腹 未 扪及包块？ 暂分如此</span></p>\n<p><span style=\"font-size: medium;\">LYMPH % 35.3 %，切分百分号</span></p>\n<p><span style=\"font-size: medium;\">右侧叶间裂&nbsp;积液 ？ 暂分如此</span></p>\n<p><span style=\"font-size: medium;\">欣康 20 mg*20#/20 mg po bid ？ 暂分如此</span></p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(27,'A 00 (31).txt','',8,3,1,1,9,2,'<p><span style=\"font-size: medium;\">复查 血常规</span></p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(28,'A 00 (32).txt','',7,3,1,1,9,2,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>\n<p><span style=\"font-size: medium;\">未 见 胃肠型 及 蠕动波？ 暂分如此</span></p>\n<p><span style=\"font-size: medium;\">全 腹未 扪及 包块？ 暂分如此</span></p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(29,'A 00 (33).txt','',10,3,1,1,7,4,'<p>肝脾大要不要分开</p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(30,'A 00 (34).txt','',10,3,1,1,3,4,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','<p><span style=\"font-size: medium;\">\"GLASGOW评分：E4V5M6\"评分名称需与后面的分数分开吗？</span></p>'),(31,'A 00 (35).txt','',10,3,1,1,3,4,'<p><span style=\"font-size: medium;\">右顶叶片状高低混杂密度影</span></p>\n<p><span style=\"font-size: medium;\">右侧半卵圆中心多发片状低密</span><span style=\"font-size: medium;\">度影</span></p>\n<p><span style=\"font-size: medium;\">现病史部分需医生review</span></p>',''),(32,'A 00 (36).txt','',4,2,1,1,2,4,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(33,'A 00 (37).txt','',5,3,1,1,2,4,'<p><span style=\"font-size: medium;\">大汗</span></p>\n<p><span style=\"font-size: medium;\">尿量减少</span></p>\n<p><span style=\"font-size: medium;\">平卧</span></p>\n<p><span style=\"font-size: medium;\">尿量减少</span></p>\n<p><span style=\"font-size: medium;\">舌下含服硝酸甘油</span></p>\n<p><span style=\"font-size: medium;\">极高危组</span></p>\n<p><span style=\"font-size: medium;\">冠状动脉支架置入术后</span></p>\n<p><span style=\"font-size: medium;\">胸部压榨感</span></p>\n<p><span style=\"font-size: medium;\">双肺叩诊过清音</span></p>\n<p><span style=\"font-size: medium;\">慢性心功能不全(NYHAⅣ级)</span></p>\n<p><span style=\"font-size: medium;\">低流量吸氧</span></p>\n<p><span style=\"font-size: medium;\">予限盐限水</span></p>\n<p><span style=\"font-size: medium;\">双下肢股总静脉瓣膜功能不全,&nbsp;</span><span style=\"font-size: medium;\">腹主动脉迂曲显影</span></p>\n<p><span style=\"font-size: medium;\">双肾动脉</span><span style=\"font-size: medium;\">超声</span></p>\n<p><span style=\"font-size: medium;\">双肾肾内动脉阻力增高</span></p>\n<p><span style=\"font-size: medium;\">双肺气肿</span></p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(34,'A 00 (38).txt','',4,2,1,1,10,2,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(35,'A 00 (39).txt','',4,2,1,1,8,3,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(36,'A 00 (40).txt','',5,3,1,1,10,2,'<p><span style=\"font-size: medium;\">胸部CT检查示</span></p>\n<p><span style=\"font-size: medium;\">双下肺动脉及分支右</span><span style=\"font-size: medium;\">中叶肺动脉分支血栓</span></p>\n<p><span style=\"font-size: medium;\">双小腿肌间静脉血栓</span></p>\n<p><span style=\"font-size: medium;\">双肺叩清</span></p>\n<p><span style=\"font-size: medium;\">双下肢肌间静脉血栓形成</span></p>\n<p><span style=\"font-size: medium;\">洛赛克 20 mg X 7#/20mg bid；沐舒坦 30mgX50#/1# tid。</span></p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(37,'A 00 (41).txt','',6,4,1,1,3,4,'<p><span style=\"font-size: medium;\">慢性 肾功能 不全 病 史 &nbsp; &nbsp;\"慢性 肾功能不全\"？&ldquo;慢性 肾功能不全病&rdquo;？</span></p>',''),(38,'A 00 (42).txt','',10,2,1,1,8,3,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(39,'A 00 (43).txt','',5,3,1,1,3,4,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(40,'A 00 (44).txt','',8,3,1,1,4,2,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(41,'A 00 (45).txt','',5,3,3,2,8,3,'<p><span style=\"font-size: medium;\">昨日</span></p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(42,'A 00 (46).txt','',6,4,1,1,8,3,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','<p><span style=\"font-size: medium;\">立腹 见 双膈 下 游离气体&nbsp;</span></p>\n<p><span style=\"font-size: medium;\">不确定</span></p>\n<p><span style=\"font-size: medium;\">胆囊切除 术后</span></p>\n<p><font size=\"3\">两可分法？</font></p>\n<p><font size=\"3\">此病历应重点标注</font></p>'),(43,'A 00 (47).txt','',5,3,1,1,3,4,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(44,'A 00 (48).txt','',7,3,8,2,5,3,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>'),(45,'A 00 (49).txt','',7,3,1,1,6,4,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>\n<p><span style=\"font-size: medium;\">极高危 组？ 暂分如此</span></p>','<p><span style=\"font-size: medium;\">&ldquo;极 高危组&rdquo;</span></p>'),(46,'A 00 (50).txt','',5,3,1,1,6,4,'<p>请在此处留下评论。有任何不确定的疑问也请在此处留下。</p>','<p><span style=\"font-size: medium;\">&ldquo;肝 功能&rdquo; &nbsp;&ldquo;</span><span style=\"font-size: medium;\">胰腺 功能&rdquo; &ldquo;肝功&rdquo; &ldquo;肾功&rdquo; &nbsp;如何统一标注。</span></p>'),(47,'CH-EHR36000/1/file0.txt','',1,1,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(48,'CH-EHR36000/1/file1.txt','',1,1,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(49,'CH-EHR36000/1/file2.txt','',1,1,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(50,'CH-EHR36000/1/file3.txt','',1,1,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(51,'CH-EHR36000/1/file4.txt','',1,1,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(52,'CH-EHR36000/1/file5.txt','',13,2,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(53,'CH-EHR36000/1/file6.txt','',1,1,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(54,'CH-EHR36000/1/file7.txt','',1,1,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(55,'CH-EHR36000/1/file8.txt','',1,1,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(56,'CH-EHR36000/1/file9.txt','',1,1,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。',''),(57,'CH-EHR36000/1/file15.txt','',13,2,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。'),(58,'CH-EHR36000/1/file27.txt','',13,2,1,1,1,1,'请在此处留下评论。有任何不确定的疑问也请在此处留下。','请在此处留下评论。有任何不确定的疑问也请在此处留下。');
/*!40000 ALTER TABLE `editor_textfile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-11 22:09:30
