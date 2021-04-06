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
CREATE DATABASE IF NOT EXISTS  `business` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE `business`;
DROP TABLE IF EXISTS `business`;
CREATE TABLE IF NOT EXISTS `business` (
    `bid` INT(11) NOT NULL AUTO_INCREMENT,
    `bname` VARCHAR (128),
    `bemail` VARCHAR (128),
    `bpassword` VARCHAR (128),
    `bpaypal` VARCHAR (128),
    `baddress` VARCHAR (128),
    `bdescription` VARCHAR (128),
    PRIMARY KEY (`bid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

insert into `business` (`bid`, `bname`, `bemail`, `password`, `bpaypal`, `baddress`, `bdescription`)
VALUES (1, 'Shopee', 'shopee@abc.com', MD5('newpassword'), 'shopee@adc.com', 'Blk 124 SMU Avenue 1','business desc');

insert into `business` (`bid`, `bname`, `bemail`, `password`, `bpaypal`, `baddress`, `bdescription`)
VALUES (2, 'Scentopia', 'scent@def.com', MD5('newpassword'), 'scent@def.com', 'Blk 300 SMU Avenue 1','We sell handmade soap and scented candles made with natual ingredients.');

insert into `business` (`bid`, `bname`, `bemail`, `password`, `bpaypal`, `baddress`, `bdescription`)
VALUES (3, 'Circus wholeseller', 'clownclown@123.com', MD5('newpassword'), 'clown123@def.com', 'Blk 90 Yishun Avenue 1','We supply inventory for one-mancircus startup.');
COMMIT;