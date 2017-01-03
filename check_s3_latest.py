import boto3
from datetime import datetime
import sys

# the script takes the s3 bucket name as an argument
bucket = sys.argv[1]
today = datetime.now().strftime('%y-%m-%d')
conn = boto3.client('s3')

datelist = []
for key in conn.list_objects(Bucket=bucket
                             )['Contents']:
    datelist.append(key['LastModified'].strftime('%y-%m-%d'))

# set return code so nagios can react to results

if today in datelist:
    print 'Current snapshot available'
    exit()
else:
    exit('Current snapshot not found')

