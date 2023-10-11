import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

def createtable():

    # Define the table schema
    table_name = 'Users'
    key_schema = [
        {
            'AttributeName': 'userID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'password',
            'KeyType': 'RANGE'
        },
        # Add additional entries for sort keys if needed
    ]

    attribute_definitions = [
        {
            'AttributeName': 'userID',
            'AttributeType': 'S'  #userID
        },
        {
            'AttributeName': 'password',
            'AttributeType': 'S'  #hashed of course
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


    """Other attributes to include:
            user type
            taken courses
            enrolled courses"""