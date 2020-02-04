This goal of this project is to predict the success of an android application and create a recommonded system for android applications.

Tools and packages used:

	Spyder in Anaconda - Packages used here google play_scraper, flask, sklearn, pandas, matplotlib, flask
	HTML, CSS, JavaScript

Data Collection:

	For prediction purpose data of around 870 apps was scraped using google play_scraper package in python.
	For recommendation purpose data of around 600 apps was scraped.

Variables Used:
	
	For prediction purpose the variables used were Category, Size of an application, Content suitable for,  Rating, No. of 					installations, Time elapsed after the last update, Android Version, No. of Reviews
	
	For recommendation system the variables used were Name of the application and the Description

Methodolgy:
	
	For prediction cleaned and transformed all the variables and built a logistic regression model to predict apps into successful or not successful. 
	
	A content based Recommondation system was created. In this based on the description of the given application it will recommend you a set of 5 		other similar applications in this database

	Flask package was used in the backend to link python with the HTML

Files:

Final_html.html: 

	This is the home screen of your webpage.

Playstore.html:
	
	This page is created for asking the user to enter details of the application and when we submit the details the output of the prediction is displayed.

login.html:
	
	This page is created for an user to select the application and once when an application is selected, the recommendation output is displayed.

output_recommend.html:
	
	This page is created for displaying the output.

Final_code_html.py:

	This is the python file and in this python code using flask was written for building a prediction model and recommendation system

Final_Data.csv:
	
	This is the data set used for prediction purpose

description_csv.csv
	
	This is the dataset used for recommendation purpose.

12.jpg
	This is the image used for background purpose in the HTML web page
