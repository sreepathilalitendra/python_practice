
# Day 50 Challenge: Product Inventory

import csv

# Step 1: Write product data to a CSV file
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Product", "Price", "Quantity"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({
        "Product": "Laptop",
        "Price": 45000,
        "Quantity": 2
    })

    writer.writerow({
        "Product": "Mouse",
        "Price": 500,
        "Quantity": 5
    })

    writer.writerow({
        "Product": "Keyboard",
        "Price": 1200,
        "Quantity": 3
    })

print("Products saved successfully!")

# Step 2: Read product data and calculate total value
print("\n----- PRODUCT INVENTORY -----")

grand_total = 0

with open("products.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for product in reader:
        name = product["Product"]
        price = float(product["Price"])
        quantity = int(product["Quantity"])

        total_value = price * quantity
        grand_total += total_value

        print("Product:", name)
        print("Price: ₹", price)
        print("Quantity:", quantity)
        print("Total Value: ₹", total_value)
        print()

print("Grand Total Value: ₹", grand_total)
