# Challenge 1
# Create a set containing 5 programming languages
# and print the set.

languages = {"Python", "Java", "C", "C++", "JavaScript"}
print(languages)


# Challenge 2
# Create a set containing duplicate values
# and print the set.

colors = {
    "Red",
    "Green",
    "Orange",
    "Purple",
    "Red",
    "White",
    "Yellow",
    "Green",
    "Orange"
}
print(colors)


# Challenge 3
# Create a set containing duplicate numbers
# and print the set.

numbers = {1, 2, 3, 4, 5, 6, 2, 4, 5, 6, 2, 1, 3, 2, 5, 6}
print(numbers)


# Challenge 4
# Add a new programming language using add().

languages.add("HTML")
print(languages)


# Challenge 5
# Remove one programming language using remove().

languages.remove("Java")
print(languages)


# Challenge 6
# Check whether "Python" exists in the set
# and print the length of the set.

print("Python" in languages)

print(len(languages))


# Challenge 7
# Print every programming language
# using a for loop.

for language in languages:
    print(language)
    