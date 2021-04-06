
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
--
CREATE DATABASE IF NOT EXISTS  `customer` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE `customer`;

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
    `cid` INT(11) AUTO_INCREMENT,
    `cName` VARCHAR (128),
    `cEmail` VARCHAR (128),
    `cPassword` VARCHAR (128),
    `cPaypal` VARCHAR (128),
    `cAddress` VARCHAR (128),
    PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci; 


insert into `customer` (`cid`, `cName`, `cEmail`, `cPassword`, `cPaypal` , `cAddress`)
VALUES (1, 'Amy Tan', 'amy@abc.com', MD5('newpassword'), 'amy@abc.com', 'Blk 123 SMU Avenue 1');

insert into `customer` (`cid`, `cName`, `cEmail`, `cPassword`, `cPaypal` , `cAddress`)
VALUES (2, 'Tommy Tan', 'tom@abc.com', MD5('newpassword'), "tom@abc.com", 'Blk 123 SMU Avenue 1');