import random

with open ("wordlist.txt", "r") as payload_file:
	payload = payload_file.read().split("\n")

arguments = []
for i in payload():
	arguments.append(payload(i))

print arguments
# print payload
# un = random.choice(payload)
# pw = random.choice(payload)

# print un, pw