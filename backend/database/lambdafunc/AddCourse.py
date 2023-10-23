""" Given: UserID, CourseID, Section, 
    TODO:
        update users and courses tables for enrollment
        return a success message
    Users: Students
"""

import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    user = event["UserID"]
    course = event["CourseID"]
    section = event["Section"]
    
    # Check if the user is already enrolled in the course
    course_id_section = f"{course}-{section}"
    
    user_item = client.get_item(
        TableName='Users',
        Key={
            'Type': {
                'S': "Student",
            },
            'UserID': {
                'S': user        
            }
        }
    )
    if 'Item' in user_item:
        enrollment = user_item['Item'].get('Enrollment', {'L': []}).get('L', [])
        clist = [item.get('S') for item in enrollment]
        for classes in clist:
            if course in classes:
                return {
                    'statusCode': 400,
                    'body': json.dumps(f'Already enrolled in {course_id_section}.')
                }
    else:
        #should never enter this
        return {
            'statusCode': 400,
            'body': json.dumps('User not found')
        }
        
    #UPDATE TABLES IF THE STUDENT IS NOT ALREADY ENROLLED
    response = client.update_item(
        TableName='Courses',
        Key={
            'CourseID': {
                'S': course
            },
            'Section': {
                'N': str(section) 
            }
        },
        UpdateExpression='SET Enrollment = Enrollment + :enrollment, StudentList = list_append(StudentList, :userId)',
        ExpressionAttributeValues={
            ':enrollment': {
                'N': '1'  # Increment by 1
            },
            ':userId': {
                'L': [{'S': user}]
            }
        }
    )
    response2 = client.update_item(
        TableName='Users',
        Key={
            'Type': {
                'S': "Student",
            },
            'UserID': {
                'S': user        
            }
        },
        UpdateExpression='SET Enrollment = list_append(if_not_exists(Enrollment, :emptyList), :courseIdSection)',
        ExpressionAttributeValues={
            ':emptyList': {
                'L': []
            },
            ':courseIdSection': {
                'L': [{'S': course_id_section}]
            }
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully enrolled in {course_id_section}!')
    }