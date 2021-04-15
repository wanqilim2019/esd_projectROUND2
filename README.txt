Starting the application:

	1. Unpack the team’s project files into the wamp64 or mamp directory 

	Eg. C:\wamp64\www\g8t6 if in windows

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
