from urlparse import *
import sys

url = sys.argv[1]
#url = 'http://hackeducate.com/admin?user=1&password=2'

parsed = urlparse(url)

print parse_qs(parsed.query)