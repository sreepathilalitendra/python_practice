
# Day 49: JSON Challenge

import json

# Challenge 1: Create a dictionary
product = {
    "name": "Laptop",
    "price": 45000,
    "brand": "Lenovo",
    "available": True
}

# Challenge 2: Convert dictionary to JSON
json_data = json.dumps(product, indent=4)
print("JSON Data:")
print(json_data)


# Challenge 3: Convert JSON back to Python
data = json.loads(json_data)
print("\nProduct Name:", data["name"])
print("Product Price:", data["price"])


# Challenge 4: Update a value
data["price"] = 42000
print("\nUpdated Price:", data["price"])


# Challenge 5: Save updated data to a file
with open("product.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("Product data saved successfully!")
