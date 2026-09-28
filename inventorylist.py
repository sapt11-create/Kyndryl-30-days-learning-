inventory = ["Laptop", "Mouse", "Keyboard", "Monitor"]

item_details = {
    "Laptop": {"price": 75000, "quantity": 5},
    "Mouse": {"price": 800, "quantity": 10},
    "Keyboard": {"price": 1500, "quantity": 7},
    "Monitor": {"price": 12000, "quantity": 4}
}

print("Inventory:")
for item in inventory:
    print(item)

print("\nItem Details:")
for item, details in item_details.items():
    print(item, "- Price:", details["price"], "Quantity:", details["quantity"])