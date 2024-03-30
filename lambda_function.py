import json
import pandas as pd
import boto3
from io import StringIO

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    # Read data from landing zone
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3_client.get_object(Bucket=bucket, Key=key)
    file_content = response["Body"].read().decode('utf-8')
 
    json_data = pd.read_json(StringIO(file_content))
    #print(json_data)
    #print(type(json_data))
    
    #Transform the data
    filtered_df = json_data[json_data['status'] == 'delivered']
    
    #writing transformed_data as json in other bucket...
    json_string = filtered_df.to_json(orient='records')
    key = key.replace('raw_input', 'output')
    target_bucket = 'ass-doordash-target-zone'
    
    s3_client.put_object(Bucket=target_bucket,
    Key=key,
    Body=json_string)
    
    print("Write Sucessful")
    
    #Publishing the notification into the sns 
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }