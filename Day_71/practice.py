
from pathlib import Path

# Challenge 1: Create a folder
folder = Path("MyProjects")
folder.mkdir(exist_ok=True)

print("Folder created:", folder)


# Challenge 2: Create about.txt inside the folder
file_path = folder / "about.txt"

file_path.touch(exist_ok=True)

print("File created:", file_path)


# Challenge 3: Write personal and course information
file_path.write_text(
    "Name: Lalitendra\n"
    "Course: Diploma CSE\n"
    "College: St. Mary's Group of Institutions",
    encoding="utf-8"
)

print("Information saved successfully")


# Challenge 4: Read and display file contents
content = file_path.read_text(encoding="utf-8")

print("\nFile contents:")
print(content)


# Challenge 5: Check whether about.txt exists
if file_path.exists():
    print("\nabout.txt exists")
else:
    print("\nabout.txt does not exist")


# Challenge 6: Display file name and extension
print("\nFile name:", file_path.name)
print("Extension:", file_path.suffix)


# Challenge 7: Create three text files and list them
for number in range(1, 4):
    text_file = folder / f"file{number}.txt"
    text_file.write_text(
        f"This is text file {number}",
        encoding="utf-8"
    )

print("\nText files:")

for item in folder.glob("*.txt"):
    print(item.name)


# Challenge 8: Find all Python files
print("\nPython files:")

for item in Path(".").glob("*.py"):
    print(item.name)


# Challenge 9: Rename a text file
old_file = folder / "file1.txt"
new_file = folder / "renamed_file.txt"

if old_file.exists():
    old_file.rename(new_file)
    print("\nFile renamed successfully:", new_file.name)


# Challenge 10: Simple File Manager
print("\nSimple File Manager")

current_folder = Path(".")

for item in current_folder.iterdir():

    if item.is_file():
        print("FILE:", item.name)

    elif item.is_dir():
        print("FOLDER:", item.name)
