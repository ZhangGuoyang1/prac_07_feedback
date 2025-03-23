from datetime import datetime


class Project:
    """
    Represents a project with details such as name, start date, priority,
    cost estimate, and completion percentage.
    """
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """
        Initializes a new Project instance.
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """
        Returns a nicely formatted string representation of the project.
        """
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """
        Compares two projects based on priority.
        """
        return self.priority < other.priority

    def to_line(self):
        """
        Converts the project to a tab-delimited string format suitable for file storage.
        """
        return (f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}"
                f"\t{self.completion_percentage}")


