import random

numberOfStreaks = 0
for experimentNumber in range(1000):
    headsortails = ""
    for i in range(100):
        if random.randint(0,1) == 0:
            headsortails += "H"
        else:
            headsortails += "T"
    if "HHHHHH" in headsortails:
        numberOfStreaks += 1
    if "TTTTTT" in headsortails:
        numberOfStreaks += 1 

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
