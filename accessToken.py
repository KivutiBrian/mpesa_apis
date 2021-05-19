import requests
import os
from requests.auth import HTTPBasicAuth

import constants



def access_token():
    
    consumer_key = os.environ.get("consumer_key")
    consumer_secret = os.environ.get("consumer_secret")

    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    
    the_token = r.json()['access_token']
    return the_token

# store the access token that has been generated in a new variable 
# gerated_access_token = generate_access_token()
    
token = access_token()
