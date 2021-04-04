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
pdescription VARCHAR (225) NOT NULL,
imgname VARCHAR (225)
);



insert into product (PName,Price,PDescription,imgname)
values('Happy Clown - Sweatshirt', 91.27, " Just a very happy clown, happy that you're wearing them. Each sweatshirt is precision-cut and hand-sewn to achieve the best possible look, the durable fabric with a cotton-feel face and soft brushed fleece inside means that it's also super comfy and perfect for going out or staying at home!", "img1.jpg");

insert into product (PName,Price,PDescription,imgname)
values('Handmade Adult Patchwork Clown Suit ', 63.18, "A vintage old circus clown suit for you next Halloween! ","img2.jpg");

insert into product (PName,Price,PDescription,imgname)
values('Circus Party Box', 35.10, "Perfect for your circus themed party ! This product comes in pack of 12. ","img3.jpg");

insert into product (PName,Price,PDescription,imgname)
values('Mint soy wax Candle', 12.64, " Intended to draw prosperity, well-being, and fortune. Created with Eucalyptus Mint Natural Scent","img4.jpg");

insert into product (PName,Price,PDescription,imgname)
values('Lavender Candle ', 23.86, " Secret Garden top two scents are Lavender and just a hit of Rose","img5.jpg");

insert into product (PName,Price,PDescription,imgname)
values('Lavender Goat Milk Soap All Natural Soap', 7.51, " Let scent of lavender whisk you away to the french countryside","img6.jpg");

insert into product (PName,Price,PDescription,imgname)
values('Handmade Cold Process Soap', 5.62, " Love is in the air and what does it smell like? It smells beautiful, sweet & tropical.","img7.jpg");

insert into product (PName,Price,PDescription,imgname)
values('Personalized Name Wood Puzzle Handmade Toy', 44.86, "We use special paint and varnish that is 100% safe for the babies! All of the puzzle pieces are raised, making them easy to get out and play with ","img8.jpg");

insert into product (PName,Price,PDescription,imgname)
values('Handmade Dinosaur Crayons', 6.80, " These Dinosaur Crayons are perfect for your mini Dinosaur enthusiasts!","img9.jpg");

insert into product (PName,Price,PDescription,imgname)
values('Knitted Handmade Bag', 97.86, "Your unique hand knitted bag that you will never find another same one!","img10.jpg");

insert into product (PName,Price,PDescription,imgname)
values('Clown Costume',20.93, "This is a clown costume perfect for starting circuses.","img11.jpg");

select * from product;
