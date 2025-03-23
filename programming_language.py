"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""
    def __init__(self, name: str, reflection: bool, pointer_arithmetic: bool):
        """
        Initialize a new ProgrammingLanguage instance.
        """
        self.name = name
        self.reflection = reflection
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """
        Return a string representation of the ProgrammingLanguage instance.
        """
        return (f"Language: {self.name}, Reflection: {self.reflection}, "
                f"Pointer Arithmetic: {self.pointer_arithmetic}")

    def __repr__(self):
        """
        Return an unambiguous string representation of the ProgrammingLanguage instance.
        """
        return (f"ProgrammingLanguage(name='{self.name}', reflection={self.reflection}, "
                f"pointer_arithmetic={self.pointer_arithmetic})")
