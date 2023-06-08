#!/bin/env python3

# dependency: pip install twilio

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import urllib

import secrets

SID	= secrets.SID
TOKEN	= secrets.TOKEN
TO	= secrets.TO
FROM	= secrets.FROM

def attempt_send(to, body):
	c = Client(SID, TOKEN)
	try:
		c.messages.create(to=TO, from_=FROM, body=body)
		return 'sent to %s: %s\n' % (to, body)
	except twilio.base.exceptions.TwilioRestException as e:
		return 'SMS failed: %s\n' % print(e)

def application(env, SR):

	q = urllib.parse.parse_qs(env.get('QUERY_STRING', ''))

	msg = q.get('msg', None)
	if msg is not None:
		o = attempt_send(TO, msg[0])
	else:
		o = 'no msg\n'
		
	SR('200 Ok', [('Content-Type', 'text/plain')])
	return [bytes(o, 'UTF-8')]
