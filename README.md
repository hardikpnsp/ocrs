# ocrs
Online Car Rental System, a college project made with python language, django framework and mysql as database.

## the structure of project 

  there are three modules (apps), one for car dealers, one for customers, one for the home page. Each app handles usual django things like models, urls and views.
  
## the system

  This is how the system works, car-dealer goes to the car_dealer_portal, signs up and uploads cars that he thinks are available for renting. Customer logs in to the customer_portal, enters the area at which he wants the car and the system scans through all the available car-dealers and their cars at that perticular area and shows the results to the customer. If the car is already rented by someone else it wont show up in the search results. 
  
## css 
 
  I have used the simple css file provided by w3schools.org. The main purpose of this project was to learn django framework, handling backend tasks and managing database, so didn't use bootstrap or other css frameworks.

## database 

  I have used the local mysql database and the python classes in models.py helps managing/updating database. the database configuration can be accessed in ocrs/ocrs/settings.py and in that file under the DATABASE section you can add your own database, username password etc.
