from main import api,Resource,fields
from accessToken import token

import os
import requests
import json

# create a namespace
ns_c2b = api.namespace('c2b', description="MPESA c2b")

# describe the payload expected
sim_transaction = api.model('Sim',{
    "amount":fields.Integer,
    "msisdn":fields.String,
    "billRefNumber": fields.String
})


# Use this API to register validation and confirmation URLs on M-Pesa 
@ns_c2b.route('/registerurl')
class C2b(Resource):
    
    def post(self):
        """Use this API endpoint to register validation and confirmation URLs on M-Pesa"""

        access_token = token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = { "ShortCode": os.environ.get("BusinessShortCode"), #the shortcode is the shortcode 1 on the test credential
            "ResponseType": "Confirmed",
            "ConfirmationURL": os.environ.get("confirmationUrl"),
            "ValidationURL": os.environ.get("validationUrl")}
        
        response = requests.post(api_url, json = request, headers=headers)
        
        return {"message":"urls successfully registered"}, 200


# Whenever M-Pesa receives a transaction on the shortcode,
#  M-Pesa triggers a validation request against the validation URL 
@ns_c2b.route('/validation')
class C2bValidation(Resource):

    def post(self):

        """ Whenever M-Pesa receives a transaction on the shortcode,M-Pesa triggers a validation request against the validation URL  """

        data = api.payload
        
        try:
            with open('ValidateResponse.json', 'a') as outfile:
                json.dump(data, outfile)
        except:
            print('sss')
        return {"ResultCode":0, "ResultDesc":"Confirmation received successfully"}, 200


# Whenever M-Pesa receives a transaction on the shortcode,
#  M-Pesa triggers a confirmation request against the confirmation URL 
@ns_c2b.route('/confirmation')
class C2bConfirmation(Resource):
    
    def post(self):

        """ Whenever M-Pesa receives a transaction on the shortcode,M-Pesa triggers a validation request against the confirmation URL  """

        data = api.payload
        try:
            with open('ConfirmResponse.json', 'a') as outfile:
                json.dump(data, outfile)
        except:
            print('sss')
        return {"ResultCode":0, "ResultDesc":"Confirmation received successfully"}, 200


# C2B Simulate Transaction - Resource URL
@ns_c2b.route('/simulate/transaction')
class C2bSimulateTransaction(Resource):

    @api.expect(sim_transaction)
    def post(self):
        
        """This API endpoint is used to make payment requests from Client to Business (C2B)."""

        data = api.payload

        access_token = token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = { "ShortCode": os.environ.get("shortcode"),
            "CommandID":"CustomerPayBillOnline",
            "Amount":data['amount'],
            "Msisdn":data['msisdn'],
            "BillRefNumber":data['billRefNumber']} # (Optional)
        
        response = requests.post(api_url, json = request, headers=headers)
        
        return  {"response":response.json()}
  