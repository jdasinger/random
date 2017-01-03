#!/bin/bash

#script to toggle the NewRelic alerts for on and off during scheduled restarts.

#convert ALERTPOLICYKEY and NEWRELICAPIKEY to variable



if [ -z "$1" ]; then
              echo "usage: $0 start|stop"
              exit
fi

if [ $1 = "start" ]
        then
        /usr/bin/curl -X PUT "https://api.newrelic.com/v2/alert_policies/ALERTPOLICYKEY.json" \
             -H "NEWRELIC_API_KEY" -i \
             -H "Content-Type: application/json" \
             -d '{"alert_policy": {"enabled": "true"}}'
elif [ $1 = "stop" ]
        then
        /usr/bin/curl -X PUT "https://api.newrelic.com/v2/alert_policies/ALERTPOLICYKEY.json" \
             -H "NEWRELICAPIKEY" -i \
             -H "Content-Type: application/json" \
             -d '{"alert_policy": {"enabled": "false"}}'
fi
