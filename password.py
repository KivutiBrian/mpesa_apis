import base64
import timeformat
import os

# import the formatted time in the format --> YYYYMMDDHHmmss
formatted_time = timeformat.the_formatted_time

business_short_code = os.environ.get("BusinessShortCode")
pass_key = os.environ.get("LipaNaMpesaPassKey")

def generate_password():
    # timestamp is a combinationn of shortcode+passkey+time
    timestamp = business_short_code + pass_key + formatted_time

    # encode to base64
    encode_password = base64.b64encode(timestamp.encode())

    # the result is in binary format but we need it as a string
    decoded_password = encode_password.decode('utf-8')
    
    return decoded_password

the_decoded_password = generate_password()