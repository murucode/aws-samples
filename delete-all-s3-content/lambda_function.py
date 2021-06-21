import json
import boto3    

def lambda_handler(event, context):
    
    s3 = boto3.resource('s3')
    
    # Print out bucket names
    for bucket in s3.buckets.all():
        try:
            print(f'  {bucket.name}')
            
            print('printing objects')
            for key in bucket.objects.all():
                print(key.key)
                key.delete()
                
            print('printing versions')
            for key in bucket.object_versions.all():
                print(key.object_key )
                #key.delete()
            
            
            bucket.delete()
            print('deleted')
        except:
            continue  
        break
    return {
        'statusCode': 200,
        'body': json.dumps('Buckets and contents deleted!')
    }
