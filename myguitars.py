from guitar import Guitar
import csv

NUM_FIELDS = 3


def main():
    """
    Main function to run the guitar management program.
    """
    filename = "guitars.csv"

    # Load existing guitars from file
    guitars = load_guitars(filename)

    print("Guitars loaded from file:")
    display_guitars(guitars)

    # Sort guitars by year (oldest first)
    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    # Ask user to add new guitars
    new_guitars = add_new_guitars()
    if new_guitars:
        guitars.extend(new_guitars)
        print("\nFinal list of guitars:")
        display_guitars(guitars)
        # Write the updated list to the CSV file
        save_guitars(filename, guitars)
        print(f"\nUpdated guitars have been saved to {filename}.")
    else:
        print("No new guitars were added.")


def load_guitars(filename):
    """
    Read guitars from a CSV file and return a list of Guitar objects.
    """
    guitars = []
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != NUM_FIELDS:
                    continue  # Skip rows that don't have exactly 3 values
                name, year, cost = row
                try:
                    guitar = Guitar(name, int(year), float(cost))
                    guitars.append(guitar)
                except ValueError:
                    print(f"Invalid data for guitar: {row}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return guitars


def display_guitars(guitars):
    """
    Display all guitars in the provided list.
    """
    for guitar in guitars:
        print(guitar)


def save_guitars(filename, guitars):
    """
    Write all guitar objects to the CSV file.
    """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def add_new_guitars():
    """
    Prompt the user to enter new guitars and create Guitar objects accordingly.
    """
    new_guitars = []
    print("\nEnter new guitar details (leave name blank to finish):")

    # Read the first guitar name outside the loop.
    name = input("Name: ").strip()
    while name:
        year_input = input("Year: ").strip()
        cost_input = input("Cost: ").strip()
        try:
            new_guitars.append(Guitar(name, int(year_input), float(cost_input)))
        except ValueError:
            print("Invalid year or cost. Please try again.")
        # Ask for the next guitar name at the end of the loop.
        name = input("Name: ").strip()

    return new_guitars


if __name__ == '__main__':
    main()
