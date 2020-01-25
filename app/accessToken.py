import requests
from requests.auth import HTTPBasicAuth
import constants


def generate_access_token():
    
    consumer_key = constants.consumer_keyy
    consumer_secret = constants.consumer_secrett
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    #get the response in json format 
    access_token  = r.json()

    return access_token['access_token']

# store the access token that has been generated in a new variable 
gerated_access_token = generate_access_token()
    

