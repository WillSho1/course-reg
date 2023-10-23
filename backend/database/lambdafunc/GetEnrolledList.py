""" Given:  userID, type
    Return: enrollment list
    Users:  Students, maybe teachers
"""

import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    userid = event["UserID"]
    type = event["Type"]
    
    user_item = client.get_item(
        TableName='Users',
        Key={
            'Type': {
                'S': type,
            },
            'UserID': {
                'S': userid        
            }
        }
    )
    
    if ('Item' in user_item):
        enrollment = user_item['Item'].get('Enrollment', {'L': []}).get('L', [])
        return {
            'statusCode': 200,
            'body': json.dumps(enrollment)
        }
    else:
        return {
            #should not reach
            'statusCode': 400,
            'body': json.dumps(f'User not found')
        }