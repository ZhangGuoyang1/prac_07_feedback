"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

from programming_language import ProgrammingLanguage

MIN_FIELDS = 3


def read_languages(file_path: str):
    """
    Read programming language data from a CSV file and return a list of ProgrammingLanguage instances.
    """
    languages = []
    try:
        with open(file_path, "r") as file:
            header = file.readline()  # Skip header line
            for line in file:
                # Each line is expected to be in the format:
                parts = line.strip().split(",")
                if len(parts) < MIN_FIELDS:
                    continue
                name = parts[0].strip()
                reflection = parts[1].strip().lower() == 'true'
                pointer_arithmetic = parts[2].strip().lower() == 'true'
                language = ProgrammingLanguage(name, reflection, pointer_arithmetic)
                languages.append(language)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return languages


if __name__ == "__main__":
    file_path = "languages.csv"
    langs = read_languages(file_path)
    for lang in langs:
        print(lang)
