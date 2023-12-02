""" Use Case: An admin adding a section to a database.
    Users: Admins
    Type: POST
    Endpoint: ./adminhomepage/sections/add
    Provide in request:
        Body:
        {
            "CourseID": '',
            "UserID": '',
            "Section": N
        }
    TODO:
        Validate input data (e.g., check for missing fields, validate CourseID format).
        Check if the course already exists in the database.
        Add the new course to the Courses table.
    Response:
        Strings signifying success or failure
"""

import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    course_id = event.get("CourseID")
    title = event.get("Title")
    description = event.get("Description")
    prereqs = event.get("Prerequisites", [])
    capacity = event.get("Capacity")
    section = event.get("Section")

    if not all([course_id, title, description, capacity, section]):
        return response(400, 'Missing required course details')
    try:
        section = int(section)
    except ValueError:
        return response(400, 'Section must be a number')

    existing_course = client.get_item(
        TableName='Courses',
        Key={
            'CourseID': {'S': course_id},
            'Section': {'N': str(section)}
        }
    )

    if 'Item' in existing_course:
        return response(400, f'Course {course_id} Section {section} already exists')

    client.put_item(
        TableName='Courses',
        Item={
            'CourseID': {'S': course_id},
            'Section': {'N': str(section)}, 
            'Title': {'S': title},
            'Description': {'S': description},
            'Prerequisites': {'L': [{'S': prereq} for prereq in prereqs]},
            'Capacity': {'N': str(capacity)}
        }
    )

    return response(200, f'Course {course_id} Section {section} added successfully')

def response(status_code, message):
    return {
        'statusCode': status_code,
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
