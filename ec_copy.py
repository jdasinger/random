import boto3

region = 'us-east-1'


# need to convert cache_cluster_id and target bucket to command line input variable

def lambda_handler(event, context):
    try:
        source = boto3.client('elasticache', region_name=region)
        snapid = \
            source.describe_snapshots(CacheClusterId='<cache_cluster_id>', SnapshotSource='system')['Snapshots'][-1][
                'SnapshotName']
        source.copy_snapshot(SourceSnapshotName=snapid, TargetSnapshotName=snapid,
                             TargetBucket='<target_bucket>')

    except Exception as e:
        raise e
    print '[main] End'
