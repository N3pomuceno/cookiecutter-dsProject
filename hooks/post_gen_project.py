import shutil
import os
import logging

# Path to the generated project root
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_gitignore():
    """
    Creates the .gitignore file from a template and removes the template file.
    """
    logger.info('Creating .gitignore file...')
    shutil.copy('.gitignore_project', '.gitignore')
    template_path = os.path.join(PROJECT_DIRECTORY, '.gitignore_project')
    if os.path.exists(template_path):
        os.remove(template_path)


def remove_extra_files(project_type, use_jupyter, database):
    """
    Removes unnecessary files based on project settings.

    :param project_type: Type of the project (e.g., "EDA").
    :param use_jupyter: Whether Jupyter notebooks are used ("Yes" or "No").
    :param database: The selected database option.
    """
    logger.info('Removing extra files...')

    # Remove Jupyter notebooks if not used
    if use_jupyter == "No":
        files = ['Modelling_{{cookiecutter.project_name}}.ipynb', 'EDA_{{cookiecutter.project_name}}.ipynb']
        for file in files:
            filepath = os.path.join(PROJECT_DIRECTORY, file)
            if os.path.exists(filepath):
                os.remove(filepath)

    # Remove modeling files and directories if project is EDA
    if project_type == "EDA":
        files = ['Modelling_{{cookiecutter.project_name}}.ipynb']
        if use_jupyter != "No":
            filepath = os.path.join(PROJECT_DIRECTORY, files[0])
            if os.path.exists(filepath):
                os.remove(filepath)
        shutil.rmtree('./models', ignore_errors=True)
        shutil.rmtree('./models_results', ignore_errors=True)

    # Remove database-related files if no database is selected
    if database == "None":
        files = ['docker-compose.yml', '.database_env']
        for file in files:
            filepath = os.path.join(PROJECT_DIRECTORY, file)
            if os.path.exists(filepath):
                os.remove(filepath)
        shutil.rmtree('./sql', ignore_errors=True)
    
    logger.info('Extra files successfully removed!')


def main():
    """
    Main function to execute post-processing steps after project creation.
    """
    logger.info('Starting post-processing...')

    project_type = "{{cookiecutter.project_type}}"
    use_jupyter = "{{cookiecutter.use_jupyter}}"
    database = "{{cookiecutter.database}}"

    create_gitignore()
    remove_extra_files(project_type, use_jupyter, database)

    logger.info('Post-processing completed!')
    logger.info('Remember to create a virtual environment and install the project dependencies. 😉')


if __name__ == '__main__':
    main()
