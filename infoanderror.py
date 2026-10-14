import logging

logging.basicConfig(
    filename="division.log",
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def division():
    logger.info("Starting division.")

    try:
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))

    except ValueError:
        logger.error("Invalid input. Please enter numeric values.")
        print("Invalid input. Please enter numbers.")
        return

    if divisor == 0:
        logger.error("Attempted division by zero.")
        print("Cannot divide by zero.")
        return

    result = dividend / divisor

    logger.info("Division completed successfully. Result: %s", result)
    print("Result:", result)


division()