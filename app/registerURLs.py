import requests
import accessToken #file containing the generated access token
import constants #file contantaing shortcode

def c2b_register_urls():
  
    access_token = accessToken.gerated_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "ShortCode": constants.BusinessShortCode, #either use the shortcode is the shortcode 1 on the test credential or Business shortcode
        "ResponseType": "Completed",
        "ConfirmationURL": constants.confirmationUrl,
        "ValidationURL": constants.validationUrl}
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.json)

c2b_register_urls()