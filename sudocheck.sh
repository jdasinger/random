#!/bin/bash

# This script displays a list of users and their sudo priviliges. 
# It pulls a list of users from the passwd file then lists their permissions, 
# filtering out users that aren't able to sudo i.e. "not allowed to run sudo" or "unknown user"

for i in $(getent passwd | cut -d: -f1); do
        sudo -n -l -U $i 2>&1 | egrep -i -A 10  "may run the following commands"
done
