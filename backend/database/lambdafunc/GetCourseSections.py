""" TODO:
        given a courseID query course table
        return all sections of the course
    Users: Students, Admins
"""
import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    courseid = event["CourseID"]
        
    response = client.query(
        TableName = "Courses",
        KeyConditionExpression='#courseid = :val',
        ExpressionAttributeNames={
                '#courseid': 'CourseID', 
                '#sec': 'Section', 
                '#enr': 'Enrollment', 
                '#cap': 'Capacity', 
                '#loc': 'Location',
                '#sched': 'Schedule',
                '#teachid': 'TeacherID', 
        },
        ExpressionAttributeValues={':val': {'S': courseid}},
        ProjectionExpression = '#courseid, #sec, #enr, #cap, #loc, #sched, #teachid'
    )
    
    items = response.get('Items', [])
    if len(items) == 0:
        return {
            'statusCode': 400,
            'body': json.dumps(f'No available sections')
        }
    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }