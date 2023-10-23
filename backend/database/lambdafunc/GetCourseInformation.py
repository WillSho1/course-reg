""" Given: courseID-section, type, UserID
    TODO:
        query course table for more information on this course/section
        return information on the course (MAKE SURE TO DIFFERENTIATE BETWEEN USERS)
    Users: Students, teachers
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
    type = event["Type"]
    
    #CHECK FOR AUTHORIZATION - make sure user with that type exists
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
        teacher = course_item['Item'].get('TeacherID', {'S': ''})
        studentlist = course_item['Item'].get('StudentList', {'L': []})
        
        if type == 'Teacher': 
            combined = {**location, **schedule, **studentlist}
            return {
                'statusCode': 200,
                'body': json.dumps(combined)
            }
        
        else:
            #student
            #need teacher name
            tname = teacher
            if teacher.get('S', '') != 'unassigned':
                teacher_item = client.get_item(
                    TableName='Users',
                    Key={
                        'Type': {
                            'S': "Teacher",
                        },
                        'UserID': {
                            'S': userid        
                        }
                    }
                )
                if ('Item' in teacher_item):
                    tname = teacher_item['Item'].get('Name', {'S': ''})
                else:
                    tname = "Teacher not found"
            combined = {**location, **schedule, **tname}
            return {
                'statusCode': 200,
                'body': json.dumps(combined)
            }
        
    else:
        return {
            #should not reach this point
            'statusCode': 400,
            'body': json.dumps(f'Course not found')
        }