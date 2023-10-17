import json
import random
import string


class SharedCourse:
    def __init__(self, courses, tlist):
        #shared information
        self.CourseID = '{} {}'.format(generate_random_stringU(random.randint(3, 4)), random.randint(1000, 6400))
        self.Name = generate_random_string(10)
        self.description = generate_random_string(50)
        self.prereqs = [courses[random.randint(0, 19)] for i in range(random.randint(0, 3))]
        #building realistic sections
        self.count = 0
        self.posteachers = [tlist[random.randint(0, 39)] for i in range(3)]

class User:
    def __init__(self, type, prereqs=[]):
        self.type = type
        self.UserID = '{}{}'.format(generate_random_stringL(3), random.randint(10000, 24000))
        self.name = '{} {}'.format(generate_random_string(random.randint(3, 9)), generate_random_string(random.randint(3, 9)))
        self.password = generate_random_string(13)

        self.taken = []
        if type == 'Student':
            self.taken = [prereqs[random.randint(0, 19)] for i in range(random.randint(0, 3))]
        self.enrollment = []

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

#make list of 20 prereqs
prereqs = []
for i in range(20):
    prereqs.append('{} {}'.format(generate_random_stringU(4), random.randint(1000, 6000)))

#make users
stulist = []
for i in range(1000):
    student = User('Student', prereqs)
    stulist.append(student)

teachlist = []
for i in range(40):
    teacher = User('Teacher')
    teachlist.append(teacher)

adminlist = []
for i in range(15):
    admin = User('Admin')
    adminlist.append(admin)

# Generate 300 unique course examples with random attributes
courselist = []
for i in range(75):
    newcourse = SharedCourse(prereqs, teachlist)
    courselist.append(newcourse)

popcourses = []
for i in range(300):
    course = courselist[random.randint(0, 74)]
    course.count += 1
    teacher = course.posteacher[random.randint(0, 2)]
    teacher.enrollment.append(course.CourseID)

    topop = {
        "CourseID":  course.CourseID,
        "Section": '{}'.format(course.count),
        "Capacity": random.randint(15, 50),
        "Description": course.description,
        "Enrollment": 0,
        "Location": generate_random_stringU(4) + ' {}'.format(random.randint(0, 400)),
        "Name": course.Name,
        "Prerequisites": course.prereqs,
        "Schedule": generate_random_schedule(),
        "StudentList": [],
        "TeacherID": teacher.UserID
    }
    popcourses.append(topop)



# Save the course data to a JSON file
with open('courses.json', 'w') as json_file:
    json.dump(popcourses, json_file, indent=2)

print("courses.json file created with 100 course examples with fully random attributes.")
