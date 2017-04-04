#whitehat.academy CTF #2
#Choose a strong password
#20 points
#scriptingencryption

#The flag is your password.
#Here are some guidelines for choosing a good password:
#1. Your password must be at least twenty characters long.
#2. Your password must be less than twenty-one characters long.
#3. Your password must contain only numbers and uppercase letters.
#4. Your password must contain at least ten digits.
#5. Your password must start with the Unicode equivalent (not include U+) of the emoji pair victory hand no entry sign
#6. You password must contain at least seven uppercase 'C' characters.
#7. Your password must not repeat any character more than once, with the exception of uppercase 'C'.
#8. The last five characters of your password must be numbers.
#9. The SHA-256 hex hash of your password must match the following: 2fcc64cad25d0450497348cc3810685dde660c8fb29a9a153804fa4a5b0d395d

from itertools import permutations
from hashlib import sha256

shahash = '2fcc64cad25d0450497348cc3810685dde660c8fb29a9a153804fa4a5b0d395d'
endnums = ['3','4','5','8','9']

perms = list(permutations(endnums))

for perm in perms:
	password = '270C1F6ABCCCCCC' + ''.join(perm)
	if sha256(password).hexdigest() == shahash:
		print password