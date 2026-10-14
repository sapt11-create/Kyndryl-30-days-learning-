
import argparse


def classify_score(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 50:
        return "Pass"
    return "Fail"


def main():
    parser = argparse.ArgumentParser(description="Classify a student's score.")
    parser.add_argument(
        "--score",
        type=int,
        required=True,
        help="Student score between 0 and 100"
    )

    args = parser.parse_args()

    try:
        result = classify_score(args.score)
        print(f"Score: {args.score}")
        print(f"Result: {result}")
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
