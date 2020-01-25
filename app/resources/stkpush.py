from main import api,Resource,fields

import requests #requests library
import constants #file contantaing some of my constant details eg consumer key & consumer secret
import accessToken #file containing the generated access token
import password #file containing the generated password
import timeformat #file containing the function to generate timestamp in the following format YYYYMMDDHHmmss

generated_password = password.the_decoded_password
generated_timestamp = timeformat.the_formatted_time

# create a namespace for the stk resource
ns_stkpush = api.namespace('stkpush', description="MPESA STK PUSH")

@ns_stkpush.route('')
class Stkpush(Resource):
    
    """Use this API to initiate online payment on behalf of a customer."""
    def post(self):
    
        access_token = accessToken.gerated_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": "Bearer %s" % access_token }
        request = {
            "BusinessShortCode": constants.BusinessShortCode ,
            "Password": generated_password,
            "Timestamp": generated_timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",
            "PartyA": "254705275702",
            "PartyB": constants.BusinessShortCode,
            "PhoneNumber": "254705275702",
            "CallBackURL": "https://test.com",
            "AccountReference": "Test100",
            "TransactionDesc": "Test payment"
        }
        
        response = requests.post(api_url, json = request, headers=headers)
        # print (response.text)

        return {"response":response.json()}
  