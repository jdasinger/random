#!/bin/bash

# add prompts for url, oldpass and newpass instead of positional parameters
# add error handling if variable unset (or use that strict checking thing)

url=$1
oldpass=$2
newpass=$3

/usr/bin/curl -u admin:$oldpass -Fplain=$newpass -Fverify=$newpass -Fold=$oldpass -FPath=/home/users/a/admin http://$url/crx/explorer/ui/setpassword.jsp
