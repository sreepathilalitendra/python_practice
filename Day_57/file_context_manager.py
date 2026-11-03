
# Day 57: File Context Manager

# Open a file using the with statement

with open("student.txt", "w") as file:
    file.write("Name: Lalitendra\n")
    file.write("Course: Diploma CSE\n")
    file.write("Subject: Python\n")

print("File written successfully!")


# Read the file

with open("student.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)


# Check whether the file is closed

print("Is file closed?", file.closed)
