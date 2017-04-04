# whitehat.academy CTF #2 scripting challenge
# Count von Count says: a a a...
# 20 points
# scripting

# We lost the output file that should have been attached to this challenge; you'll have to recreate it yourself! The file starts:
# abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefaaaaaaaaaaaaabacadaeafbbbbbbbbbbbabbb...
# It's a single line of lowercase letters that represent all the "letters" (athrough f, but not digits 0 through 9) in each of the hexidecimal numbers from 0 through f4240, inclusive.
# (f4240 is 1,000,000 in base ten; the last hex number f4240 contributes an f as the very last character of the output file.)
# The flag is: the first 20 characters of the MD5 hash of this output file.


from hashlib import md5

letters = ''

for i in (range(1,1000001)):
	letters += hex(i)[2:].translate(None, '0123456789')
print md5(letters).hexdigest()[:20]
