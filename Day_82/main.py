
import sqlite3

# Connect to database
connection = sqlite3.connect("college.db")

cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

connection.commit()

# Insert student records
try:
    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        ("Lalitendra", 85)
    )

    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        ("Rahul", 90)
    )

    # Save changes
    connection.commit()

    print("Records inserted successfully!")

except sqlite3.Error as error:
    connection.rollback()
    print("Database error:", error)

finally:
    cursor.close()
    connection.close()
    print("Database connection closed.")
