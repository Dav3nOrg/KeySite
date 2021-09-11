#!/usr/bin/env python

from twilio.rest import Client

account_sid = 'ACf380c8edf3a8c7faa705d15e03897fe7'

auth_token = '62afd0074fd6239c9757e6134f75f0d3'

client = Client(account_sid, auth_token)

message = client.messages.create(body='Message', from_='+15017122661', to='+33629725686')

print(message.sid)
