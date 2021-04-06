-- business
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
CREATE DATABASE IF NOT EXISTS  `ESD` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE `business`;

DROP TABLE IF EXISTS business;
CREATE TABLE business (
BID INT  primary key AUTO_INCREMENT,
BName VARCHAR (128),
Email VARCHAR (128),
Password VARCHAR (128),
Paypal VARCHAR (128),
BAddress VARCHAR (128),
BDescription VARCHAR (128)
);

insert into business (bname, email, password, paypal , baddress,bdescription)
VALUES ('Shopee', 'shopee@abc.com', MD5('newpassword'), 'shopee@adc.com', 'Blk 124 SMU Avenue 1','business desc');

insert into business (bname, email, password, paypal , baddress,bdescription)
VALUES ('Scentopia', 'scent@def.com', MD5('newpassword'), 'scent@def.com', 'Blk 300 SMU Avenue 1','We sell handmade soap and scented candles made with natual ingredients.');

insert into business (bname, email, password, paypal , baddress,bdescription)
VALUES ('Circus wholeseller', 'clownclown@123.com', MD5('newpassword'), 'clown123@def.com', 'Blk 90 Yishun Avenue 1','We supply inventory for one-mancircus startup.');
