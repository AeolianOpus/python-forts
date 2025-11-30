# datastructures.py

def demo_basic_types():
    number = 10
    text = "Hello"
    pi = 3.14
    flag = True

    print("Number:", number)
    print("Text:", text)
    print("Float:", pi)
    print("Boolean:", flag)


def demo_collections():
    # List (mutable)
    numbers = [1, 2, 3, 4]

    # Tuple (immutable)
    coords = (10, 20)

    # Set (unika värden)
    tags = {"python", "data", "python"}

    # Dict (key-value)
    user = {"id": 1, "name": "Alice"}

    print("List:", numbers)
    print("Tuple:", coords)
    print("Set:", tags)
    print("Dict:", user)


def demo_comprehensions():
    numbers = [1, 2, 3, 4, 5]

    # List comprehension
    squared = [n * 2 for n in numbers]

    # Dict comprehension
    squared_dict = {n: n*n for n in numbers}

    # Set comprehension
    evens = {n for n in numbers if n % 2 == 0}

    print("Squared:", squared)
    print("Squared dict:", squared_dict)
    print("Evens:", evens)


def demo_unpacking():
    point = (10, 20)
    x, y = point  # unpack tuple

    print("x =", x, "| y =", y)

    # Star operator *
    a, *rest = [1, 2, 3, 4, 5]
    print("a =", a, "| rest =", rest)
