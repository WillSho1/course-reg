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
    capacity = event.get("Capacity")
    section = event.get("Section")
    enrollment = event.get("Enrollment")
    location = event.get("Location")
    schedule = event.get("Schedule")
    teacher_id = event.get("TeacherID")

    # Validate input data
    if not all([course_id, capacity, section, enrollment, location, schedule, teacher_id]):
        return response(400, 'Missing required course details')

    # Validate section is a number
    try:
        section = int(section)
    except ValueError:
        return response(400, 'Section must be a number')

    # Check if the course already exists
    existing_course = client.get_item(
        TableName='Courses',
        Key={
            'CourseID': {'S': course_id},
            'Section': {'N': str(section)}
        }
    )

    if 'Item' in existing_course:
        return response(400, f'Course {course_id} Section {section} already exists')

    # Add the new course to the Courses table
    client.put_item(
        TableName='Courses',
        Item={
            'CourseID': {'S': course_id},
            'Section': {'N': str(section)},
            'Capacity': {'N': str(capacity)},
            'Enrollment': {'N': str(enrollment)},
            'Location': {'S': location},
            'Schedule': {'M': schedule},
            'TeacherID': {'S': teacher_id},
            'StudentList': {'L': []}  # Initializing StudentList as an empty list
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