# functions.py

def greet(name: str = "Student") -> str:
    """
    Returns a greeting.
    Demonstrates default parameters + type hints.
    """
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b


def demo_args(*args):
    """Shows how *args works."""
    print("Args:", args)


def demo_kwargs(**kwargs):
    """Shows how **kwargs works."""
    print("Kwargs:", kwargs)


def multiple_returns():
    """Returns two values as a tuple."""
    return "Alice", 25


def imported_function_example():
    print("This is executed from an imported module!")
