# Day 14 - Strings

name = "Sreepathi Lalitendra"
language = "Python"
print(name)
print(language)


# String Indexing

name = "python"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])


# Negative Indexing

name = "python"
print(name[-1])
print(name[-2])


# String Length - len()

name = "python"
print(len(name))


# String Slicing

name = "python"
print(name[0:3])


# Upper Case

name = "python"
print(name.upper())


# Lower Case

name = "PYTHON"
print(name.lower())


# Remove Extra Space - strip()

name = "   python    "
print(name.strip())


# Replace Text

name = "I like Java"
new_name = name.replace("Java", "Python")
print(new_name)


# Check Text

name = "python"
print("python" in name)
print("Java" in name)