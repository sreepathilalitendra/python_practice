
from pathlib import Path

# Example 1: Create a path
file_path = Path("sample.txt")

print("File path:", file_path)


# Example 2: Check whether a path exists
print("Exists:", file_path.exists())


# Example 3: Check file and directory
print("Is file:", file_path.is_file())
print("Is directory:", file_path.is_dir())


# Example 4: Create a folder
folder = Path("Python_Files")

folder.mkdir(exist_ok=True)

print("Folder created:", folder)


# Example 5: Write text into a file
file_path.write_text(
    "Welcome to Python pathlib!\nLearning filesystem operations.",
    encoding="utf-8"
)

print("Data written successfully")


# Example 6: Read file contents
content = file_path.read_text(encoding="utf-8")

print("\nFile content:")
print(content)


# Example 7: Get file information
print("\nFile name:", file_path.name)
print("File extension:", file_path.suffix)
print("Parent folder:", file_path.parent)


# Example 8: Create another file inside a folder
new_file = folder / "student.txt"

new_file.write_text(
    "Name: Lalitendra\nCourse: Diploma CSE",
    encoding="utf-8"
)

print("\nNew file created:", new_file)


# Example 9: List folder contents
print("\nFolder contents:")

for item in Path(".").iterdir():
    print(item)


# Example 10: Find Python files
print("\nPython files:")

for item in Path(".").glob("*.py"):
    print(item)


# Example 11: Search Python files recursively
print("\nAll Python files in subfolders:")

for item in Path(".").rglob("*.py"):
    print(item)


# Example 12: Rename a file
old_file = Path("sample.txt")
renamed_file = Path("python_notes.txt")

old_file.rename(renamed_file)

print("\nFile renamed:", renamed_file)


# Example 13: Delete a file
if renamed_file.exists():
    renamed_file.unlink()
    print("File deleted successfully")
