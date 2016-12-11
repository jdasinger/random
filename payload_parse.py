import random


def get_payload():
	with open ("wordlist.txt", "r") as payload_file:
		payload = payload_file.read().split("\n")
	return random.choice(payload)

# un = random.choice(payload)
# pw = random.choice(payload)

# print un, pw
get_payload()