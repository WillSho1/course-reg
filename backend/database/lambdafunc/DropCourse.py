""" Given: courseid, section, userID
    TODO:
        update enrollment for users and courses tables
        return success message
    User: students
"""

import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    course_id_section = event["course_id_section"]
    cis = course_id_section.split('-')
    courseid = cis[0]
    section = cis[1]
    user = event["UserID"]
    
    #SHOULD NOT NEED TO CHECK ENROLLMENT
    
    #UPDATE TABLES IF PREVIOUS CONDITIONS PASS
    course_item = client.get_item(
            TableName = 'Courses',
            Key={
            'CourseID': {
                'S': courseid
            },
            'Section': {
                'N': section
            }
        }
    )
    
    if "Item" in course_item:
            studentlist = course_item['Item'].get('StudentList', {'L': []}).get('L', [])
            enrollment = course_item['Item'].get('Enrollment', {}).get('N', '0')
            student_list = [student for student in studentlist if student['S'] != user]
            enrollment = len(student_list)
    else:
        return {
            #should never enter this
            'statusCode': 400,
            'body': json.dumps(f'{course_id_section} not found')
        }
            
    
    response = client.update_item(
        TableName='Courses',
        Key={
            'CourseID': {
                'S': courseid
            },
            'Section': {
                'N': section
            }
        },
        UpdateExpression='SET Enrollment = :enrollment, StudentList = :student_list',
        ExpressionAttributeValues={
            ':enrollment': {
                'N': str(enrollment)
            },
            ':student_list': {
                    'L': student_list
            }
        }
    )
    
    user_item = client.get_item(
            TableName = 'Users',
            Key={
            'Type': {
                'S': "Student"
            },
            'UserID': {
                'S': user
            }
        }
    )
    
    if "Item" in user_item:
            courselist = user_item['Item'].get('Enrollment', {'L': []}).get('L', [])
            course_list = [classes for classes in courselist if classes['S'] != course_id_section]
    else:
        return {
            #should never enter this
            'statusCode': 400,
            'body': json.dumps(f'{user} not found')
        }
    
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
        UpdateExpression='SET Enrollment = :enrollment',
        ExpressionAttributeValues={
            ':enrollment': {
                'L': course_list
            }
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully dropped {course_id_section}!')
    }