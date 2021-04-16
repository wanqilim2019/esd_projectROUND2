Starting the application:

	1. Unpack the team’s project files into the wamp64 or mamp directory 

	Eg. C:\wamp64\www\g8t6project-main\ if in windows

	2. Start up WAMP or MAMP and ensure all services are running before proceeding

	If the files are having some problems please refer to https://github.com/wanqilim2019/g8t6project.


Setting up the databases:

	1. Enter into the following directory g8t6/database/ to retrieve the following sql files:

		activity.sql
		business.sql
		customer.sql
		error.sql
		order.sql
		product.sql

	Load the scripts onto your local myphpadmin or mysqlworkbench and run them execute them in no particular sequence 

Setting up Docker:

	Setting up the yaml file

	Access the file titled  docker-compose.yml. Replace all <dockerid> to your own docker id 
	In the command prompt, change the directory to where the YAML file is located.
	Run yaml file using  docker -compose up 
	Use the following command to check if the containers are running: docker-compose ps


Sample accounts to use:

	Customer Account (optional use) - To make Product Purchases & Check Order:
	Username: amy@abc.com
	Password: newpassword

	Business Account (optional use) - To make Product Listing & Fulfill Order
	Username: clowncircus@def.com 
	Password: newpassword

	Paypal Sandbox Account (MUST USE) - To make Payment
	Username: amy@abc.com
	Password: X%-;Ip8c 
	

If docker fails to startup all microservices as a containers:

	1. Start up RABBITMQ using the following command in the terminal

	docker run -d --hostname esd-rabbit --name rabbitmq-mgmt -p 5672:5672 -p 15672:15672 rabbitmq:3-management

	2. After RABBITMQ is started up, boot up the following  microservices in the following sequence

		1.1. product.py

		1.2. customer.py

		1.3. business.py

		1.4. order.py

		1.5. amqp_setup.py (must run before complex microservices)

		1.6. place_order.py

		1.7. fulfill_order.py

		1.8. activity_log.py

		1.9. error.py

		1.10. check_order_biz.py

		1.11. check_order_cust.py
		
Using our application:

	1. Enter the following directory and access our application starting from the Loginpage.php page
		Eg. C:\wamp64\www\g8t6project-main\templates

	2. Sign in into the application using a business/customer account (above or create your own) to begin using their functionalities as per our scenarios
