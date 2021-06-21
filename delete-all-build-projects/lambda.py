import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('codebuild')
    response = client.list_projects()
    for item in response['projects']:
        response = client.delete_project(name=item)
        print(item)        
    return {
        'statusCode': 200,
        'body': json.dumps('Builds deleted !')
    }
