""" Given: courseID-section,  UserID
    TODO:
        query course table for more information on this course/section
        return information on the course (MAKE SURE TO DIFFERENTIATE BETWEEN USERS)
    Users: teachers
"""
import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    course_id_section = event["course-id-section"]
    split = course_id_section.split('-')
    courseid = split[0]
    section = split[1]
    userid = event["UserID"]
    
    #CHECK FOR AUTHORIZATION - make sure user with that type exists
    user_item = client.get_item(
        TableName='Users',
        Key={
            'Type': {
                'S': 'Teacher',
            },
            'UserID': {
                'S': userid    
            }
        }
    )
    
    if ('Item' not in user_item):
        return {
            'statusCode': 400,
            'body': json.dumps(f'Incorrect Authorization')
        }
    #else...
    course_item = client.get_item(
        TableName='Courses',
        Key={
            'CourseID': {
                'S': courseid,
            },
            'Section': {
                'N': section
            }
        }
    )
    if ('Item' in course_item):
        #MAKE SURE THE FRONTEND LIKES THE OUTPUT
        #get items to return
        location = course_item['Item'].get('Location', {'S': ''})
        schedule = course_item['Item'].get('Schedule', {'M': {}})
        studentlist = course_item['Item'].get('StudentList', {'L': []})
        result = {}
        result['Location'] = location
        result['Schedule'] = schedule
        result['StudentList'] = studentlist
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
        
    else:
        return {
            #should not reach this point
            'statusCode': 400,
            'body': json.dumps(f'Course not found')
        }