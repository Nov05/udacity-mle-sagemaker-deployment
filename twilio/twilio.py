# Download the helper library from https://www.twilio.com/docs/python/install
# import os
import json
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

filename = 'twilio.json'
with open(filename) as f:
    twilio_config = json.load(f)

client = Client(twilio_config['account_sid'], twilio_config['auth_token'])

def text_notification(body='Text notification from Twilio',
                    #   media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg']
                      from_=twilio_config['number_from'],
                      to=twilio_config['number_to']):
    message = client.messages \
        .create(
            body=body,
            # media_url=media_url,
            from_=from_,
            to=to
        )
    print(message.sid)

text_notification()