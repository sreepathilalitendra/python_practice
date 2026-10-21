# Day 44: Checking __name__

print("Current name:", __name__)

if __name__ == "__main__":
    print("This file is running directly")
else:
    print("This file was imported")