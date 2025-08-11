import logging
import os
import shutil

# Path to the generated project root
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

logging.basicConfig(
    format="%(asctime)s [%(levelname)s]:%(lineno)d - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def remove_gitkeep_files():
    """
    Removes all .gitkeep files from the generated project.
    """
    logger.info("Removing .gitkeep files...")

    for root, dirs, files in os.walk(PROJECT_DIRECTORY):
        for file in files:
            if file == ".gitkeep":
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    logger.info(f"Removed {file_path}")
                except Exception as e:
                    logger.warning(f"Failed to remove {file_path}: {e}")


def create_gitignore():
    """
    Creates the .gitignore file from a template and removes the template file.
    """
    logger.info("Creating .gitignore file...")
    shutil.copy(".gitignore_project", ".gitignore")
    template_path = os.path.join(PROJECT_DIRECTORY, ".gitignore_project")
    if os.path.exists(template_path):
        os.remove(template_path)


def remove_extra_files(project_type, use_jupyter, database, tests, ingestion):
    """
    Removes unnecessary files based on project settings.

    :param project_type: Type of the project (e.g., "EDA").
    :param use_jupyter: Whether Jupyter notebooks are used ("Yes" or "No").
    :param database: The selected database option.
    """
    logger.info("Removing extra files...")

    # Remove ingestion files if not used
    if ingestion == "No":
        files = [
            "cmd/ingest_data.py",
            "cmd/ingest.sh",
            "notebooks/ingest_{{cookiecutter.project_name}}.ipynb",
            "cmd/ingest.py",
        ]
        for file in files:
            filepath = os.path.join(PROJECT_DIRECTORY, file)
            if os.path.exists(filepath):
                os.remove(filepath)
        logger.info(f"Removed {file} file.")

    # Remove Jupyter notebooks if not used
    if use_jupyter == "No":
        shutil.rmtree("./notebooks", ignore_errors=True)
        logger.info("Removed notebooks directory.")

    # Remove modeling files and directories if project is EDA
    if project_type == "EDA":
        files = ["Modelling_{{cookiecutter.project_name}}.ipynb"]
        if use_jupyter != "No":
            filepath = os.path.join(PROJECT_DIRECTORY, files[0])
            if os.path.exists(filepath):
                os.remove(filepath)
        shutil.rmtree("./models", ignore_errors=True)
        shutil.rmtree("./models_results", ignore_errors=True)
        shutil.rmtree("./cmd", ignore_errors=True)
        logger.info("ML directory and files related successfully removed!")

    # Remove database-related files if no database is selected
    if database == "None":
        files = ["docker-compose.yml", ".database_env", ".env"]
        for file in files:
            filepath = os.path.join(PROJECT_DIRECTORY, file)
            if os.path.exists(filepath):
                os.remove(filepath)
        shutil.rmtree("./sql", ignore_errors=True)
        logger.info("Sql directory successfully removed!")

    # Remove tests if not used
    if tests == "No":
        shutil.rmtree("./tests", ignore_errors=True)
        logger.info("Tests directory successfully removed!")


def main():
    """
    Main function to execute post-processing steps after project creation.
    """
    logger.info("Starting post-processing...")

    project_type = "{{cookiecutter.project_type}}"
    use_jupyter = "{{cookiecutter.use_jupyter}}"
    database = "{{cookiecutter.database}}"
    tests = "{{cookiecutter.use_tests}}"
    ingestion = "{{cookiecutter.use_data_ingestion}}"

    create_gitignore()
    remove_extra_files(project_type, use_jupyter, database, tests, ingestion)
    remove_gitkeep_files()

    logger.info("Post-processing completed!")
    logger.info(
        "Remember to create a virtual environment and install the project dependencies. 😉"
    )
    logger.info("And please, have a nice project! 😊")


if __name__ == "__main__":
    main()
