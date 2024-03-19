import json
import pandas as pd
def lambda_handler(event, context):
    # Read data from landing zone
    # Transform the data using pandas -- (pandas we using as a layer)
    # write data into the target zone
    # push the notification to the SNS Topic
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
