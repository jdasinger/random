# whitehat.academy CTF #1 scripting challenge
# Counting holes
# 20 points
# scripting crypto

# On no! We lost the file that would have given you the flag. You'll have to 
# create it yourself. It started something like this:
# 100010102110001...
# The file contains a single, very long string of digits that represent the total
# 'holes' in each of the numbers from 0 through 100,000. Specifically, the
# digits 0. 4. and 9 all have one 'hole'; the digit 8 has two holes, and other
# digits (1,2,3,5,7) have zero holes.

#The flag is the first 20 characters of the MD5 hash of this file's contents.

from hashlib import md5

digits = ''
for x in xrange(0,100001):
    total = 0
    for y in str(x):
        if y in ['0','4','6','9']:
            total += 1
        elif y == '8':
            total += 2
        else:
            total += 0        
    digits += str(total)

print md5(digits).hexdigest()[:20]
