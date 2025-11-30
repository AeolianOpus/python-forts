# main.py

from datastructures import (
    demo_basic_types,
    demo_collections,
    demo_comprehensions,
    demo_unpacking,
)
from functions import (
    greet,
    add,
    demo_args,
    demo_kwargs,
    multiple_returns,
)
from files_and_json import (
    read_text_file,
    write_text_file,
    read_json_file,
    write_json_file,
    read_csv_file,
)
from oop_basics import Record, LabeledRecord
from error_handling import demo_error_handling, validate_positive


def run_all():
    print("\n--- DATA STRUCTURES ---")
    demo_basic_types()
    demo_collections()
    demo_comprehensions()
    demo_unpacking()

    print("\n--- FUNCTIONS ---")
    print(greet("Markus"))
    print("Add:", add(3, 4))
    demo_args(1, 2, 3)
    demo_kwargs(name="Alice", age=30)
    print("Multiple return:", multiple_returns())

    print("\n--- FILES & JSON ---")
    write_text_file()
    read_text_file()
    write_json_file()
    read_json_file()
    read_csv_file()

    print("\n--- OOP ---")
    r = Record(1, 10.0)
    print("Record:", r)
    print("Double:", r.double())

    lr = LabeledRecord(2, 5.0, "Temperature")
    print("Labeled:", lr)

    print("\n--- ERROR HANDLING ---")
    demo_error_handling("hej")
    try:
        validate_positive(-5)
    except Exception as e:
        print("Caught exception:", e)


if __name__ == "__main__":
    run_all()
