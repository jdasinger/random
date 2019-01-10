#We lost the output file that should have been attached to this challenge; you'll have to recreate it yourself! The contents of the file start:

#0138BCDE1011113...
#It's a single line of numbers and uppercase letters.

#It was created by taking all the hexidecimal numbers from 0 through F4240, inclusive, stringing them all together in a row, and keeping only the characters that have horizontal symmetry.

#(F4240 is 1,000,000 in base ten; the last hex number F4240 contributes a 0 as the very last character of this file, since 0 is the only character in F4240 that has horizontal symmetry.)

#The flag is: the first 20 characters of the lowercase hexidecimal MD5 hash of this output file.
#B C D E H I K O X

from hashlib import md5

letters = ''

for i in (range(1,1000001)):
	letters += hex(i)[2:].translate(None, '1245679AFGJLMNPQRTUVWYZ')
print letters[:20]
#print md5(letters).hexdigest()[:20]