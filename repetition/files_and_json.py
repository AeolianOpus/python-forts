# files_and_json.py

import json
import csv
from pathlib import Path

DATA_DIR = Path("data")  # default directory for data


def read_text_file():
    """Reads a plain text file."""
    file = DATA_DIR / "example.txt"

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    print("Text content:", content)


def write_text_file():
    """Writes to a text file."""
    file = DATA_DIR / "output.txt"

    with open(file, "w", encoding="utf-8") as f:
        f.write("This is a test file created in Python.\n")


def read_json_file():
    file = DATA_DIR / "data.json"

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("JSON content:", data)


def write_json_file():
    file = DATA_DIR / "generated.json"

    example_data = {"id": 1, "name": "Dataset", "values": [1, 2, 3]}

    with open(file, "w", encoding="utf-8") as f:
        json.dump(example_data, f, indent=2)


def read_csv_file():
    file = DATA_DIR / "sample.csv"

    with open(file, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print("CSV rows:", rows)