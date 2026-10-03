# CHALLENGE 1:
# Create student.txt and write your name

with open("student.txt", "w") as file:
    file.write("Lalitendra")


# CHALLENGE 2:
# Read student.txt and print its content

with open("student.txt", "r") as file:
    print(file.read())


# CHALLENGE 3:
# Write your course name into course.txt

with open("course.txt", "w") as file:
    file.write("Diploma CSE")


# CHALLENGE 4:
# Append Python Developer to course.txt

with open("course.txt", "a") as file:
    file.write("\nPython Developer")


# CHALLENGE 5:
# Read a file one line at a time

with open("course.txt", "r") as file:
    for line in file:
        print(line.strip())


# CHALLENGE 6:
# Create notes.txt only if it doesn't exist

try:
    with open("notes.txt", "x") as file:
        file.write("My Python notes")

    print("notes.txt created successfully!")

except FileExistsError:
    print("notes.txt already exists!")