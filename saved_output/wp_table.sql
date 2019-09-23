CREATE TABLE `wp_participants_database` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `private_id` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `first_name` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `last_name` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
   `address` tinytext COLLATE utf8_unicode_ci DEFAULT NULL,
   `city` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
   `state` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
   `country` tinytext COLLATE utf8_unicode_ci DEFAULT NULL,
   `zip` tinytext COLLATE utf8_unicode_ci DEFAULT NULL,
   `phone` tinytext COLLATE utf8_unicode_ci DEFAULT NULL,
   `email` tinytext COLLATE utf8_unicode_ci DEFAULT NULL,
   `mailing_list` text COLLATE utf8_unicode_ci DEFAULT NULL,
   `photo` text COLLATE utf8_unicode_ci DEFAULT NULL,
   `website` text COLLATE utf8_unicode_ci DEFAULT NULL,
   `interests` text COLLATE utf8_unicode_ci DEFAULT NULL,
   `approved` varchar(8) COLLATE utf8_unicode_ci DEFAULT NULL,
   `date_recorded` timestamp NOT NULL DEFAULT current_timestamp(),
   `date_updated` timestamp NULL DEFAULT NULL,
   `last_accessed` timestamp NULL DEFAULT NULL,
   `details` text COLLATE utf8_unicode_ci DEFAULT NULL,
   `content` text COLLATE utf8_unicode_ci DEFAULT NULL,
    `old_id` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
    `slug` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
     PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci
