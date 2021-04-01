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
PID INT  primary key AUTO_INCREMENT,
PName VARCHAR (128) NOT NULL,
Price DECIMAL (5,2) NOT NULL,
PDescription VARCHAR (128) NOT NULL,
bizid INT NOT NULL
);


insert into product (PName,Price,PDescription,bizid)
values('Product1', 1.00, "This is the description for product 1",1);


select * from product;