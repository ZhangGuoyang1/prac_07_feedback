"""

"""

import datetime
from project import Project


def main():
    """
    Main function that drives the project management application.
    Loads the default project data, then repeatedly displays a menu for user actions until the user quits.
    """
    print("Welcome to Pythonic Project Management")
    projects = load_projects("projects.txt")
    print(f"Loaded {len(projects)} projects from projects.txt")

    choice = ""
    while choice != 'q':
        display_menu()
        choice = input(">>> ").strip().lower()
        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? : ").strip().lower()
            if save_choice == 'y':
                save_projects("projects.txt", projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid menu option. Please try again.")


def load_projects(filename):
    """
    Loads projects from a tab-delimited file.
    """
    projects = []
    try:
        with open(filename, 'r') as f:
            header = f.readline()  # Skip header
            for line in f:
                if line.strip() == "":
                    continue  # Skip blank lines
                parts = line.strip().split('\t')
                name = parts[0]
                start_date = parts[1]
                priority = int(parts[2])
                cost_estimate = float(parts[3])
                completion = int(parts[4])
                project = Project(name, start_date, priority, cost_estimate, completion)
                projects.append(project)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return projects


def save_projects(filename, projects):
    """
    Saves projects to a tab-delimited file.
    The file starts with a header line, then one project per line.
    """
    with open(filename, 'w') as f:
        f.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            f.write(project.to_line() + "\n")
    print(f"Projects saved to {filename}")


def display_projects(projects):
    """
    Displays two groups of projects: incomplete (completion < 100%) and completed.
    """
    incomplete = [p for p in projects if p.completion_percentage < 100]
    completed = [p for p in projects if p.completion_percentage == 100]
    incomplete.sort()  # Relies on __lt__ in Project
    completed.sort()
    print("Incomplete projects:")
    for p in incomplete:
        print("  " + str(p))
    print("Completed projects:")
    for p in completed:
        print("  " + str(p))


def filter_projects_by_date(projects):
    """
    Asks the user for a date and displays only projects that start after that date,
    sorted by start date.
    """
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return
    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda p: p.start_date)
    for p in filtered:
        print(str(p))


def add_new_project(projects):
    """
    Prompts the user for project details and adds a new Project to the list.
    """
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    try:
        datetime.datetime.strptime(start_date, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Project not added.")
        return
    try:
        priority = int(input("Priority: "))
    except ValueError:
        print("Invalid priority. Project not added.")
        return
    try:
        cost_estimate = float(input("Cost estimate: ").replace('$',''))
    except ValueError:
        print("Invalid cost estimate. Project not added.")
        return
    try:
        completion = int(input("Percent complete: "))
    except ValueError:
        print("Invalid completion percentage. Project not added.")
        return
    project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(project)


def update_project(projects):
    """
    Displays a numbered list of projects, lets the user select one, and then updates
    the project's completion percentage and/or priority based on user input.
    """
    for i, project in enumerate(projects):
        print(f"{i} {str(project)}")
    try:
        index = int(input("Project choice: "))
        if index < 0 or index >= len(projects):
            print("Invalid project choice.")
            return
    except ValueError:
        print("Invalid input.")
        return
    project = projects[index]
    print(str(project))
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_completion.strip() != "":
        try:
            project.completion_percentage = int(new_completion)
        except ValueError:
            print("Invalid percentage input. Not updating completion percentage.")
    if new_priority.strip() != "":
        try:
            project.priority = int(new_priority)
        except ValueError:
            print("Invalid priority input. Not updating priority.")


def display_menu():
    """
    Displays the main menu options.
    """
    menu = (
        "- (L)oad projects  \n"
        "- (S)ave projects  \n"
        "- (D)isplay projects  \n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project  \n"
        "- (U)pdate project\n"
        "- (Q)uit"
    )
    print(menu)


if __name__ == '__main__':
    main()
