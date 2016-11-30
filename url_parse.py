from urllib import urlencode
from urlparse import parse_qs, urlsplit, urlunsplit
import sys


def set_query_parameter(url, param_name, param_value):
    scheme, netloc, path, query_string, fragment = urlsplit(url)
    query_params = parse_qs(query_string)
    query_params[param_name] = [param_value]
    new_query_string = urlencode(query_params, doseq=True)
    return urlunsplit((scheme, netloc, path, new_query_string, fragment))

print set_query_parameter(sys.argv[1],sys.argv[2], sys.argv[3])
