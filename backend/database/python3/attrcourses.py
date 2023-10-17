import boto3


# Initialize a session using Amazon DynamoDB.
dynamodb = boto3.resource('dynamodb')

def addattr():
    # Define the name of the existing table.
    table_name = 'Courses'

    # Update the table with the new attribute.
    table = dynamodb.Table(table_name)

    # Update the table's attribute definitions.
    response = table.update(
        AttributeDefinitions=[
            {
                'AttributeName': 'Name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Description',
                'AttributeType': 'S'
                
            },
            {
                'AttributeName': 'Prerequisites',
                'AttributeType': 'S'        #need parsing
            },
            {
                'AttributeName': 'TeacherID',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Location',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Schedule',
                'AttributeType': 'S'        #need parsing
            },
            {
                'AttributeName': 'Capacity',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'Enrollment',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'StudentList',
                'AttributeType': 'S'        #need parsing
            },
        ]
    )

if __name__ == "__main__":
    addattr()