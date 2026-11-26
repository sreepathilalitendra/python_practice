
import sqlite3


# Challenge 1: Create college database

connection = sqlite3.connect("college.db")

cursor = connection.cursor()

print("College Database Created Successfully")


# Challenge 2: Create courses table

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    duration TEXT NOT NULL
)
""")

print("Courses Table Created")


# Challenge 3: Add table columns

cursor.execute("PRAGMA table_info(courses)")

columns = cursor.fetchall()

print("\nCourse Table Columns")

for column in columns:
    print(column[1])


# Challenge 4: Insert five courses

courses = [
    (101, "Computer Science", "3 Years"),
    (102, "Mechanical Engineering", "3 Years"),
    (103, "Electrical Engineering", "3 Years"),
    (104, "Civil Engineering", "3 Years"),
    (105, "Electronics Engineering", "3 Years")
]

cursor.executemany("""
INSERT OR IGNORE INTO courses
(course_id, course_name, duration)
VALUES (?, ?, ?)
""", courses)

connection.commit()

print("\nFive Courses Inserted")


# Challenge 5: Display all courses

cursor.execute("SELECT * FROM courses")

all_courses = cursor.fetchall()

print("\nAll Courses")

for course in all_courses:
    print(course)


# Challenge 6: Retrieve one course using ID

search_id = 101

cursor.execute(
    "SELECT * FROM courses WHERE course_id = ?",
    (search_id,)
)

course = cursor.fetchone()

print("\nSearch Result")

if course:
    print(course)
else:
    print("Course Not Found")


# Challenge 7: Display only course names

cursor.execute("SELECT course_name FROM courses")

course_names = cursor.fetchall()

print("\nCourse Names")

for name in course_names:
    print(name[0])


# Challenge 8: Count total courses

cursor.execute("SELECT COUNT(*) FROM courses")

total_courses = cursor.fetchone()[0]

print("\nTotal Courses:", total_courses)


# Challenge 9: Display table structure

cursor.execute("PRAGMA table_info(courses)")

table_info = cursor.fetchall()

print("\nTable Structure")

for column in table_info:
    print(
        "Column:", column[1],
        "| Type:", column[2],
        "| Primary Key:", column[5]
    )


# Challenge 10: Mini Course Database Manager

def add_course(course_id, course_name, duration):

    cursor.execute("""
    INSERT OR IGNORE INTO courses
    (course_id, course_name, duration)
    VALUES (?, ?, ?)
    """, (course_id, course_name, duration))

    connection.commit()

    if cursor.rowcount > 0:
        print("Course Added Successfully")
    else:
        print("Course ID Already Exists")


def display_courses():

    cursor.execute("SELECT * FROM courses")

    records = cursor.fetchall()

    print("\nCourse Database")

    for record in records:
        print(
            "ID:", record[0],
            "| Name:", record[1],
            "| Duration:", record[2]
        )


def search_course(course_id):

    cursor.execute(
        "SELECT * FROM courses WHERE course_id = ?",
        (course_id,)
    )

    result = cursor.fetchone()

    if result:
        print("\nCourse Found:", result)
    else:
        print("\nCourse Not Found")


print("\nMini Course Database Manager")

add_course(106, "Information Technology", "3 Years")

display_courses()

search_course(106)


# Close database connection

connection.close()

print("\nDatabase Connection Closed")
