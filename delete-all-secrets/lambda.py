import json
import boto3
client = boto3.client('secretsmanager')

def lambda_handler(event, context):
    print('Deletes all the secrets without recovery')
    response = client.list_secrets(MaxResults=100)
    list_secrets = response['SecretList']
    
    for item in list_secrets:
        print(item['Name'])
        response = client.delete_secret(SecretId=item['Name'],ForceDeleteWithoutRecovery=True)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Secrets deleted')
    }
