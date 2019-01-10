#!/bin/bash
#based on SANS webcast: Web Application Scanning Automation
# https://www.youtube.com/watch?v=QgIyYruyCL0

# assumes targets.txt file in same directory

ports="80 443"
curdate=$(date +%Y%m%d)

nmap -n -Pn -iL targets.txt -oA $curdate\_nmap_tcp --reason

#grep '80/open' $curdate\_nmap_tcp.gnmap

#pull ip address
#grep '80/open' $curdate\_nmap_tcp.gnmap | cut -d ' ' -f2

# feed targets to nikto
for testport in $ports
    do for targetip in $(awk '/'$testport'\/open/{print $2})' $curdate\_nmap_tcp.gnmap)
        do nikto -host $targetip:$testport -ask no -nointeractive -useragent \
        "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0" \
        -Format htm -output $curdate\_nikto_$targetip\_$testport.html 
    done
done

#alternative. remove ports variable. target gnmap file directly. All results in same file
#nikto -host $curdate\_nmap_tcp.gnmap -ask no -nointeractive -useragent "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0" -Format htm -output .

#optionally expand to additional scans. w3af etc.
