#!/bin/bash


MENU=$(cat <<-END
    BASIC - basic TCP connect scan
    PING - run a ping only scan 
    STEALTH - stealth scan
    VERSION - scan for service/version
    UDP - UDP scan
END
)

echo "Please enter the IP address or range to scan"
read ip_address

echo "Please enter the type of scan you'd like to run"
echo "$MENU"
read option


case "$option" in

BASIC)  echo "running basic TCP connect scan"
    nmap -v -sT $ip_address #basic TCP connect scan
    ;;
PING)  echo "running ping only scan"
    nmap -v -sn $ip_address #ping only scan
    ;;
STEALTH)  echo  "running stealth scan"
    nmap -v -sS $ip_address #stealth scan
    ;;
VERSION) echo  "running service/version scan"
   nmap -v -sV $ip_address #scan for service/version
   ;;
UDP) echo  "running UDP scan"
   nmap -v -sU $ip_address #UDP scan
   ;;
*) echo "Please choose an option from the menu"
   ;;
esac
