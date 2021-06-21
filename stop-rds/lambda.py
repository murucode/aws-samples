import boto3

cluster_whitelist = ['cluster 1', 'cluster 2']

def stop_database_clusters(event, context):
    # Disable all databases that either dont have an AutoOff tag set to 'true'
    rds_client = boto3.client('rds')

    print("Searching for database clusters")
    running_clusters_and_tags = [
        (cluster['DBClusterIdentifier'], rds_client.list_tags_for_resource(ResourceName=cluster['DBClusterArn'])['TagList'])
        for cluster in rds_client.describe_db_clusters()['DBClusters']
        if cluster['Status'] == 'available'
    ]

    clusters_to_stop = [cluster_and_tags[0] for cluster_and_tags in running_clusters_and_tags if should_manage_cluster(cluster_and_tags)]

    for cluster_identifier in clusters_to_stop:
        rds_client.stop_db_cluster(DBClusterIdentifier=cluster_identifier)

    print(f"Stopped the following clusters {clusters_to_stop}")

def should_manage_cluster(cluster_and_tags):
    return cluster_and_tags[0] not in cluster_whitelist