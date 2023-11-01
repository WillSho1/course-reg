""" Given: Type, UserID, password
    TODO:
        check if user exists
        check password
        check type
        send success or failure message
    Request:   
    Query string:
    Header:
    Body:
    {
      "UserID": "",
      "Type": "",
      "Password": ""
    }
"""

import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    userid = event["UserID"]
    type = event["Type"]
    password = event["Password"]
    corsheaders = {
      "Access-Control-Allow-Credentials": "true",
      "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
      "Access-Control-Allow-Methods": "OPTIONS, POST",
      "Access-Control-Allow-Origin": "*",
      "Content-Type": "application/json"
    }
    
    #look for user
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
        pw = user_item['Item'].get('Password', {'S': ''}).get('S', '')
        if password == pw:
            return {
                'statusCode': 200,
                'headers': corsheaders,
                'body': json.dumps(f'Login success!')
            }
        else:
            return {
                'statusCode': 400,
                'headers': corsheaders,
                'body': json.dumps(f'Login failed: incorrect credentials')
            }
    else:
        return {
            #should not reach
            'statusCode': 400,
            'headers': corsheaders,
            'body': json.dumps(f'Login failed: user either not found or authorized')
        }