# 1. Write content into a file

with open("sample.txt", "w") as file:
    file.write("Hello, Python!")


# 2. Read content from a file

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


# 3. Append content to a file

with open("sample.txt", "a") as file:
    file.write("\nWelcome to CodeMonolith!")


# 4. Read the updated content

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


# 5. Write student details

with open("student.txt", "w") as file:
    file.write("Name: Lalitendra\n")
    file.write("Course: Diploma CSE\n")


# 6. Read student details

with open("student.txt", "r") as file:
    print(file.read())


# 7. Write course details

with open("course.txt", "w") as file:
    file.write("Python Programming")


# 8. Append text to course.txt

with open("course.txt", "a") as file:
    file.write("\nPython Developer")


# 9. Read a file line by line

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())


# 10. Create a file only if it doesn't exist

try:
    with open("notes.txt", "x") as file:
        file.write("My Python notes")

    print("File created successfully!")

except FileExistsError:
    print("File already exists!")