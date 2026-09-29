records = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 58),
    ("David", 45),
    ("Eve", 91)
]

for name, score in records:
    if score >= 80:
        result = "Excellent"
    elif score >= 60:
        result = "Good"
    elif score >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(name, score, result)