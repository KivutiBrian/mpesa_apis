from main import api,Resource,fields
from accessToken import token

import requests #requests library
import os
import password #file containing the generated password
import timeformat #file containing the function to generate timestamp in the following format YYYYMMDDHHmmss

generated_password = password.the_decoded_password
generated_timestamp = timeformat.the_formatted_time

# create a namespace for the stk resource
ns_stkpush = api.namespace('stkpush', description="MPESA STK PUSH")

stk_payload = api.model('Stk',{
    "phone_number":fields.String,
    "amount":fields.String
})

@ns_stkpush.route('')
class Stkpush(Resource):
    
    
    @api.expect(stk_payload)
    def post(self):
    
        """Use this API endpoint to initiate online payment on behalf of a customer."""
        
        # get the payload
        data = api.payload

        # format the phone number in the right order
        formated_number = '254{}'.format(data['phone_number'][1:])

        access_token = token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": "Bearer %s" % access_token }
        request = {
            "BusinessShortCode":  os.environ.get("BusinessShortCode"),
            "Password": generated_password,
            "Timestamp": generated_timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": data['amount'],                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
            "PartyA": formated_number,
            "PartyB": os.environ.get("BusinessShortCode"),
            "PhoneNumber": formated_number, #pass in the phone number that will be prompted to enter the pin
            "CallBackURL": "https://test.com", #pass in an actual callback url if you have one
            "AccountReference": "muer101",
            "TransactionDesc": "Test payment"
        }
        
        response = requests.post(api_url, json = request, headers=headers)
        # print (response.text)

        return {"response":response.json()}
  