""" TODO:
        Return a list of unique subj/courses - up to frontend to display
    Users: students (filter), admins
    THIS MAY NOT BE THE MOST EFFICIENT METHOD
"""

import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    response = client.scan(
        TableName = "Subjects",
        Select='SPECIFIC_ATTRIBUTES',
        AttributesToGet=['subject']
    )
    unique_subj = [item['subject']['S'] for item in response['Items']]
    unique_subj = list(set(unique_subj))
    
    subjdict = {}
    for subj in unique_subj:
        subjdict[subj] = []
        
    #get all of the courses
    all_courses = []
    response = client.scan(
        TableName = "Subjects"
    )
    all_courses.extend(response.get('Items', []))
    while 'LastEvaluatedKey' in response:
        response = client.scan(
            TableName= "Subjects",
            ExclusiveStartKey=response['LastEvaluatedKey']
        )
        all_courses.extend(response.get('Items', []))
        
    #want to add all of the courses to the dictionary, unless empty
    for course in all_courses:
        subject = course.get('subject', {'S': ''}).get('S', '')
        courseid = course.get('courseid', {'S': ''}).get('S', '')
        if courseid == "empty": continue
        subjdict[subject].append(course)
    
    return {
        'statusCode': 200,
        'body': json.dumps(subjdict)
    }