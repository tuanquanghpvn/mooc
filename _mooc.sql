-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mooc
-- ------------------------------------------------------
-- Server version	5.5.44-0ubuntu0.14.04.1

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
-- Table structure for table `account_emailaddress`
--

DROP TABLE IF EXISTS `account_emailaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_emailaddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `account_emailaddress_e8701ad4` (`user_id`),
  CONSTRAINT `account_emailaddress_user_id_704a3566e16b7299_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailaddress`
--

LOCK TABLES `account_emailaddress` WRITE;
/*!40000 ALTER TABLE `account_emailaddress` DISABLE KEYS */;
INSERT INTO `account_emailaddress` VALUES (3,'tuanquanghpvn@outlook.com',0,1,22);
/*!40000 ALTER TABLE `account_emailaddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_emailconfirmation`
--

DROP TABLE IF EXISTS `account_emailconfirmation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_emailconfirmation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime NOT NULL,
  `sent` datetime DEFAULT NULL,
  `key` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `email_address_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`),
  KEY `account_emailconfirmation_6f1edeac` (`email_address_id`),
  CONSTRAINT `acc_email_address_id_42ba4bbbc55b76bb_fk_account_emailaddress_id` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailconfirmation`
--

LOCK TABLES `account_emailconfirmation` WRITE;
/*!40000 ALTER TABLE `account_emailconfirmation` DISABLE KEYS */;
INSERT INTO `account_emailconfirmation` VALUES (3,'2015-11-18 07:27:11',NULL,'7biwzmovzrp8revxpdwk7ozav6ll9gtqxm8kznllichp6gz2g0mxiv0waplufxsj',3);
/*!40000 ALTER TABLE `account_emailconfirmation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_3a56c4fa42ce3121_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_63b53040f9bc685d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_3a56c4fa42ce3121_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_p_content_type_id_64c4d48ce26b820_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user profile',7,'add_userprofile'),(20,'Can change user profile',7,'change_userprofile'),(21,'Can delete user profile',7,'delete_userprofile'),(22,'Can add teacher',8,'add_teacher'),(23,'Can change teacher',8,'change_teacher'),(24,'Can delete teacher',8,'delete_teacher'),(25,'Can add student',9,'add_student'),(26,'Can change student',9,'change_student'),(27,'Can delete student',9,'delete_student'),(28,'Can add course',10,'add_course'),(29,'Can change course',10,'change_course'),(30,'Can delete course',10,'delete_course'),(31,'Can add teacher course',11,'add_teachercourse'),(32,'Can change teacher course',11,'change_teachercourse'),(33,'Can delete teacher course',11,'delete_teachercourse'),(34,'Can add category',12,'add_category'),(35,'Can change category',12,'change_category'),(36,'Can delete category',12,'delete_category'),(37,'Can add Blog',13,'add_blog'),(38,'Can change Blog',13,'change_blog'),(39,'Can delete Blog',13,'delete_blog'),(40,'Can add Subject',14,'add_subject'),(41,'Can change Subject',14,'change_subject'),(42,'Can delete Subject',14,'delete_subject'),(43,'Can add Session',15,'add_session'),(44,'Can change Session',15,'change_session'),(45,'Can delete Session',15,'delete_session'),(46,'Can add Task',16,'add_task'),(47,'Can change Task',16,'change_task'),(48,'Can delete Task',16,'delete_task'),(52,'Can add Review',18,'add_review'),(53,'Can change Review',18,'change_review'),(54,'Can delete Review',18,'delete_review'),(55,'Can add Enroll',19,'add_enroll'),(56,'Can change Enroll',19,'change_enroll'),(57,'Can delete Enroll',19,'delete_enroll'),(58,'Can add Comment',20,'add_comment'),(59,'Can change Comment',20,'change_comment'),(60,'Can delete Comment',20,'delete_comment'),(61,'Can add site',21,'add_site'),(62,'Can change site',21,'change_site'),(63,'Can delete site',21,'delete_site'),(64,'Can add email address',22,'add_emailaddress'),(65,'Can change email address',22,'change_emailaddress'),(66,'Can delete email address',22,'delete_emailaddress'),(67,'Can add email confirmation',23,'add_emailconfirmation'),(68,'Can change email confirmation',23,'change_emailconfirmation'),(69,'Can delete email confirmation',23,'delete_emailconfirmation'),(70,'Can add social application',24,'add_socialapp'),(71,'Can change social application',24,'change_socialapp'),(72,'Can delete social application',24,'delete_socialapp'),(73,'Can add social account',25,'add_socialaccount'),(74,'Can change social account',25,'change_socialaccount'),(75,'Can delete social account',25,'delete_socialaccount'),(76,'Can add social application token',26,'add_socialtoken'),(77,'Can change social application token',26,'change_socialtoken'),(78,'Can delete social application token',26,'delete_socialtoken');
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
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$54PTYXhhiGFN$YN0MF77T2UOrhX6v3GXDuTrEgwcC8xTjSYjptnHs7o4=','2015-11-18 07:24:20',1,'admin','','','admin@admin.com',1,1,'2015-10-27 02:28:37'),(2,'pbkdf2_sha256$20000$54PTYXhhiGFN$YN0MF77T2UOrhX6v3GXDuTrEgwcC8xTjSYjptnHs7o4=','2015-11-18 01:23:24',0,'teacher01','','','',1,1,'0000-00-00 00:00:00'),(4,'pbkdf2_sha256$20000$jPHvpd8FYi1h$qfYoQmAsPqozxyiXldjfSmcM31nTJpEh0XxXaBFhol8=','2015-11-18 04:12:12',0,'student01','','','',0,1,'2015-10-28 09:35:35'),(19,'pbkdf2_sha256$20000$JZhaiSvz0FfC$awhDv649eII8xiJFf6Zz2yrGmB1rfld7qcv9MRABN1Y=','2015-10-30 02:02:05',0,'teacher03','','','',1,1,'2015-10-30 02:01:57'),(22,'!kribdqjdx3O3BzyW987uX58yjaFUMuCbXGFrcmaU','2015-11-18 07:28:33',0,'quang','Quang','Trương Tuấn','tuanquanghpvn@outlook.com',0,1,'2015-11-18 07:27:10');
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
  KEY `auth_user_groups_group_id_4f3a74679ee9a531_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_4f3a74679ee9a531_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_57bacfa661183e20_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_738cf764cb3d55e7_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7ba4a5baaaf2596e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_738cf764cb3d55e7_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_date` datetime NOT NULL,
  `modified_date` datetime NOT NULL,
  `title` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content` longtext COLLATE utf8_unicode_ci NOT NULL,
  `status` smallint(6) NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_2dbcba41` (`slug`),
  KEY `blog_d9614d40` (`teacher_id`),
  CONSTRAINT `blog_teacher_id_1771c3debd251e7b_fk_teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (2,'2015-10-27 09:04:10','2015-10-27 09:04:10','Morbi nec quam sed elit pharetra','morbi-nec-quam-sed-elit-pharetra','Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus erat ligula, condimentum quis congue posuere, posuere id nisi. Pellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis ligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi commodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. Proin sagittis nibh lectus, lobortis ultrices.','<p>Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus\r\n erat ligula, condimentum quis congue posuere, posuere id nisi. \r\nPellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae\r\n ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis \r\nligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi \r\ncommodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. \r\nProin sagittis nibh lectus, lobortis ultrices.</p><p></p><blockquote>Etiam est sem, aliquam a congue id, porttitor et massa. Sed velit \r\nmauris, viverra non mi sit amet, tempor semper turpis. Etiam tempus \r\nporttitor pharetra. Mauris a aliquam nisl. Duis dignissim velit purus, \r\nquis rhoncus nisl fringilla id. Phasellus consectetur facilisis ex, ac \r\ninterdum ipsum consequat in. Vestibulum ante ipsum primis in faucibus \r\norci luctus et ultrices posuere cubilia Curae. Vestibulum ante ipsum \r\nprimis in faucibus orci luctus et ultrices posuere cubilia Curae. Donec \r\ntincidunt in ipsum ut molestie.</blockquote><p></p><p>Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur \r\neu leo elit. Aliquam dapibus porta tellus, dictum sodales turpis \r\nultricies ac. Cras mattis erat sit amet porttitor vehicula. Vivamus \r\nultrices sem nulla, eget sagittis eros pulvinar at. Proin pretium \r\nconvallis magna dapibus iaculis. Nunc nisl mauris, commodo in eleifend \r\nin, commodo id mauris. Suspendisse efficitur vel odio viverra \r\nscelerisque. Praesent tempus tincidunt magna vitae volutpat. Mauris id \r\nrutrum felis. Nulla facilisi. Quisque et nunc interdum, faucibus diam \r\neget, sodales nunc. Vivamus eu velit et neque consequat congue.<br></p>',1,'blog/blog-article.jpg',2),(3,'2015-10-27 09:04:10','2015-10-28 01:54:53','Morbi nec quam sed elit pharetra 2','morbi-nec-quam-sed-elit-pharetra-2','Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus erat ligula, condimentum quis congue posuere, posuere id nisi. Pellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis ligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi commodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. Proin sagittis nibh lectus, lobortis ultrices.','<p>Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus\r\n erat ligula, condimentum quis congue posuere, posuere id nisi. \r\nPellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae\r\n ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis \r\nligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi \r\ncommodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. \r\nProin sagittis nibh lectus, lobortis ultrices.</p><p></p><blockquote>Etiam est sem, aliquam a congue id, porttitor et massa. Sed velit \r\nmauris, viverra non mi sit amet, tempor semper turpis. Etiam tempus \r\nporttitor pharetra. Mauris a aliquam nisl. Duis dignissim velit purus, \r\nquis rhoncus nisl fringilla id. Phasellus consectetur facilisis ex, ac \r\ninterdum ipsum consequat in. Vestibulum ante ipsum primis in faucibus \r\norci luctus et ultrices posuere cubilia Curae. Vestibulum ante ipsum \r\nprimis in faucibus orci luctus et ultrices posuere cubilia Curae. Donec \r\ntincidunt in ipsum ut molestie.</blockquote><p></p><p>Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur \r\neu leo elit. Aliquam dapibus porta tellus, dictum sodales turpis \r\nultricies ac. Cras mattis erat sit amet porttitor vehicula. Vivamus \r\nultrices sem nulla, eget sagittis eros pulvinar at. Proin pretium \r\nconvallis magna dapibus iaculis. Nunc nisl mauris, commodo in eleifend \r\nin, commodo id mauris. Suspendisse efficitur vel odio viverra \r\nscelerisque. Praesent tempus tincidunt magna vitae volutpat. Mauris id \r\nrutrum felis. Nulla facilisi. Quisque et nunc interdum, faucibus diam \r\neget, sodales nunc. Vivamus eu velit et neque consequat congue.<br></p>',1,'blog/image12.jpg',2),(4,'2015-10-27 09:04:10','2015-10-28 01:58:00','Morbi nec quam sed elit pharetra 3','morbi-nec-quam-sed-elit-pharetra-3','Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus erat ligula, condimentum quis congue posuere, posuere id nisi. Pellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis ligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi commodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. Proin sagittis nibh lectus, lobortis ultrices.','<p>Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus\r\n erat ligula, condimentum quis congue posuere, posuere id nisi. \r\nPellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae\r\n ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis \r\nligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi \r\ncommodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. \r\nProin sagittis nibh lectus, lobortis ultrices.</p><p></p><blockquote>Etiam est sem, aliquam a congue id, porttitor et massa. Sed velit \r\nmauris, viverra non mi sit amet, tempor semper turpis. Etiam tempus \r\nporttitor pharetra. Mauris a aliquam nisl. Duis dignissim velit purus, \r\nquis rhoncus nisl fringilla id. Phasellus consectetur facilisis ex, ac \r\ninterdum ipsum consequat in. Vestibulum ante ipsum primis in faucibus \r\norci luctus et ultrices posuere cubilia Curae. Vestibulum ante ipsum \r\nprimis in faucibus orci luctus et ultrices posuere cubilia Curae. Donec \r\ntincidunt in ipsum ut molestie.</blockquote><p></p><p>Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur \r\neu leo elit. Aliquam dapibus porta tellus, dictum sodales turpis \r\nultricies ac. Cras mattis erat sit amet porttitor vehicula. Vivamus \r\nultrices sem nulla, eget sagittis eros pulvinar at. Proin pretium \r\nconvallis magna dapibus iaculis. Nunc nisl mauris, commodo in eleifend \r\nin, commodo id mauris. Suspendisse efficitur vel odio viverra \r\nscelerisque. Praesent tempus tincidunt magna vitae volutpat. Mauris id \r\nrutrum felis. Nulla facilisi. Quisque et nunc interdum, faucibus diam \r\neget, sodales nunc. Vivamus eu velit et neque consequat congue.<br></p>',1,'blog/1389121022775.jpg',2),(5,'2015-10-27 09:04:10','2015-10-28 01:58:36','Morbi nec quam sed elit pharetra 4','morbi-nec-quam-sed-elit-pharetra-4','Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus erat ligula, condimentum quis congue posuere, posuere id nisi. Pellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis ligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi commodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. Proin sagittis nibh lectus, lobortis ultrices.','<p>Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus\r\n erat ligula, condimentum quis congue posuere, posuere id nisi. \r\nPellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae\r\n ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis \r\nligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi \r\ncommodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. \r\nProin sagittis nibh lectus, lobortis ultrices.</p><p></p><blockquote>Etiam est sem, aliquam a congue id, porttitor et massa. Sed velit \r\nmauris, viverra non mi sit amet, tempor semper turpis. Etiam tempus \r\nporttitor pharetra. Mauris a aliquam nisl. Duis dignissim velit purus, \r\nquis rhoncus nisl fringilla id. Phasellus consectetur facilisis ex, ac \r\ninterdum ipsum consequat in. Vestibulum ante ipsum primis in faucibus \r\norci luctus et ultrices posuere cubilia Curae. Vestibulum ante ipsum \r\nprimis in faucibus orci luctus et ultrices posuere cubilia Curae. Donec \r\ntincidunt in ipsum ut molestie.</blockquote><p></p><p>Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur \r\neu leo elit. Aliquam dapibus porta tellus, dictum sodales turpis \r\nultricies ac. Cras mattis erat sit amet porttitor vehicula. Vivamus \r\nultrices sem nulla, eget sagittis eros pulvinar at. Proin pretium \r\nconvallis magna dapibus iaculis. Nunc nisl mauris, commodo in eleifend \r\nin, commodo id mauris. Suspendisse efficitur vel odio viverra \r\nscelerisque. Praesent tempus tincidunt magna vitae volutpat. Mauris id \r\nrutrum felis. Nulla facilisi. Quisque et nunc interdum, faucibus diam \r\neget, sodales nunc. Vivamus eu velit et neque consequat congue.<br></p>',1,'blog/teacher_apple120118.jpg',2),(6,'2015-10-27 09:04:10','2015-10-28 01:59:27','Morbi nec quam sed elit pharetra 5','morbi-nec-quam-sed-elit-pharetra-5','Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus erat ligula, condimentum quis congue posuere, posuere id nisi. Pellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis ligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi commodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. Proin sagittis nibh lectus, lobortis ultrices.','<p>Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus\r\n erat ligula, condimentum quis congue posuere, posuere id nisi. \r\nPellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae\r\n ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis \r\nligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi \r\ncommodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. \r\nProin sagittis nibh lectus, lobortis ultrices.</p><p></p><blockquote>Etiam est sem, aliquam a congue id, porttitor et massa. Sed velit \r\nmauris, viverra non mi sit amet, tempor semper turpis. Etiam tempus \r\nporttitor pharetra. Mauris a aliquam nisl. Duis dignissim velit purus, \r\nquis rhoncus nisl fringilla id. Phasellus consectetur facilisis ex, ac \r\ninterdum ipsum consequat in. Vestibulum ante ipsum primis in faucibus \r\norci luctus et ultrices posuere cubilia Curae. Vestibulum ante ipsum \r\nprimis in faucibus orci luctus et ultrices posuere cubilia Curae. Donec \r\ntincidunt in ipsum ut molestie.</blockquote><p></p><p>Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur \r\neu leo elit. Aliquam dapibus porta tellus, dictum sodales turpis \r\nultricies ac. Cras mattis erat sit amet porttitor vehicula. Vivamus \r\nultrices sem nulla, eget sagittis eros pulvinar at. Proin pretium \r\nconvallis magna dapibus iaculis. Nunc nisl mauris, commodo in eleifend \r\nin, commodo id mauris. Suspendisse efficitur vel odio viverra \r\nscelerisque. Praesent tempus tincidunt magna vitae volutpat. Mauris id \r\nrutrum felis. Nulla facilisi. Quisque et nunc interdum, faucibus diam \r\neget, sodales nunc. Vivamus eu velit et neque consequat congue.<br></p>',1,'blog/English-Teacher1.jpg',2),(7,'2015-10-27 09:04:10','2015-10-28 02:00:02','Morbi nec quam sed elit pharetra 6','morbi-nec-quam-sed-elit-pharetra-6','Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus erat ligula, condimentum quis congue posuere, posuere id nisi. Pellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis ligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi commodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. Proin sagittis nibh lectus, lobortis ultrices.','<p>Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus\r\n erat ligula, condimentum quis congue posuere, posuere id nisi. \r\nPellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae\r\n ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis \r\nligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi \r\ncommodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. \r\nProin sagittis nibh lectus, lobortis ultrices.</p><p></p><blockquote>Etiam est sem, aliquam a congue id, porttitor et massa. Sed velit \r\nmauris, viverra non mi sit amet, tempor semper turpis. Etiam tempus \r\nporttitor pharetra. Mauris a aliquam nisl. Duis dignissim velit purus, \r\nquis rhoncus nisl fringilla id. Phasellus consectetur facilisis ex, ac \r\ninterdum ipsum consequat in. Vestibulum ante ipsum primis in faucibus \r\norci luctus et ultrices posuere cubilia Curae. Vestibulum ante ipsum \r\nprimis in faucibus orci luctus et ultrices posuere cubilia Curae. Donec \r\ntincidunt in ipsum ut molestie.</blockquote><p></p><p>Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur \r\neu leo elit. Aliquam dapibus porta tellus, dictum sodales turpis \r\nultricies ac. Cras mattis erat sit amet porttitor vehicula. Vivamus \r\nultrices sem nulla, eget sagittis eros pulvinar at. Proin pretium \r\nconvallis magna dapibus iaculis. Nunc nisl mauris, commodo in eleifend \r\nin, commodo id mauris. Suspendisse efficitur vel odio viverra \r\nscelerisque. Praesent tempus tincidunt magna vitae volutpat. Mauris id \r\nrutrum felis. Nulla facilisi. Quisque et nunc interdum, faucibus diam \r\neget, sodales nunc. Vivamus eu velit et neque consequat congue.<br></p>',1,'blog/2014_09_26_TeacherNzltr.jpg',2),(8,'2015-10-27 09:04:10','2015-10-28 02:00:44','Morbi nec quam sed elit pharetra 7','morbi-nec-quam-sed-elit-pharetra-7','Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus erat ligula, condimentum quis congue posuere, posuere id nisi. Pellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis ligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi commodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. Proin sagittis nibh lectus, lobortis ultrices.','<p>Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus\r\n erat ligula, condimentum quis congue posuere, posuere id nisi. \r\nPellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae\r\n ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis \r\nligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi \r\ncommodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. \r\nProin sagittis nibh lectus, lobortis ultrices.</p><p></p><blockquote>Etiam est sem, aliquam a congue id, porttitor et massa. Sed velit \r\nmauris, viverra non mi sit amet, tempor semper turpis. Etiam tempus \r\nporttitor pharetra. Mauris a aliquam nisl. Duis dignissim velit purus, \r\nquis rhoncus nisl fringilla id. Phasellus consectetur facilisis ex, ac \r\ninterdum ipsum consequat in. Vestibulum ante ipsum primis in faucibus \r\norci luctus et ultrices posuere cubilia Curae. Vestibulum ante ipsum \r\nprimis in faucibus orci luctus et ultrices posuere cubilia Curae. Donec \r\ntincidunt in ipsum ut molestie.</blockquote><p></p><p>Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur \r\neu leo elit. Aliquam dapibus porta tellus, dictum sodales turpis \r\nultricies ac. Cras mattis erat sit amet porttitor vehicula. Vivamus \r\nultrices sem nulla, eget sagittis eros pulvinar at. Proin pretium \r\nconvallis magna dapibus iaculis. Nunc nisl mauris, commodo in eleifend \r\nin, commodo id mauris. Suspendisse efficitur vel odio viverra \r\nscelerisque. Praesent tempus tincidunt magna vitae volutpat. Mauris id \r\nrutrum felis. Nulla facilisi. Quisque et nunc interdum, faucibus diam \r\neget, sodales nunc. Vivamus eu velit et neque consequat congue.<br></p>',1,'blog/alternative-teaching-certification.jpg',2),(9,'2015-10-27 09:04:10','2015-10-28 02:01:16','Morbi nec quam sed elit pharetra 8','morbi-nec-quam-sed-elit-pharetra-8','Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus erat ligula, condimentum quis congue posuere, posuere id nisi. Pellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis ligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi commodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. Proin sagittis nibh lectus, lobortis ultrices.','<p>Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus\r\n erat ligula, condimentum quis congue posuere, posuere id nisi. \r\nPellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae\r\n ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis \r\nligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi \r\ncommodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. \r\nProin sagittis nibh lectus, lobortis ultrices.</p><p></p><blockquote>Etiam est sem, aliquam a congue id, porttitor et massa. Sed velit \r\nmauris, viverra non mi sit amet, tempor semper turpis. Etiam tempus \r\nporttitor pharetra. Mauris a aliquam nisl. Duis dignissim velit purus, \r\nquis rhoncus nisl fringilla id. Phasellus consectetur facilisis ex, ac \r\ninterdum ipsum consequat in. Vestibulum ante ipsum primis in faucibus \r\norci luctus et ultrices posuere cubilia Curae. Vestibulum ante ipsum \r\nprimis in faucibus orci luctus et ultrices posuere cubilia Curae. Donec \r\ntincidunt in ipsum ut molestie.</blockquote><p></p><p>Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur \r\neu leo elit. Aliquam dapibus porta tellus, dictum sodales turpis \r\nultricies ac. Cras mattis erat sit amet porttitor vehicula. Vivamus \r\nultrices sem nulla, eget sagittis eros pulvinar at. Proin pretium \r\nconvallis magna dapibus iaculis. Nunc nisl mauris, commodo in eleifend \r\nin, commodo id mauris. Suspendisse efficitur vel odio viverra \r\nscelerisque. Praesent tempus tincidunt magna vitae volutpat. Mauris id \r\nrutrum felis. Nulla facilisi. Quisque et nunc interdum, faucibus diam \r\neget, sodales nunc. Vivamus eu velit et neque consequat congue.<br></p>',1,'blog/what_to_do_when_you_or_your_child_dont_get_along_with_the_teacher.jpg',2),(10,'2015-10-27 09:04:10','2015-10-28 02:03:27','Morbi nec quam sed elit pharetra 9','morbi-nec-quam-sed-elit-pharetra-9','Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus erat ligula, condimentum quis congue posuere, posuere id nisi. Pellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis ligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi commodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. Proin sagittis nibh lectus, lobortis ultrices.','<p>Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus\r\n erat ligula, condimentum quis congue posuere, posuere id nisi. \r\nPellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae\r\n ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis \r\nligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi \r\ncommodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. \r\nProin sagittis nibh lectus, lobortis ultrices.</p><p></p><blockquote>Etiam est sem, aliquam a congue id, porttitor et massa. Sed velit \r\nmauris, viverra non mi sit amet, tempor semper turpis. Etiam tempus \r\nporttitor pharetra. Mauris a aliquam nisl. Duis dignissim velit purus, \r\nquis rhoncus nisl fringilla id. Phasellus consectetur facilisis ex, ac \r\ninterdum ipsum consequat in. Vestibulum ante ipsum primis in faucibus \r\norci luctus et ultrices posuere cubilia Curae. Vestibulum ante ipsum \r\nprimis in faucibus orci luctus et ultrices posuere cubilia Curae. Donec \r\ntincidunt in ipsum ut molestie.</blockquote><p></p><p>Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur \r\neu leo elit. Aliquam dapibus porta tellus, dictum sodales turpis \r\nultricies ac. Cras mattis erat sit amet porttitor vehicula. Vivamus \r\nultrices sem nulla, eget sagittis eros pulvinar at. Proin pretium \r\nconvallis magna dapibus iaculis. Nunc nisl mauris, commodo in eleifend \r\nin, commodo id mauris. Suspendisse efficitur vel odio viverra \r\nscelerisque. Praesent tempus tincidunt magna vitae volutpat. Mauris id \r\nrutrum felis. Nulla facilisi. Quisque et nunc interdum, faucibus diam \r\neget, sodales nunc. Vivamus eu velit et neque consequat congue.<br></p>',1,'blog/1389121022775_Yk6aFO9.jpg',2),(11,'2015-10-27 09:04:10','2015-10-28 02:03:38','Morbi nec quam sed elit pharetra 10','morbi-nec-quam-sed-elit-pharetra-10','Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus erat ligula, condimentum quis congue posuere, posuere id nisi. Pellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis ligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi commodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. Proin sagittis nibh lectus, lobortis ultrices.','<p>Praesent dui diam, vestibulum id mi at, iaculis accumsan ligula. Vivamus\r\n erat ligula, condimentum quis congue posuere, posuere id nisi. \r\nPellentesque tempor sit amet arcu in mattis. Nullam congue, lectus vitae\r\n ultrices interdum, augue nibh lacinia ante, et tempus arcu tellus quis \r\nligula. Aliquam congue ex vitae turpis fermentum, ac tempor nisi \r\ncommodo. Ut ante turpis, pulvinar eu arcu eu, blandit blandit sapien. \r\nProin sagittis nibh lectus, lobortis ultrices.</p><p></p><blockquote>Etiam est sem, aliquam a congue id, porttitor et massa. Sed velit \r\nmauris, viverra non mi sit amet, tempor semper turpis. Etiam tempus \r\nporttitor pharetra. Mauris a aliquam nisl. Duis dignissim velit purus, \r\nquis rhoncus nisl fringilla id. Phasellus consectetur facilisis ex, ac \r\ninterdum ipsum consequat in. Vestibulum ante ipsum primis in faucibus \r\norci luctus et ultrices posuere cubilia Curae. Vestibulum ante ipsum \r\nprimis in faucibus orci luctus et ultrices posuere cubilia Curae. Donec \r\ntincidunt in ipsum ut molestie.</blockquote><p></p><p>Interdum et malesuada fames ac ante ipsum primis in faucibus. Curabitur \r\neu leo elit. Aliquam dapibus porta tellus, dictum sodales turpis \r\nultricies ac. Cras mattis erat sit amet porttitor vehicula. Vivamus \r\nultrices sem nulla, eget sagittis eros pulvinar at. Proin pretium \r\nconvallis magna dapibus iaculis. Nunc nisl mauris, commodo in eleifend \r\nin, commodo id mauris. Suspendisse efficitur vel odio viverra \r\nscelerisque. Praesent tempus tincidunt magna vitae volutpat. Mauris id \r\nrutrum felis. Nulla facilisi. Quisque et nunc interdum, faucibus diam \r\neget, sodales nunc. Vivamus eu velit et neque consequat congue.<br></p>',1,'blog/blog-article.jpg',2);
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_date` datetime NOT NULL,
  `modified_date` datetime NOT NULL,
  `name` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'2015-10-27 02:35:04','2015-10-27 02:35:04','Software Development','Software Development'),(2,'2015-10-28 02:08:06','2015-10-28 02:08:06','Business','Business'),(3,'2015-10-28 02:08:20','2015-10-28 02:08:20','Arts and Humanities','Arts and Humanities'),(4,'2015-10-28 02:08:35','2015-10-28 02:08:35','Computer Science','Computer Science'),(5,'2015-10-28 02:09:11','2015-10-28 02:09:11','Math and Logic','Math and Logic'),(6,'2015-10-28 02:09:28','2015-10-28 02:09:28','Social Sciences','Social Sciences');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category_subject`
--

DROP TABLE IF EXISTS `category_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category_subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `subject_id` (`subject_id`,`category_id`),
  KEY `category_subject_category_id_5479f087f9493d83_fk_category_id` (`category_id`),
  CONSTRAINT `category_subject_category_id_5479f087f9493d83_fk_category_id` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  CONSTRAINT `category_subject_subject_id_657e74bf7629c161_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category_subject`
--

LOCK TABLES `category_subject` WRITE;
/*!40000 ALTER TABLE `category_subject` DISABLE KEYS */;
INSERT INTO `category_subject` VALUES (3,3,1),(4,4,1),(5,5,2),(6,6,3),(7,7,5),(8,8,6);
/*!40000 ALTER TABLE `category_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `create_date` datetime NOT NULL,
  `content` longtext COLLATE utf8_unicode_ci NOT NULL,
  `blog_id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comment_profile_id_1dd8bbd0ea6ea541_fk_core_userprofile_user_id` (`profile_id`),
  KEY `comment_blog_id_6eddaeff598adbf7_fk_blog_id` (`blog_id`),
  CONSTRAINT `comment_blog_id_6eddaeff598adbf7_fk_blog_id` FOREIGN KEY (`blog_id`) REFERENCES `blog` (`id`),
  CONSTRAINT `comment_profile_id_1dd8bbd0ea6ea541_fk_core_userprofile_user_id` FOREIGN KEY (`profile_id`) REFERENCES `user_profile` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,'2015-10-28 06:15:38','gfdgfdgfdgfdgfdgfdgfd',11,2),(2,'2015-10-28 06:16:41','fdsfdsfds fds fds fds',11,2),(3,'2015-10-28 06:17:33','fdsfdsfds fds fds fdsgfdgfd gfdg gfd',11,2);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_date` datetime NOT NULL,
  `modified_date` datetime NOT NULL,
  `name` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (3,'2015-10-28 02:32:57','2015-10-28 02:32:57','Creative Website Design and Development','Creative Website Design and Development');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_76f3accda71110b0_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_503adeee1c908422_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_503adeee1c908422_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_76f3accda71110b0_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_46c102fe18658bea_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (22,'account','emailaddress'),(23,'account','emailconfirmation'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(13,'blog','blog'),(12,'categories','category'),(20,'comments','comment'),(5,'contenttypes','contenttype'),(7,'core','userprofile'),(10,'courses','course'),(11,'courses','teachercourse'),(18,'reviews','review'),(6,'sessions','session'),(21,'sites','site'),(25,'socialaccount','socialaccount'),(24,'socialaccount','socialapp'),(26,'socialaccount','socialtoken'),(9,'students','student'),(19,'subjects','enroll'),(15,'subjects','session'),(14,'subjects','subject'),(16,'subjects','task'),(8,'teachers','teacher');
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
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-10-27 02:25:05'),(2,'auth','0001_initial','2015-10-27 02:25:07'),(3,'admin','0001_initial','2015-10-27 02:25:08'),(4,'contenttypes','0002_remove_content_type_name','2015-10-27 02:25:08'),(5,'auth','0002_alter_permission_name_max_length','2015-10-27 02:25:08'),(6,'auth','0003_alter_user_email_max_length','2015-10-27 02:25:09'),(7,'auth','0004_alter_user_username_opts','2015-10-27 02:25:09'),(8,'auth','0005_alter_user_last_login_null','2015-10-27 02:25:09'),(9,'auth','0006_require_contenttypes_0002','2015-10-27 02:25:09'),(10,'core','0001_initial','2015-10-27 02:25:10'),(11,'teachers','0001_initial','2015-10-27 02:25:10'),(12,'blog','0001_initial','2015-10-27 02:25:10'),(13,'blog','0002_blog_teacher','2015-10-27 02:25:11'),(14,'categories','0001_initial','2015-10-27 02:25:11'),(15,'courses','0001_initial','2015-10-27 02:25:12'),(16,'students','0001_initial','2015-10-27 02:25:13'),(17,'subjects','0001_initial','2015-10-27 02:25:17'),(18,'reviews','0001_initial','2015-10-27 02:25:18'),(19,'sessions','0001_initial','2015-10-27 02:25:18'),(20,'subjects','0002_auto_20151027_0905','2015-10-28 00:48:11'),(21,'subjects','0003_auto_20151027_0922','2015-10-28 00:48:11'),(23,'comments','0001_initial','2015-10-28 04:31:41'),(24,'reviews','0002_auto_20151028_0539','2015-10-28 06:54:30'),(25,'subjects','0004_auto_20151028_0626','2015-10-28 06:54:31'),(26,'blog','0003_auto_20151028_0842','2015-10-28 08:42:17'),(27,'subjects','0005_auto_20151028_0845','2015-10-28 08:45:56'),(28,'subjects','0006_auto_20151028_0847','2015-10-28 08:47:03'),(29,'comments','0002_auto_20151028_0921','2015-10-29 01:02:38'),(30,'subjects','0007_auto_20151028_0921','2015-10-29 01:02:38'),(31,'subjects','0008_auto_20151118_0224','2015-11-18 02:25:06'),(32,'subjects','0009_remove_task_image','2015-11-18 02:46:00'),(33,'account','0001_initial','2015-11-18 04:34:11'),(34,'account','0002_email_max_length','2015-11-18 04:34:12'),(35,'sites','0001_initial','2015-11-18 04:34:12'),(36,'socialaccount','0001_initial','2015-11-18 04:34:15'),(37,'socialaccount','0002_token_max_lengths','2015-11-18 04:34:16'),(38,'core','0002_auto_20151118_0710','2015-11-18 07:10:30'),(39,'socialaccount','0003_auto_20151118_0710','2015-11-18 07:10:30'),(40,'core','0003_auto_20151118_0719','2015-11-18 07:20:00');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0jj57kr8tuax762ldql7q2gi77pawieq','MjQ2MTA2ZWQwNDE4Y2U2ZmZkMGVlMTIyNGMzOTI2ODFlZTM0ZmU1Nzp7Il9hdXRoX3VzZXJfaGFzaCI6IjlmMjRjOTRiZWVlZDBkOTM2YTYyOWY2OTE1Y2QxNTY2YWJjZmE2M2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2015-11-13 03:13:54'),('69nn08lhk7xxoosnjecg8dqumxv5oqwd','YzY5MTQxMGQ4NDNmMWNmODFmYjQzOTE2ZWMzZjExNzkxZjg5MjUyNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjlmMjRjOTRiZWVlZDBkOTM2YTYyOWY2OTE1Y2QxNTY2YWJjZmE2M2YiLCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-12-02 01:23:24'),('iabz5hohyjypdibgidvu89sia35sw4aq','MmM3ZTAzZWM0OTdkN2Y0ODAwMWFmMGU5ZDljODkxNmYzN2FjNzEwYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjU5M2EzOTBiZDU5MjRmOTNlNmFmYmM2MTUwMjNmZmI3NWMyY2RmZTYiLCJfYXV0aF91c2VyX2lkIjoiNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-12-02 04:12:12'),('nwnmdde2lgybciqq0vszyaxjpbjrbk3z','NGExNWEwNWYxYjA5ODc1MDJkMWUwZWY1ZDUyNjZlMDg1MTFkNzMzZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5ZjI0Yzk0YmVlZWQwZDkzNmE2MjlmNjkxNWNkMTU2NmFiY2ZhNjNmIn0=','2015-11-12 09:48:17'),('sglaf9q12dkdnnccpc3wyvgacxrj2rpt','MGRhNGI5ZWIxOGY4NGY0YmI1OGY2OWUxNTdiMWY2YjlkNDUwMjU0ZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjhkOWIyMDlhZDI5N2M1ZThlNWRjMTIzNjAwNjE4MzdlOTU0MTM4YmUiLCJfYXV0aF91c2VyX2lkIjoiMjIifQ==','2015-12-02 07:28:33'),('uwyl11jwr5sjzpbtb5fbgp614w0s4uuc','NThlOThjNjk1NDk0MWEzZGViNTMzZjlkMTI1ODFhMWI1ZjI4ODRjZDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1OTNhMzkwYmQ1OTI0ZjkzZTZhZmJjNjE1MDIzZmZiNzVjMmNkZmU2In0=','2015-11-11 09:35:42'),('zlmqt67j9dvwjoq1kwxyps735k1lrbzb','MzI2MjRiNDU0MjllOGM1YjRiODUwODI3ZTFhZjUzZTgzNjYwMjBmOTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOWYyNGM5NGJlZWVkMGQ5MzZhNjI5ZjY5MTVjZDE1NjZhYmNmYTYzZiIsIl9hdXRoX3VzZXJfaWQiOiIyIn0=','2015-11-13 02:08:24');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'localhost','TMS');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enroll`
--

DROP TABLE IF EXISTS `enroll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `enroll` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_date` datetime NOT NULL,
  `modified_date` datetime NOT NULL,
  `session_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `endroll_7fc8ef54` (`session_id`),
  KEY `endroll_30a811f6` (`student_id`),
  CONSTRAINT `endroll_student_id_6f23276bc48367a0_fk_student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`),
  CONSTRAINT `enroll_session_id_4b85794100691556_fk_session_id` FOREIGN KEY (`session_id`) REFERENCES `session` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enroll`
--

LOCK TABLES `enroll` WRITE;
/*!40000 ALTER TABLE `enroll` DISABLE KEYS */;
INSERT INTO `enroll` VALUES (1,'2015-10-28 09:35:49','2015-10-28 09:35:49',3,2),(2,'2015-10-29 01:17:52','2015-10-29 01:17:52',9,2),(3,'2015-11-18 07:28:05','2015-11-18 07:28:05',9,4);
/*!40000 ALTER TABLE `enroll` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_date` datetime NOT NULL,
  `modified_date` datetime NOT NULL,
  `rating` int(11) NOT NULL,
  `content` longtext COLLATE utf8_unicode_ci NOT NULL,
  `student_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `review_student_id_2b4948b6c3c30276_fk_student_id` (`student_id`),
  KEY `review_subject_id_3b051362cf7b1dc2_fk_subject_id` (`subject_id`),
  CONSTRAINT `review_student_id_2b4948b6c3c30276_fk_student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`),
  CONSTRAINT `review_subject_id_3b051362cf7b1dc2_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
INSERT INTO `review` VALUES (1,'2015-10-29 01:17:40','2015-10-29 01:17:40',4,'Good',2,8);
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `session` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `subject_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `session_ffaba1d1` (`subject_id`),
  CONSTRAINT `session_subject_id_171a0aece3902df4_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
INSERT INTO `session` VALUES (3,'2010-10-10 00:00:00','2011-11-11 00:00:00',3),(4,'2010-10-10 00:00:00','2011-11-11 00:00:00',4),(5,'2010-10-10 00:00:00','2011-11-11 00:00:00',5),(6,'2010-10-10 00:00:00','2011-11-11 00:00:00',6),(7,'2010-10-10 00:00:00','2011-11-11 00:00:00',7),(8,'2010-10-10 00:00:00','2011-11-11 00:00:00',8),(9,'2011-11-11 00:00:00','2012-12-12 00:00:00',8);
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialaccount`
--

DROP TABLE IF EXISTS `socialaccount_socialaccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `socialaccount_socialaccount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `uid` varchar(191) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  `extra_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialaccount_provider_5087dc4b946c1d82_uniq` (`provider`,`uid`),
  KEY `socialaccount_socialaccount_e8701ad4` (`user_id`),
  CONSTRAINT `socialaccount_socialacc_user_id_5dd3d95dcf67e35c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialaccount`
--

LOCK TABLES `socialaccount_socialaccount` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialaccount` DISABLE KEYS */;
INSERT INTO `socialaccount_socialaccount` VALUES (3,'facebook','565588333592957','2015-11-18 07:28:33','2015-11-18 07:27:11','{\"verified\": true, \"last_name\": \"Tr\\u01b0\\u01a1ng Tu\\u1ea5n\", \"link\": \"https://www.facebook.com/app_scoped_user_id/565588333592957/\", \"first_name\": \"Quang\", \"locale\": \"vi_VN\", \"gender\": \"male\", \"updated_time\": \"2015-11-08T14:15:22+0000\", \"email\": \"tuanquanghpvn@outlook.com\", \"id\": \"565588333592957\", \"timezone\": 7, \"name\": \"Tr\\u01b0\\u01a1ng Tu\\u1ea5n Quang\"}',22);
/*!40000 ALTER TABLE `socialaccount_socialaccount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialapp`
--

DROP TABLE IF EXISTS `socialaccount_socialapp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `socialaccount_socialapp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `client_id` varchar(191) COLLATE utf8_unicode_ci NOT NULL,
  `secret` varchar(191) COLLATE utf8_unicode_ci NOT NULL,
  `key` varchar(191) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialapp`
--

LOCK TABLES `socialaccount_socialapp` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialapp` DISABLE KEYS */;
INSERT INTO `socialaccount_socialapp` VALUES (1,'facebook','Course Bridge','110970232602883','71d093b5018ef201dc1af95cc8e639b2','');
/*!40000 ALTER TABLE `socialaccount_socialapp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialapp_sites`
--

DROP TABLE IF EXISTS `socialaccount_socialapp_sites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `socialaccount_socialapp_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `socialapp_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialapp_id` (`socialapp_id`,`site_id`),
  KEY `socialaccount_socialapp_sites_fe95b0a0` (`socialapp_id`),
  KEY `socialaccount_socialapp_sites_9365d6e7` (`site_id`),
  CONSTRAINT `socialaccount_sociala_site_id_6eb0f1715a879738_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`),
  CONSTRAINT `soci_socialapp_id_4ecdf51a7b1bb6f5_fk_socialaccount_socialapp_id` FOREIGN KEY (`socialapp_id`) REFERENCES `socialaccount_socialapp` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialapp_sites`
--

LOCK TABLES `socialaccount_socialapp_sites` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialapp_sites` DISABLE KEYS */;
INSERT INTO `socialaccount_socialapp_sites` VALUES (1,1,1);
/*!40000 ALTER TABLE `socialaccount_socialapp_sites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socialaccount_socialtoken`
--

DROP TABLE IF EXISTS `socialaccount_socialtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `socialaccount_socialtoken` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` longtext COLLATE utf8_unicode_ci NOT NULL,
  `token_secret` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expires_at` datetime DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `app_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `socialaccount_socialtoken_app_id_37c601a8e64fa9b_uniq` (`app_id`,`account_id`),
  KEY `socialaccount_socialtoken_8a089c2a` (`account_id`),
  KEY `socialaccount_socialtoken_f382adfe` (`app_id`),
  CONSTRAINT `socialacco_app_id_3cf30157caa67d98_fk_socialaccount_socialapp_id` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`),
  CONSTRAINT `soc_account_id_3f78a39a4a49a09_fk_socialaccount_socialaccount_id` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socialaccount_socialtoken`
--

LOCK TABLES `socialaccount_socialtoken` WRITE;
/*!40000 ALTER TABLE `socialaccount_socialtoken` DISABLE KEYS */;
INSERT INTO `socialaccount_socialtoken` VALUES (3,'CAABk7UVLgQMBAKqsHnD8c6xGdChpYR3WbV3ozHBUobpS6yAuZC0dqx20ZC4lszOBZCZAgv8mUVJtq0DkTNZAJx7J0B4vOErMCbXF1vGSmoVKPdShdmq2ctmX7Bj61NED1Dmcputm8zBRzTfwPBmgI85tJljHgY4jLXky6ZAm58tRzkYMSCRUDlZAuQkWfW6vV4CmDmZAxWZA5fAZDZD','',NULL,3,1);
/*!40000 ALTER TABLE `socialaccount_socialtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `profile_id` (`profile_id`),
  CONSTRAINT `student_profile_id_7105b0d709e4f9b_fk_core_userprofile_user_id` FOREIGN KEY (`profile_id`) REFERENCES `user_profile` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (2,4),(4,22);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_date` datetime NOT NULL,
  `modified_date` datetime NOT NULL,
  `name` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `image` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `subject_course_id_6864dc77de3a4eac_fk_course_id` (`course_id`),
  KEY `subject_2dbcba41` (`slug`),
  CONSTRAINT `subject_course_id_6864dc77de3a4eac_fk_course_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (3,'2015-10-28 02:34:00','2015-10-28 02:34:00','Donec porta nulla volutpat interdum porta','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sit amet pharetra nunc, non scelerisque ligula. Cras vel justo nulla. Vestibulum a sollicitudin metus, faucibus fermentum leo. Nulla ut purus vel nunc ultricies dignissim at at nunc. Vivamus tempor eget lorem non commodo.','donec-porta-nulla-volutpat-interdum-porta','subjects/course01.jpg',3),(4,'2015-10-28 02:36:07','2015-10-28 02:36:07',' Introducing to Digital Photography','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sit amet pharetra nunc, non scelerisque ligula. Cras vel justo nulla. Vestibulum a sollicitudin metus, faucibus fermentum leo. Nulla ut purus vel nunc ultricies dignissim at at nunc. Vivamus tempor eget lorem non commodo.','introducing-to-digital-photography','subjects/course02.jpg',3),(5,'2015-10-28 02:37:28','2015-10-28 02:37:28','Adobe Illustrator and Vector Design Basics','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sit amet pharetra nunc, non scelerisque ligula. Cras vel justo nulla. Vestibulum a sollicitudin metus, faucibus fermentum leo. Nulla ut purus vel nunc ultricies dignissim at at nunc. Vivamus tempor eget lorem non commodo.','adobe-illustrator-and-vector-design-basics','subjects/course03.jpg',3),(6,'2015-10-28 02:38:54','2015-10-28 02:38:54','Composition and Lighting Advanced Course','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sit amet pharetra nunc, non scelerisque ligula. Cras vel justo nulla. Vestibulum a sollicitudin metus, faucibus fermentum leo. Nulla ut purus vel nunc ultricies dignissim at at nunc. Vivamus tempor eget lorem non commodo.','composition-and-lighting-advanced-course','subjects/course04.jpg',3),(7,'2015-10-28 02:40:07','2015-10-28 02:40:07','Web Design and Development Premium Course','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sit amet pharetra nunc, non scelerisque ligula. Cras vel justo nulla. Vestibulum a sollicitudin metus, faucibus fermentum leo. Nulla ut purus vel nunc ultricies dignissim at at nunc. Vivamus tempor eget lorem non commodo.','web-design-and-development-premium-course','subjects/course05.jpg',3),(8,'2015-10-28 02:40:57','2015-10-28 02:40:57','Advanced Web Development Course','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sit amet pharetra nunc, non scelerisque ligula. Cras vel justo nulla. Vestibulum a sollicitudin metus, faucibus fermentum leo. Nulla ut purus vel nunc ultricies dignissim at at nunc. Vivamus tempor eget lorem non commodo.','advanced-web-development-course','subjects/course12.jpg',3);
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  `slug` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content` longtext COLLATE utf8_unicode_ci NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `session_id` int(11) NOT NULL,
  `link_youtube` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `task_2dbcba41` (`slug`),
  KEY `task_session_id_782ad7ecb109e8c7_fk_session_id` (`session_id`),
  CONSTRAINT `task_session_id_782ad7ecb109e8c7_fk_session_id` FOREIGN KEY (`session_id`) REFERENCES `session` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (16,'Task 1 - Python Core','','task-1-python-core','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.','2011-11-11 00:00:00','2011-12-12 00:00:00',9,'https://www.youtube.com/watch?v=D48iCw3WWpI');
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `profile_id` (`profile_id`),
  CONSTRAINT `teacher_profile_id_4aee3960f52fd2b6_fk_core_userprofile_user_id` FOREIGN KEY (`profile_id`) REFERENCES `user_profile` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (2,2),(12,19);
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_course`
--

DROP TABLE IF EXISTS `teacher_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_creator` tinyint(1) NOT NULL,
  `course_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_course_course_id_31c63f115679a8f_fk_course_id` (`course_id`),
  KEY `teacher_course_teacher_id_672e0213e582555a_fk_teacher_id` (`teacher_id`),
  CONSTRAINT `teacher_course_course_id_31c63f115679a8f_fk_course_id` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`),
  CONSTRAINT `teacher_course_teacher_id_672e0213e582555a_fk_teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_course`
--

LOCK TABLES `teacher_course` WRITE;
/*!40000 ALTER TABLE `teacher_course` DISABLE KEYS */;
INSERT INTO `teacher_course` VALUES (3,1,3,2);
/*!40000 ALTER TABLE `teacher_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_profile`
--

DROP TABLE IF EXISTS `user_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_profile` (
  `user_id` int(11) NOT NULL,
  `avatar` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `modified_date` datetime NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `core_userprofile_user_id_38d72d3b32c9b835_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profile`
--

LOCK TABLES `user_profile` WRITE;
/*!40000 ALTER TABLE `user_profile` DISABLE KEYS */;
INSERT INTO `user_profile` VALUES (1,'','0000-00-00 00:00:00'),(2,'','0000-00-00 00:00:00'),(4,'','2015-10-28 09:35:35'),(19,'','2015-10-30 02:01:57'),(22,'','2015-11-18 07:27:10');
/*!40000 ALTER TABLE `user_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-18 15:00:40
