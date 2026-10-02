# Day 25 - Python OS Module

import os


# Current Working Directory
print(os.getcwd())


# List Files and Folders
print(os.listdir())


# Create a Folder
if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")
    print("Folder created successfully!")
else:
    print("Folder already exists!")


# Check Whether a File Exists
print(os.path.exists("practice.py"))


# Check File or Folder
print(os.path.isfile("practice.py"))
print(os.path.isdir("MyFolder"))


# Join File Paths
folder = "MyFolder"
file = "notes.txt"

path = os.path.join(folder, file)

print(path)


# Get File Name
file_path = "Day25/practice.py"

print(os.path.basename(file_path))


# Get File Name and Extension
print(os.path.splitext(file_path))