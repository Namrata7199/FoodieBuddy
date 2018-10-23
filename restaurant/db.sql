CREATE DATABASE food;

USE food;

CREATE TABLE `index_menu` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `food` varchar(30) NOT NULL, `price` integer NOT NULL, `cuisine` varchar(20) NOT NULL);

CREATE TABLE `index_owner` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `first_name` varchar(30) NOT NULL, `middle_name` varchar(30) NOT NULL, `last_name` varchar(30) NOT NULL);

CREATE TABLE `index_restaurant` (`name` varchar(30) NOT NULL, `dno` varchar(10) NOT NULL, `street` varchar(30) NOT NULL, `city` varchar(30) NOT NULL, `phn` integer NOT NULL, `images` varchar(10000) NOT NULL, `gstin` varchar(20) NOT NULL PRIMARY KEY, `menupk_id` integer NOT NULL);

ALTER TABLE `index_owner` ADD COLUMN `gstin_id` varchar(20) NOT NULL;
ALTER TABLE `index_restaurant` ADD CONSTRAINT `index_restaurant_menupk_id_68046d30_fk_index_menu_id` FOREIGN KEY (`menupk_id`) REFERENCES `index_menu` (`id`);
ALTER TABLE `index_owner` ADD CONSTRAINT `index_owner_gstin_id_3f62db8d_fk_index_restaurant_gstin` FOREIGN KEY (`gstin_id`) REFERENCES `index_restaurant` (`gstin`);


CREATE TABLE `index_reviews` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `ratings` integer NOT NULL, `Feedback` varchar(1000) NOT NULL);

CREATE TABLE `index_search_by_cuisine` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY);

CREATE TABLE `index_user` (`email` varchar(30) NOT NULL PRIMARY KEY, `first_name` varchar(30) NOT NULL, `middle_name` varchar(30) NOT NULL, `last_name` varchar(30) NOT NULL, `dno` varchar(10) NOT NULL, `street` varchar(30) NOT NULL, `city` varchar(30) NOT NULL, `phn` integer NOT NULL);

ALTER TABLE `index_restaurant` ADD COLUMN `cuisine` varchar(30) DEFAULT no NOT NULL;
ALTER TABLE `index_restaurant` ALTER COLUMN `cuisine` DROP DEFAULT;

ALTER TABLE `index_user` ADD COLUMN `rest_id` varchar(20) NOT NULL;

ALTER TABLE `index_search_by_cuisine` ADD COLUMN `email_id` varchar(30) NOT NULL;

ALTER TABLE `index_search_by_cuisine` ADD COLUMN `gstin_id` varchar(20) NOT NULL;

ALTER TABLE `index_reviews` ADD COLUMN `gstin_id` varchar(20) NOT NULL;

ALTER TABLE `index_reviews` ADD COLUMN `userpk_id` integer NOT NULL;
ALTER TABLE `index_user` ADD CONSTRAINT `index_user_rest_id_b25021d2_fk_index_restaurant_gstin` FOREIGN KEY (`rest_id`) REFERENCES `index_restaurant` (`gstin`);
ALTER TABLE `index_search_by_cuisine` ADD CONSTRAINT `index_search_by_cuisine_email_id_0eab35cf_fk_index_user_email` FOREIGN KEY (`email_id`) REFERENCES `index_user` (`email`);
ALTER TABLE `index_search_by_cuisine` ADD CONSTRAINT `index_search_by_cuis_gstin_id_d416119d_fk_index_res` FOREIGN KEY (`gstin_id`) REFERENCES `index_restaurant` (`gstin`);
ALTER TABLE `index_reviews` ADD CONSTRAINT `index_reviews_gstin_id_c7c3cd99_fk_index_restaurant_gstin` FOREIGN KEY (`gstin_id`) REFERENCES `index_restaurant` (`gstin`);
ALTER TABLE `index_reviews` ADD CONSTRAINT `index_reviews_userpk_id_e0d7c0f4_fk_index_owner_id` FOREIGN KEY (`userpk_id`) REFERENCES `index_owner` (`id`);


