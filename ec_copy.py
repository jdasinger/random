import boto3

region = 'us-east-1'

cluster_id = sys.argv[1]
target_bucket = sys.argv[2]


def lambda_handler(event, context):
    try:
        source = boto3.client('elasticache', region_name=region)
        snapid = \
            source.describe_snapshots(CacheClusterId=cluster_id, SnapshotSource='system')['Snapshots'][-1][
                'SnapshotName']
        source.copy_snapshot(SourceSnapshotName=snapid, TargetSnapshotName=snapid,
                             TargetBucket=target_bucket)

    except Exception as e:
        raise e
    print '[main] End'
