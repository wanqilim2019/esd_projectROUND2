
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

CREATE TABLE customer (
CID INT  primary key AUTO_INCREMENT,
CName VARCHAR (128),
Email VARCHAR (128),
Password VARCHAR (128),
Paypal VARCHAR (128),
CAddress VARCHAR (128)
);


insert into customer (cname, email, password, paypal , caddress)
VALUES ('Amy Tan', 'amy@abc.com', MD5('newpassword'), 'amy@abc.com', 'Blk 123 SMU Avenue 1');

insert into customer (cname, email, password, paypal , caddress)
VALUES ('Tommy Tan', 'tom@abc.com', MD5('newpassword'), "tom@abc.com", 'Blk 123 SMU Avenue 1');