
import sqlite3


# Example 1: Import SQLite

print("Python SQLite Database")


# Example 2: Create database connection

connection = sqlite3.connect("students.db")

print("Database Connected Successfully")


# Example 3: Create cursor

cursor = connection.cursor()


# Example 4: Create a table

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    course TEXT,
    age INTEGER
)
""")

print("Students Table Created")


# Example 5: Insert one student

cursor.execute("""
INSERT INTO students (name, course, age)
VALUES (?, ?, ?)
""", ("Lalitendra", "Diploma CSE", 18))

connection.commit()

print("Student Inserted Successfully")


# Example 6: Insert multiple students

students = [
    ("Rahul", "Diploma CSE", 19),
    ("Arjun", "Diploma ECE", 20),
    ("Priya", "Diploma CSE", 18)
]

cursor.executemany("""
INSERT INTO students (name, course, age)
VALUES (?, ?, ?)
""", students)

connection.commit()

print("Multiple Students Inserted")


# Example 7: Retrieve all students

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

print("\nAll Student Records")

for record in records:
    print(record)


# Example 8: Retrieve one student

cursor.execute(
    "SELECT * FROM students WHERE id = ?",
    (1,)
)

student = cursor.fetchone()

print("\nSingle Student Record")
print(student)


# Example 9: Retrieve selected columns

cursor.execute("""
SELECT name, course
FROM students
""")

records = cursor.fetchall()

print("\nStudent Names and Courses")

for record in records:
    print(record)


# Example 10: Count student records

cursor.execute("SELECT COUNT(*) FROM students")

total_students = cursor.fetchone()[0]

print("\nTotal Students:", total_students)


# Example 11: Display table information

cursor.execute("PRAGMA table_info(students)")

columns = cursor.fetchall()

print("\nTable Columns")

for column in columns:
    print(column)


# Example 12: Close database connection

connection.close()

print("\nDatabase Connection Closed")
