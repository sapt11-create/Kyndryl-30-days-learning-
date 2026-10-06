n = int(input("How many elements do you want to enter? "))

numbers = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)

print("\nOriginal dataset:", numbers)

# Built-in sort
numbers.sort()

print("Sorted dataset:", numbers)

""" 
1. Output of the following here we will take bubble sort as an example to sort the dataset.
Original dataset: [45, 12, 78, 23, 9]
Sorted dataset: [9, 12, 23, 45, 78]
2. Trace Bubble Sort by hand

Take:

[45, 12, 78, 23, 9]

Bubble Sort compares two neighboring values and swaps them if they are in the wrong order.

Pass 1

45 > 12  → swap → [12, 45, 78, 23, 9]
78 > 23  → swap → [12, 45, 23, 78, 9]
78 > 9   → swap → [12, 45, 23, 9, 78]

Largest value 78 has moved to the end.

Pass 2

12 < 45  → no swap → [12, 45, 23, 9, 78]
45 > 23  → swap    → [12, 23, 45, 9, 78]
45 > 9   → swap    → [12, 23, 9, 45, 78]

Pass 3

12 < 23  → no swap → [12, 23, 9, 45, 78]
23 > 9   → swap    → [12, 9, 23, 45, 78]

Pass 4

12 > 9   → swap → [9, 12, 23, 45, 78]

Final sorted dataset:

[9, 12, 23, 45, 78] """