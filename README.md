#### README- Assignment Submission :: Aayush Gadia

-----

##### API Name, Description, it's EndPoints, TestCases, ScreenShots-
1. **myauth**

- *API EndPoints-*
	- *Login URL- http://127.0.0.1:8000/myauth/login/ (POST API)*
	- *Logout URL- http://127.0.0.1:8000/myauth/logout/ (GET API)*
	   - *(Key, Value) passed in Headers :: (Authorization, Token ccacf07ed29370f863ad74699359819ebca3a35a)*
	   - *The above passed token is just an example.*
	- *SignUp URL- http://127.0.0.1:8000/myauth/signup/ (POST API)*
	- *GetToken URL- http://127.0.0.1:8000/myauth/get-token/ (POST API)*
		- *(Key, Value) passed in Form-data of Body :: (phone : 8334827095, password : Aayush@2020)*
		- *The above passed value is just an example.*

- *Description-*
	- *Login is done using HTML Templates, because their is CSRF Validation by Django so it can't be developed without rendering a Page. Similarly SignUp is done*
	- *For, security issues whenever a user will login, then on passing the username & password of the user to the *GetToken URL Endpoint, token would be returned. Using this token we could restrict all the functionality of the Application like **Search, Marking Spam, Logout** (this was also asked, that nothing would be public)*
	- *When the Logout URL Endpoint is hit, then the user whose token was authenticated, that user token is deleted from the token table because the user has logged out.*

- *Test Cases-*
	- *Also, we have done validation of the user input in the sign-up, login function. So, if a user doesn't enters the value as per the requirements, then corresponding error would be thrown.*
	- *Regex has been used for such validation, it could be seen in the views.py of the myauth application.*
	- *Here, we have also made sure that Email ID Field is not mandatory.*
	- *Here, also during Sign-up it checks whether any number is already registered before or not, if not then only it is allowed to sign-up*

- *Screenshots-*
	- ![login](rough/login.png)
	- ![logout](rough/logout.png)
	- ![signup](rough/signup.png)
	- ![get-token-1](rough/get-token-1.png)


2. **spam**

- *API EndPoints-*
	- *http://127.0.0.1:8000/spam/ (POST API)*
		- *(Key, Value) passed in Headers :: (Authorization, Token 076b19e8d60fe1e62d094d3d394e7c44361a247d)*
		- *The above passed token is just an example.*

		- *(Key, Value) passed in Form-data of Body :: (mobno : 8334827095)*
		- *The above passed value is just an example.*

- *Description-*
	- *Here, when the API Endpoint would be hit, again here the **token based validation is done as explained before.***
	- *On hitting the API Endpoint, if the particular number already exists as a SPAM number then simply the count would be increase , which marks the number of people who has marked that number spam otherwise a new entry would be done in the table with spam count = 1*


- *Test Cases-*
	- *Also, we have done validation of the user input in the spam api. So, if a user doesn't enters a 10 digit mobile number then error would be thrown.*
	- *Regex has been used for such validation, it could be seen in the views.py of the spam application.*


- *Screenshots-*
	- ![spam-1](rough/spam-1.png)
	- ![spam-2](rough/spam-2.png)


3. **search**

- *API EndPoints-*
	- *http://127.0.0.1:8000/search/aayush/ (GET API)*
		- *(Key, Value) passed in Headers :: (Authorization, Token 076b19e8d60fe1e62d094d3d394e7c44361a247d)*
		- *The above passed token is just an example.*

	- *http://127.0.0.1:8000/search/8334827095/ (GET API)*
		- *(Key, Value) passed in Headers :: (Authorization, Token 076b19e8d60fe1e62d094d3d394e7c44361a247d)*
		- *The above passed token is just an example.*


- *Description-*
	- *Here, when the API Endpoint would be hit, again here the **token based validation is done as explained before.***
	- *On hitting the API Endpoint, automatically it would be checked if the serch is done by name or by number and accordingly the respective functionality would be executed.*
	- *For Search by Name , as **asked in the problem statement file** in that way functionality is executed, same is the case for Search by Number.*

- *Screenshots-*
	- ![search-1](rough/search-1.png)
	- ![search-2](rough/search-2.png)
	- ![search-3](rough/search-3.png)


-----

##### DATABASE-

- *Here, I am using the default **User** model of the Django for storing the **Registered User data***
- *I have created the **UserContacts** model for storing the contacts of the **Regstered Users**.*
- *Also, for populating the **UserContacts** model, I had written django management commands **(viz stored in the myauth/management/commands directory)**. Using the management program I was easily able to generate 40 dataset (one can as many as they want) by simply executing **python manage.py populatedata***
- *Also, I had created **Spam** model for storing the number marked as spam and the number of users who marked it spam*
- *To, know more please visit the **db.sqlite3.***

- *Screenshots-*
	- ![db-1](rough/db-1.png)
	- ![db-2](rough/db-2.png)
	- ![db-3](rough/db-3.png)

-----

##### Author-
- **AAYUSH GADIA**
- **Phone- +91- 8334827095  |  Email- gadia.aayush@gmail.com**
- **[Wesbite](https://gadia-aayush.github.io/) | [GitHub](https://github.com/gadia-aayush)  |  [LinkedIn](https://www.linkedin.com/in/gadia-aayush/)**

------
