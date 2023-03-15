## Kubera API - credit card system

### **Technologies/Frameworks/Libs used:**

- FastAPI
- uvicorn - server client
- cryptography - to mask credit card number
- pydantic - data validation
- loglifos - logs
- python-decouple - files .env
- motor - mongodb async
- passlib.hash - password hashs
- pyjwt - generate, validate, decrypt token
- dateparser - date/datetime parser

### Step one
#### create a virtual environment
Create and start a virtual env for the project. 

- To create the virtual environment, run:
```bash
python3 -m venv env
```
- To activate the virtual environment run:

    Linux:
    ```bash
    source env/bin/activate
    ```
    Windows:
    ```shell
    env\Scripts\activate.bat
    ```

### Step two
#### Installation of dependencies
1. __Install the packages in the virtual environment from the following command:__
    
    ```bash
    pip install -r requirements.txt
    ```  

### Step three
#### Create environment variables

1. Create a `.env` file in the project root, following this template:

~~~
MONGODB_CONNECTION_URL="mongodb://localhost:27017" # start a local mongodb server or use your online string connection, using password and username if necessary
MONGODB_DATABASE_NAME="kubera"  # create a database with this name
MONGODB_USER_COLLECTION="users"  # create a collecation with this name
JWT_SECRET_KEY="mysecret" # you can generate your secret key
JWT_ALGORITHM='HS256" 
JWT_TTL="FILL_THIS_WITH_TIME_TO_LIVE_TOKEN"  # example: "3600"
KUBERA_ENCRYPTION_KEY='d5GWW0tT4F2tcC9C4SgKW5RKMl6SEIlZtfDBp9R4k6s='  # use this key, or consulting Fernet generate key for mor details
~~~

### Step four
#### Run project

1. To start the uvicorn server you need to be at the project root in the terminal and run the following command
 ~~~
   you can simply run the main.py file to start the server
   
   or setting your command line
   
   uvicorn main:app --host 0.0.0.0 --port 9000
 ~~~

2. You can change the HOST and PORT as you wish.

## **Endpoints:**

### "/api/v1/user  method=POST"

> _Endpoint to register a new user_

### "/api/v1/token   method=POST"

> _Endpoint to generate your baerer token_

### "/api/v1/credit-card  method=POST"

> _Endpoint to register a new credit card_

### "/api/v1/credit-card  method=GET"

> _Endpoint to get all the credit card numbers you have registered_

### "/api/v1/credit-card/{number}  method=GET"

> _Endpoint to get credit card details_

**internal_code available:**

- **SUCCESS=**
  0
- **INVALID_PARAMS=**
  10
- **INVALID_AUTHENTICATION=**
  30
- **INTERNAL_SERVER_ERROR=**
  40
- **UNAUTHORIZED=**
  50
- **DATA_VALIDATION_ERROR=**
  60
- **DATA_NOT_FOUND=**
  61
- **DATA_ALREADY_EXISTS=**
  62

