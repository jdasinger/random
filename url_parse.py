from urlparse import *
from urllib import urlencode

import sys

#url = sys.argv[1]
url = 'http://hackeducate.com/admin?user=1&password=2'

def parse_test(url):
	scheme, netloc, path, query_string, fragment = urlsplit(url)
	query_params = parse_qs(query_string)
#	print query_params
	# outputs query params as dict like {'password': ['2'], 'user': ['1']}
	
	#for each key:value replace value with format string like {user} {password} or {var1} {var2} etc.
	for key,value in query_params.items():
		query_params[key] = "{thing}"
	print query_params



	print urlunsplit((scheme, netloc, path, query_string, fragment))

parse_test(url)



	# parsed = urlparse(url)
	# # outputs query params as dict like {'password': ['2'], 'user': ['1']}
	# params = parse_qs(parsed.query)