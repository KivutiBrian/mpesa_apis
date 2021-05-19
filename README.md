# mpesa_apis

An API created (using flask rest-plus) to consume the safaricom daraja APIs and includes STK push, C2B

## Installation

1.Clone Repo

```
https://github.com/KivutiBrian/mpesa_apis.git
```

2.Create Virtual Environment folder

```
python -m venv env
```


3.Activate virtual environment in parent directory of your "env"

For Linux systems and MAC

```
source env/bin/avtivate
```

For Windows

```
env\Scripts\activate.bat
```

4.Install requierements
```
pip install - r requirements.txt
```

5.Before you can run the application successfully, you need to have environment variable. create a .env file with the following keys and add values to them,

```
consumer_key
consumer_secret
BusinessShortCode
LipaNaMpesaPassKey
test_msisdn
shortcode
validationUrl
confirmationUrl

```

5.1. An example of you .env file should look as follows

```

consumer_key="pktAy18FlHNwm2234234234"
consumer_secret="9blQ843534"
BusinessShortCode = "174379" 
LipaNaMpesaPassKey = 'bfb279f9aa9bdbcf158e97dd71a467'
test_msisdn = "254708374149"
shortcode = "601337"
validationUrl = 'https://www.testdomain.com/validation'
confirmationUrl = 'https://www.testdomain.com/confirmation'
```

To run the code

For windows
```
set FLASK_APP=main.py
set FLASK_ENV=development
flask run
```

For Linux systems and MAC
```
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```

# ENDPOINTS

![](swagger.PNG)
