#!/bin/bash

# This script checks for security groups that don't allow access to the qualys scanner; either via the application of the qualys-access security group or the scanner's IP.
# This script requires installation of the aws command line tools with relevant permissions.
# It can be used as a nagios plugin.

# id of qualys-access security group

#TBD: convert QUALYS_SCANNER_IP to variable

sg="SECURITY GROUP ID"

# Output a list of security groups that are attached to instances and compare to a list of instances that do have the qualys access security group. 
# Suppress common lines to output security groups without qualys access  
/usr/bin/comm -23 <(aws ec2 describe-instances --query 'Reservations[*].Instances[*].SecurityGroups[*].GroupId' --output text | tr '\t' '\n' | sort | uniq) \
<(aws ec2 describe-security-groups --output text --filters Name=ip-permission.group-id,Values=$sg --query 'SecurityGroups[*].{Name:GroupId}' | sort | uniq) > /tmp/file1

#Get a list of security groups that allow access from the qualys scanner's IP
aws ec2 describe-security-groups --output text --filters Name=ip-permission.cidr,Values='QUALYS_SCANNER_IP' --query 'SecurityGroups[*].{Name:GroupId}' | sort | uniq > /tmp/file2

# Filter the output from the first list with the output from the second list to get security groups which don't allow access to either the qualys access security group or the scanner IP. 
grpcheck=$(/usr/bin/comm -23 /tmp/file1 /tmp/file2 )

echo $grpcheck
# Status code output for Nagios
if [[ -z $grpcheck ]]
then
                echo "OK - All security groups have Qualys access"
                exit 0

#Critical
else
                echo "CRITICAL - $grpcheck missing qualys access"
                exit 2
fi

