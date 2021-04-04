-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 04, 2021 at 03:54 PM
-- Server version: 8.0.18
-- PHP Version: 7.4.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `product`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--
CREATE TABLE `product`.`product` ( `pid` INT NOT NULL AUTO_INCREMENT , `pname` VARCHAR(128) NOT NULL , `price` FLOAT(5,2) NOT NULL , `pdescription` VARCHAR(225) NOT NULL , `imgname` VARCHAR(225) NOT NULL , `bid` INT NOT NULL , PRIMARY KEY (`pid`)) ENGINE = InnoDB;

DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `pname` varchar(128) NOT NULL,
  `price` float(5,2) NOT NULL,
  `pdescription` varchar(225) NOT NULL,
  `imgname` varchar(225) NOT NULL,
  `bid` int(11) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`pid`, `pname`, `price`, `pdescription`, `imgname`, `bid`) VALUES
(1, 'Product2', 1.00, 'This is the description for product 1', 'imgname', 1),
(2, 'Product3', 2.00, 'This is the description for product 1', 'imgname', 2),
(3, 'Happy Clown - Sweatshirt', 91.27, ' Just a very happy clown, happy that you\'re wearing them. Super comfy and perfect for going out or staying at home!', 'img1.jpg', 3),
(4, 'Handmade Adult Patchwork Clown Suit ', 63.18, 'A vintage old circus clown suit for you next Halloween! ', 'img2.jpg', 4),
(5, 'Circus Party Box', 35.10, 'Perfect for your circus themed party ! This product comes in pack of 12. ', 'img3.jpg', 4),
(6, 'Mint soy wax Candle', 12.64, ' Intended to draw prosperity, well-being, and fortune. Created with Eucalyptus Mint Natural Scent', 'img4.jpg', 3),
(7, 'Lavender Candle ', 23.86, ' Secret Garden top two scents are Lavender and just a hit of Rose', 'img5.jpg', 2),
(8, 'Lavender Goat Milk Soap All Natural Soap', 7.51, ' Let scent of lavender whisk you away to the french countryside', 'img6.jpg', 1),
(9, 'Handmade Cold Process Soap', 5.62, ' Love is in the air and what does it smell like? It smells beautiful, sweet & tropical.', 'img7.jpg', 2),
(10, 'Personalized Name Wood Puzzle Handmade Toy', 44.86, 'We use special paint and varnish that is 100% safe for the babies! All of the puzzle pieces are raised, making them easy to get out and play with ', 'img8.jpg', 3),
(11, 'Handmade Dinosaur Crayons', 6.80, ' These Dinosaur Crayons are perfect for your mini Dinosaur enthusiasts!', 'img9.jpg', 4),
(12, 'Knitted Handmade Bag', 97.86, 'Your unique hand knitted bag that you will never find another same one!', 'img10.jpg', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
