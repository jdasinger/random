import requests

response = requests.get("https://example.com")
print("Status code: {}".format(response.status_code))
print(response.content)
