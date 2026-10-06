choice = int(input("Enter 1 for Stack or 2 for Queue: "))

n = int(input("How many items do you want to add? "))

items = []

for i in range(n):
    item = input("Enter an item: ")
    items.append(item)

if choice == 1:
    print("Stack:", items)
    removed_item = items.pop()
    print("Removed item:", removed_item)
    print("Stack after removal:", items)

elif choice == 2:
    print("Queue:", items)
    removed_item = items.pop(0)
    print("Removed item:", removed_item)
    print("Queue after removal:", items)

else:
    print("Invalid choice")