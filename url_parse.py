from urlparse import *
from urllib import urlencode
import random
import sys
import requests

input_file = sys.argv[1] #this is a text file with your attack payload
num = sys.argv[2] #this is the number of requests you want to make to the target url
url = 'http://hackeducate.com/admin?user=1&password=2'

def get_payload():
	with open ("wordlist.txt", "r") as payload_file:
		payload = payload_file.read().split("\n")
	return random.choice(payload)

def parse_test(url):
	scheme, netloc, path, query_string, fragment = urlsplit(url)
	
	query_params = parse_qs(query_string)

	# outputs query params as dict like {'password': ['2'], 'user': ['1']}

	for key,value in query_params.items():
	 	query_params[key] = get_payload()
	
	new_query = urlencode(query_params)

	target_url = urlunsplit((scheme, netloc, path, new_query, fragment))
	return target_url
print parse_test

# i = 0
# while i < int(num):
# 	req = requests.get(target_url)
# # #	print req.text
#  	i += 1

response = requests.get(parse_test(url))



	# parsed = urlparse(url)
	# # outputs query params as dict like {'password': ['2'], 'user': ['1']}
	# params = parse_qs(parsed.query)