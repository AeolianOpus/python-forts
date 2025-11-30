# oop_basics.py

class Record:
    """
    Simple class representing a data record.
    Shows constructor, attributes, methods, and __repr__.
    """

    def __init__(self, id: int, value: float):
        self.id = id
        self.value = value

    def double(self):
        """Returns the value multiplied by 2."""
        return self.value * 2

    def __repr__(self):
        return f"Record(id={self.id}, value={self.value})"


class LabeledRecord(Record):
    """Example of inheritance: a Record with an additional label"""

    def __init__(self, id: int, value: float, label: str):
        super().__init__(id, value)
        self.label = label

    def __repr__(self):
        return f"LabeledRecord(id={self.id}, value={self.value}, label='{self.label}')"
