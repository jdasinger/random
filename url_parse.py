from urllib import urlencode
from urlparse import parse_qs, urlsplit, urlunsplit
import sys
import requests
import random

# def set_query_parameter(url, param_name, param_value):
#     scheme, netloc, path, query_string, fragment = urlsplit(url)
#     query_params = parse_qs(query_string)
#     query_params[param_name] = [param_value]
#     new_query_string = urlencode(query_params, doseq=True)
#     return urlunsplit((scheme, netloc, path, new_query_string, fragment))

# print set_query_parameter(sys.argv[1],sys.argv[2], sys.argv[3])

with open ("wordlist.txt", "r") as payload_file:
	payload = payload_file.read().split("\n")


## using .format()
def my_url_fxn(un, pw):
	my_url = "https://www.url.com/username={username}&password={password}".format(username=un, password=pw)
	return my_url

i = 0
while i < 10:
	payload1 = random.choice(payload)
	payload2 = random.choice(payload)
	url = my_url_fxn(payload1, payload2)
	i += 1
	print url
# for arguments in list_of_params: 
# 	# list_of_params is list of lists of un, pw, like [['username','password']]
# 	url = my_url_fxn(arguments[0], arguments[1])
# 	#use request to fetch that url 
# 	requests.get(url)
