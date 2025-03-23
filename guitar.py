# guitar.py

class Guitar:
    """
    Class to represent a Guitar with a name, year, and cost.
    """
    def __init__(self, name, year, cost):
        """
        Initialize a new Guitar instance.
        """
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """
        Return a string representation of the Guitar.
        """
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """
        Compare two Guitar objects based on their manufacturing year.
        """
        return self.year < other.year
