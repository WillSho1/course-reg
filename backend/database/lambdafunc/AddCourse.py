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
    course_id_section = f"{course}-{section}"
    
    #CHECK: ENROLLMENT, PREREQS, COMPLETED
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
    subj = course.split()[0]
    course_item = client.get_item(
        TableName = 'Subjects',
        Key = {
            'subject': {
                'S': subj,
            },
            'courseid': {
                'S': course
            }
        }
    )
    if ('Item' in user_item):
        if ('Item' in course_item):
            prereqs = course_item['Item'].get('Prereqs', {'L': []}).get('L', [])
            taken = user_item['Item'].get('Completed', {'L': []}).get('L', [])
            enrollment = user_item['Item'].get('Enrollment', {'L': []}).get('L', [])
            
            clist = [item.get('S') for item in enrollment]
            takenlist = [item.get('S') for item in taken]
            prelist = [item.get('S') for item in prereqs]
            #PREREQS
            notin = []
            for i in prelist:
                if i not in takenlist:
                    notin.append(i)
            if len(notin) > 0:
                return {
                    'statusCode': 400,
                    'body': json.dumps(f'Missing Prereqs: {notin}')
                }
            #TAKEN
            for classes in takenlist:
                if course in classes:
                    return {
                        'statusCode': 400,
                        'body': json.dumps(f'Already completed {course}.')
                    }
            #ALREADY ENROLLED
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
                'body': json.dumps('Course not found')
            }
    else:
        #should never enter this
        return {
            'statusCode': 400,
            'body': json.dumps('User not found')
        }
        
    #CHECK: CAPACITY
    course_item1 = client.get_item(
        TableName='Courses',
        Key={
            'CourseID': {
                'S': course,
            },
            'Section': {
                'N': section        
            }
        }
    )
    if ('Item' in course_item1):
        cap = course_item1['Item'].get('Capacity', {}).get('N', '0')
        enrollcount = course_item1['Item'].get('Enrollment', {}).get('N', '0')
        if cap == enrollcount:
            return {
                'statusCode': 400,
                'body': json.dumps(f'{course_id_section} is currently full: {enrollcount}/{cap}.')
            }
    else:
        return {
            #should never entert this
            'statusCode': 400,
            'body': json.dumps(f'{course_id_section} not found')
        }
        
        
    #UPDATE TABLES IF PREVIOUS CONDITIONS PASS
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