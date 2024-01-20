# Django that allows you to store data that is specific to a particular user's session on the server.
# Each user that interacts with your website is assigned a unique session ID which is
# stored as a cookie in their browser.
# This session ID is used by Django to retrieve the session data for that user when they make
# subsequent requests to the server.
# You can store any Python object as a value in the request.session dictionary, and it will be
# serialized and stored on the server. This can be useful for storing data that needs to persist across
# multiple requests, such as user authentication information, shopping cart contents, or in my case,
# the OTP that was sent to the user's phone number.


# The requests library is a third-party package that allows you to easily send HTTP requests in Python.
# In this case, requests.get(url) sends a GET request to the URL specified by the url variable, and
# returns a Response object. This object contains the server's response to the request,
# including the response status code, headers, and content.
# In Python's requests library, the ok attribute of a response object is a boolean that indicates
# whether the request was successful or not. If the status code of the HTTP response is
# between 200 and 400 (inclusive), ok is True, otherwise it is False.



# In my code if response.ok: is checking whether the HTTP response was
# successful or not. If it was successful, it means that the OTP was sent successfully, and the code
# redirects the user to the validate_otp page. If the response was not successful,
# it means that there was an error in sending the OTP, and an error message is displayed to the user.

# dotenv is a Python module that allows you to load variables from a .env file into your environment variables.
# This can be useful when you have sensitive information, such as API keys or database credentials,
# that you don't want to hard-code in your codebase.
# load_dotenv() is a function from the dotenv module that loads the variables from the .env file into the
# environment variables.
# os.getenv('API_KEY') retrieves the value of the API_KEY variable from the environment variables.
# This assumes that you have loaded the variable into the environment variables using load_dotenv().


# <div class="alert alert-success"> is an HTML tag that is used to display a success message in a web page.
# It is typically used to display a message to the user after they have completed a successful action,
# such as submitting a form or completing a transaction. The alert class is used to specify that the message
# should be displayed as an alert box, and the alert-success class is used to indicate that the message is a
# success message, which is typically displayed with a green background color.




How to test API responce.ok() ?---->>>
Terminal -->> py manage.py shell
>>> import os
>>> import requests
>>> API_KEY = os.getenv('API_KEY')
>>> url = f'https://2factor.in/API/V1/{API_KEY}/SMS/+91{8888284452}/AUTOGEN'
>>> response = requests.get(url)
>>> print(response.status_code)
200
>>> print(response.json())
{'Status': 'Success', 'Details': 'aba257d8-17ef-4cff-ae52-f309ccc4dd44'}
