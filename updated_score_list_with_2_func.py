def classify_score(score):
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


def get_score():
    while True:
        try:
            score = int(input("Enter a score between 0 and 100: "))
            if 0 <= score <= 100:
                return score
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


name = input("Enter your name: ")
score = get_score()
result = classify_score(score)

print(f"{name} scored {score}: {result}")