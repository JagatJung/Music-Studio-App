SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE TABLE `artist` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `dob` datetime NOT NULL,
  `gender` enum('m','f','o') NOT NULL,
  `address` varchar(255) NOT NULL,
  `first_release_year` year(4) NOT NULL,
  `no_of_album_released` int(11) NOT NULL,
  `create_ts` datetime NOT NULL DEFAULT current_timestamp(),
  `update_ts` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `artist` VALUES(3, 'Mika singh', '1984-01-06 00:00:00', 'm', 'Delhi', '2002', 8, '2024-04-23 16:50:06', '2024-04-26 12:43:34');
INSERT INTO `artist` VALUES(4, 'Arijit Singh', '1987-04-25 00:00:00', 'm', 'Kolkata', '2010', 7, '2024-04-23 16:50:06', '2024-04-23 16:50:06');
INSERT INTO `artist` VALUES(5, 'Taylor Swift', '1989-12-13 00:00:00', 'f', 'Pennsylvania', '2006', 9, '2024-04-23 16:50:06', '2024-04-23 16:50:06');
INSERT INTO `artist` VALUES(6, 'Beyoncé', '1981-09-04 00:00:00', 'f', 'Houston', '1997', 8, '2024-04-23 16:50:06', '2024-04-23 16:50:06');
INSERT INTO `artist` VALUES(7, 'Ed Sheeran', '1991-02-17 00:00:00', 'm', 'Halifax', '2011', 6, '2024-04-23 16:50:06', '2024-04-23 16:50:06');
INSERT INTO `artist` VALUES(8, 'Rihanna', '1988-02-20 00:00:00', 'f', 'Saint Michael', '2005', 8, '2024-04-23 16:50:06', '2024-04-23 16:50:06');
INSERT INTO `artist` VALUES(9, 'Justin Bieber', '1994-03-01 00:00:00', 'm', 'London', '2009', 5, '2024-04-23 16:50:06', '2024-04-23 16:50:06');
INSERT INTO `artist` VALUES(10, 'Shakira', '1977-02-02 00:00:00', 'f', 'Barranquilla', '1990', 11, '2024-04-23 16:50:06', '2024-04-23 16:50:06');
INSERT INTO `artist` VALUES(11, 'Eminem', '1972-10-17 00:00:00', 'm', 'Detroit', '1996', 11, '2024-04-23 16:50:06', '2024-04-23 16:50:06');
INSERT INTO `artist` VALUES(12, 'Lady Gaga', '1986-03-28 00:00:00', 'f', 'New York City', '2008', 6, '2024-04-23 16:50:06', '2024-04-23 16:50:06');
INSERT INTO `artist` VALUES(20, 'hikmat', '2000-10-24 00:00:00', 'm', 'Hetauda', '2011', 5, '2024-04-26 22:15:19', '2024-04-26 22:15:19');
INSERT INTO `artist` VALUES(21, 'Balban', '1990-02-12 00:00:00', 'f', 'Mankamana', '2002', 7, '2024-04-26 22:15:19', '2024-04-26 22:15:19');
INSERT INTO `artist` VALUES(25, 'Hira', '2000-10-24 00:00:00', 'm', 'Hetauda', '2011', 50, '2024-04-26 22:24:55', '2024-04-26 22:24:55');
INSERT INTO `artist` VALUES(26, 'Melborn', '1990-02-12 00:00:00', 'o', 'Mankamana', '2002', 17, '2024-04-26 22:24:55', '2024-04-26 22:24:55');

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `auth_permission` VALUES(1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES(2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES(3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES(4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES(5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES(6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES(7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES(8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES(9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES(10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES(11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES(12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES(13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES(14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES(15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES(16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES(17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES(18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES(19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES(20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES(21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES(22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES(23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES(24, 'Can view session', 6, 'view_session');

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `django_content_type` VALUES(1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES(3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES(2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES(4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES(5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES(6, 'sessions', 'session');

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `django_migrations` VALUES(1, 'contenttypes', '0001_initial', '2024-04-18 16:32:28.840156');
INSERT INTO `django_migrations` VALUES(2, 'auth', '0001_initial', '2024-04-18 16:32:29.434277');
INSERT INTO `django_migrations` VALUES(3, 'admin', '0001_initial', '2024-04-18 16:32:29.609257');
INSERT INTO `django_migrations` VALUES(4, 'admin', '0002_logentry_remove_auto_add', '2024-04-18 16:32:29.626339');
INSERT INTO `django_migrations` VALUES(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-04-18 16:32:29.644657');
INSERT INTO `django_migrations` VALUES(6, 'contenttypes', '0002_remove_content_type_name', '2024-04-18 16:32:29.729990');
INSERT INTO `django_migrations` VALUES(7, 'auth', '0002_alter_permission_name_max_length', '2024-04-18 16:32:29.797711');
INSERT INTO `django_migrations` VALUES(8, 'auth', '0003_alter_user_email_max_length', '2024-04-18 16:32:29.841418');
INSERT INTO `django_migrations` VALUES(9, 'auth', '0004_alter_user_username_opts', '2024-04-18 16:32:29.857993');
INSERT INTO `django_migrations` VALUES(10, 'auth', '0005_alter_user_last_login_null', '2024-04-18 16:32:29.936192');
INSERT INTO `django_migrations` VALUES(11, 'auth', '0006_require_contenttypes_0002', '2024-04-18 16:32:29.939185');
INSERT INTO `django_migrations` VALUES(12, 'auth', '0007_alter_validators_add_error_messages', '2024-04-18 16:32:29.951946');
INSERT INTO `django_migrations` VALUES(13, 'auth', '0008_alter_user_username_max_length', '2024-04-18 16:32:29.975853');
INSERT INTO `django_migrations` VALUES(14, 'auth', '0009_alter_user_last_name_max_length', '2024-04-18 16:32:30.003001');
INSERT INTO `django_migrations` VALUES(15, 'auth', '0010_alter_group_name_max_length', '2024-04-18 16:32:30.029903');
INSERT INTO `django_migrations` VALUES(16, 'auth', '0011_update_proxy_permissions', '2024-04-18 16:32:30.047642');
INSERT INTO `django_migrations` VALUES(17, 'auth', '0012_alter_user_first_name_max_length', '2024-04-18 16:32:30.073742');
INSERT INTO `django_migrations` VALUES(18, 'sessions', '0001_initial', '2024-04-18 16:32:30.121840');

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `django_session` VALUES('4n6rgtzko04f7yfkgjc0lvdbnuvjx76z', 'eyJuYW1lIjoiSm9obiIsInVzZXJuYW1lIjoyfQ:1s1fpB:yHwwgnEm6rpnkW1zk-dULCuXrePMr42Xq1vukJ43e7U', '2024-05-14 05:14:41.112548');
INSERT INTO `django_session` VALUES('gcc6rzahia9g5r04iw28457i4vdqfsc0', 'eyJuYW1lIjoiSm9obiIsIm1zZyI6IlBhc3N3b3JkIHJlc2V0IFN1Y2Nlc3NmdWwsIHlvdXIgY29kZTozMjIyIiwidXNlcm5hbWUiOjJ9:1s1UYq:hyS5KRJrbZFJkpeHaXGm4JGaaMeKbypqq5cElO7Q1D0', '2024-05-13 17:13:04.306441');
INSERT INTO `django_session` VALUES('lbsgrcsawnt30bmzko8fph84e917mlrk', 'eyJuYW1lIjoiSm9obiJ9:1s1TfQ:u0BsyFQMC7luxphJXTUKQmcS-mjO-idsH2eTpcZMkl8', '2024-05-13 16:15:48.292979');

CREATE TABLE `music` (
  `id` int(11) NOT NULL,
  `artist_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `album_name` varchar(255) NOT NULL,
  `genre` enum('rnb','country','classic','rock','jazz') NOT NULL,
  `create_ts` datetime NOT NULL DEFAULT current_timestamp(),
  `update_ts` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(500) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `dob` datetime NOT NULL,
  `gender` enum('m','f','o') NOT NULL,
  `Address` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


ALTER TABLE `artist`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

ALTER TABLE `music`
  ADD PRIMARY KEY (`id`),
  ADD KEY `artist_id` (`artist_id`);

ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `artist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

ALTER TABLE `music`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `music`
  ADD CONSTRAINT `music_ibfk_1` FOREIGN KEY (`artist_id`) REFERENCES `artist` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
