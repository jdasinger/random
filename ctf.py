#!/usr/bin/python

import hashlib

digits = []
for x in range(0,100001):
    total = 0
    for y in str(x):
        element = int(y)
        if element in [0,4,6,9]:
            total += 1
        elif element == 8:
            total += 2
        else:
            total += 0        
    digits.append(total)

print digits

#num = int(''.join(map(str,digits)))

#m = hashlib.md5()
#m.update("num")
#print m.hexdigest()[:20]
