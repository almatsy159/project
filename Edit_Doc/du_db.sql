CREATE DATABASE IF NOT EXISTS `du_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `du_db`;


CREATE TABLE `block` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `parent_id` int DEFAULT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `doc` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `parent_id` int NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE `du` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



--
-- Index pour la table `block`
--
ALTER TABLE `block`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `doc`
--
ALTER TABLE `doc`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `du`
--
ALTER TABLE `du`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `block`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

ALTER TABLE `doc`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

-
ALTER TABLE `du`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
