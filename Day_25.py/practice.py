# Challenge 1 - Current Directory
import os

print(os.getcwd())


# Challenge 2 - List Files and Folders
print(os.listdir())


# Challenge 3 - Create a Folder
if not os.path.exists("PythonPractice"):
    os.mkdir("PythonPractice")
    print("Folder created successfully!")
else:
    print("Folder already exists!")


# Challenge 4 - Check Path
print(os.path.exists("practice.py"))


# Challenge 5 - Check File
print(os.path.isfile("practice.py"))


# Challenge 6 - Check Folder
print(os.path.isdir("PythonPractice"))


# Challenge 7 - Join Paths
folder = "PythonPractice"
file = "notes.txt"

path = os.path.join(folder, file)

print(path)


# Challenge 8 - Get File Name
file_path = "PythonPractice/notes.txt"

print(os.path.basename(file_path))


# Challenge 9 - Get File Extension
file_path = "practice.py"

print(os.path.splitext(file_path))


# Challenge 10 - Mini Project
folder_name = "PythonPractice"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created successfully!")
else:
    print("Folder already exists!")

print("Files and folders in the current directory:")
print(os.listdir())