import json
import random
import string

# Function to generate a random alphanumeric string of a specified length
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_random_stringL(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_random_stringU(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

# Function to generate random schedule data
def generate_random_schedule():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    schedule = {}
    for day in days_of_week:
        start_time = f"{random.randint(8, 16)}:00"
        end_time = f"{random.randint(8, 16)}:00"
        schedule[day] = f"{start_time}-{end_time}"
    return schedule

# Generate 100 unique course examples with random attributes
courses = []
for _ in range(300):
    capacity = random.randint(15, 100)
    enrollment = random.randint(0, capacity)
    course = {
        "CourseID":  '{} {}'.format(generate_random_stringU(4), random.randint(1000, 6000)),
        "Section": '{}'.format(random.randint(0, 20)),
        "Capacity": capacity,
        "Description": generate_random_string(50),
        "Enrollment": enrollment,
        "Location": generate_random_stringU(4) + ' {}'.format(random.randint(0, 400)),
        "Name": generate_random_string(10),
        "Prerequisites": [(generate_random_stringU(4) + ' {}'.format(random.randint(1000, 6000))) for _ in range(random.randint(0, 3))],
        "Schedule": generate_random_schedule(),
        "StudentList": ['{}{}'.format(generate_random_stringL(3), random.randint(10000, 24000)) for _ in range(enrollment)],
        "TeacherID": '{}{}'.format(generate_random_stringL(3), random.randint(10000, 24000))
    }
    courses.append(course)

# Save the course data to a JSON file
with open('courses.json', 'w') as json_file:
    json.dump(courses, json_file, indent=2)

print("courses.json file created with 100 course examples with fully random attributes.")
