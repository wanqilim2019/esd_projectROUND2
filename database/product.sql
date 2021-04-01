SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book`
--
CREATE DATABASE IF NOT EXISTS  `product` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE `product`;

CREATE TABLE product (
pid INT AUTO_INCREMENT PRIMARY KEY,
pname VARCHAR (128) NOT NULL,
price DECIMAL (5,2) NOT NULL,
pdescription VARCHAR (128) NOT NULL,
pic VARCHAR (128)
);



insert into product (PName,Price,PDescription)
values('Product2', 1.00, "This is the description for product 1");

insert into product (PName,Price,PDescription)
values('Product3', 2.00, "This is the description for product 1");


select * from product;
