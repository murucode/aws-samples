import json
import boto3

def lambda_handler(event, context):    
    sns = boto3.client('sns')
    response = sns.publish(
    TopicArn='arn:aws:sns:us-east-1:Accountnumber:muru-sampl-topic',    
    Message='Hello from mail account!',)
    
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from lambda function')
    }
