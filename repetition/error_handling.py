# error_handling.py

class DataError(Exception):
    """Custom exception for course demonstration."""
    pass


def demo_error_handling(value):
    try:
        number = int(value)
        print("Converted number:", number)

    except ValueError:
        print("Could not convert the value to int!")

    finally:
        print("This code always runs.")


def validate_positive(number: int):
    """Example of when you raise an exception yourself."""
    if number <= 0:
        raise DataError(f"The number {number} must be greater than 0.")

    return number
