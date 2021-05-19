import base64
import constants
import timeformat

# import the formatted time in the format --> YYYYMMDDHHmmss
formatted_time = timeformat.the_formatted_time

def generate_password():
    # timestamp is a combinationn of shortcode+passkey+time
    timestamp = constants.BusinessShortCode +constants.LipaNaMpesaPassKey+formatted_time

    # encode to base64
    encode_password = base64.b64encode(timestamp.encode())

    # the result is in binary format but we need it as a string
    decoded_password = encode_password.decode('utf-8')
    
    return decoded_password

the_decoded_password = generate_password()