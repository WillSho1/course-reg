import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

def createtable():

    # Define the table schema
    table_name = 'Courses'
    key_schema = [
        {
            'AttributeName': 'CourseID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Section',
            'KeyType': 'RANGE'
        },
        # Add additional entries for sort keys if needed
    ]

    attribute_definitions = [
        {
            'AttributeName': 'CourseID',
            'AttributeType': 'S'  #CourseID
        },
        {
            'AttributeName': 'Section',
            'AttributeType': 'S'  #Section number
        },
    ]

    # Provisioned throughput settings (adjust as needed)
    read_capacity_units = 1
    write_capacity_units = 1

    # Create the table
    response = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput={
            'ReadCapacityUnits': read_capacity_units,
            'WriteCapacityUnits': write_capacity_units
        }
    )

    # Wait for the table to be created (optional)
    response.wait_until_exists()
    print("Table: {table_name} created!")


if __name__ == "__main__":
    createtable()


    """{
            'AttributeName': 'Time',
            'AttributeType': 'S'  #Map times to days of the week
                                #need a script to parse this information
        },
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'  #Name of course
        },
        {
            'AttributeName': 'Professor',
            'AttributeType': 'S'  #Professor
        },
        {
            'AttributeName': 'Description',
            'AttributeType': 'S'  #Short Description of the course
        },
        {
            'AttributeName': 'PreReqs',
            'AttributeType': 'S'  #list of pre-reqs
                                    #need script to parse (should be simple)
        },
        {
            'AttributeName': 'StudentList',
            'AttributeType': 'S'  #List of students enrolled
                                    #need script to parse (can be same as prereqs)
        },
        {
            'AttributeName': 'EnrollmentCap',
            'AttributeType': 'N'  #enrollment cap
        },
        {
            'AttributeName': 'MajorReqs',
            'AttributeType': 'S'  #List of allowed majors
                                    #need script to parse (should be simple)
        },"""