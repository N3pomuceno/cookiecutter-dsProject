# Functions to validate the project name before its creation.
# Focused mainly on checking for spaces and character limit (maximum of 16).

def validate_project_name(project_name):
    """
    Validates the project name by checking length and spaces.

    :param project_name: Name of the project to be validated.
    :raises ValueError: If the project name is too long or contains spaces.
    """
    if len(project_name) > 16:
        raise ValueError("The project name must have a maximum of 16 characters.")

    if " " in project_name:
        raise ValueError("The project name must not contain spaces. Use underscores instead.")


def main():
    """
    Main function to check the project name validity.
    """
    project_name = "{{ cookiecutter.project_name }}"
    validate_project_name(project_name)


if __name__ == '__main__':
    main()
