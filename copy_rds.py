#
# Code per http://blog.powerupcloud.com/2016/03/26/automating-rds-snapshots-with-aws-lambda/
#

import boto3
import botocore
import datetime
import re

SOURCE_REGION = 'us-east-1'
TARGET_REGION = 'us-west-1'
iam = boto3.client('iam')
instances = ['<instance name>'] # convert to command line argument

print('Loading function')


def get_timestamp_or_now(snap):
    if 'SnapshotCreateTime' in snap:
        return datetime.datetime.isoformat(snap['SnapshotCreateTime'])
    else:
        return datetime.datetime.isoformat(datetime.datetime.now())


def lambda_handler(event, context):
    account_ids = []
    try:
        iam.get_user()
    except Exception as e:
        account_ids.append(re.search(r'(arn:aws:sts::)([0-9]+)', str(e)).groups()[1])
        account = account_ids[0]

    source = boto3.client('rds', region_name=SOURCE_REGION)

    for instance in instances:
        source_snaps = source.describe_db_snapshots(DBInstanceIdentifier=instance)['DBSnapshots']
        source_snap = sorted(source_snaps, key=get_timestamp_or_now, reverse=True)[0]['DBSnapshotIdentifier']
        source_snap_arn = 'arn:aws:rds:%s:%s:snapshot:%s' % (SOURCE_REGION, account, source_snap)
        target_snap_id = (re.sub('rds:', '', source_snap))
        print('Will Copy %s to %s' % (source_snap_arn, target_snap_id))
        target = boto3.client('rds', region_name=TARGET_REGION)

        try:
            response = target.copy_db_snapshot(
                SourceDBSnapshotIdentifier=source_snap_arn,
                TargetDBSnapshotIdentifier=target_snap_id,
                CopyTags=True)
            print(response)
        except botocore.exceptions.ClientError as e:
            raise Exception("Could not issue copy command: %s" % e)

