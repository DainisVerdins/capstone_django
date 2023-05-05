Greatings, here is a list of questions aka what must be tested and URL paths to check out in Insomnia/Postman

Login information for superuser in Django 
login: admin
password: admin1234567890
email: admin@inbox.lv

* Does the web application use Django to serve static HTML content?
Yes

* Has the learner committed the project to a Git repository?
Yes

* Does the application connect the backend to a MySQL database?
Yes

* Are the menu and table booking APIs implemented?
** Menu 
http://127.0.0.1:8000/restaurant/menu/  -> all about creating adding menus into DB
http://127.0.0.1:8000/restaurant/menu/1 - > for single menu MenuItemsView

** Booking 
http://127.0.0.1:8000/restaurant/booking/ -> to view set of booking
http://127.0.0.1:8000/restaurant/booking/tables/ -> for CRUD operations on table 


* Is the application set up with user registration and authentication?
** Auth 
http://127.0.0.1:8000/restaurant/api-token-auth/ -> to get auth token for registered user

** user registration 
http://127.0.0.1:8000/auth/users/ -> to register new user 


* Does the application contain unit tests?
In 'littlelemon\restaurant\tests' have all tests for restaurant app

* Can the API be tested with the Insomnia REST client?
Yes, but I tested using Postman also