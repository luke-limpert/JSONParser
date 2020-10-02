#XML Parser
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'http://py4e-data.dr-chuck.net/comments_707173.json'
parms = dict()
parms['address'] = address

url = urllib.parse.urlencode(parms)
print('Retrieving ', url)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read().decode()
info = json.loads(data)
print('User count:', len(info['comments']))

Adder = 0
Sum = 0

for item in info['comments']:
	Adder = item['count']
	Sum = Adder + Sum
print(Sum)
while True:
	print(Sum)
