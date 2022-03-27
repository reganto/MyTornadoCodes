__author__ = 'admin'
import opentok
import random
api_key = str(random.getrandbits(8))        # Replace with your OpenTok API key.
api_secret = str(random.getrandbits(8))  # Replace with your OpenTok API secret.

opentok_sdk = opentok.OpenTok(api_key, api_secret)
session = opentok_sdk.create_session()
print (session.session_id)