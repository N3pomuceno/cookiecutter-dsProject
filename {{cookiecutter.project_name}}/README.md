# Project {{cookiecutter.project_name}}

## Description

{{cookiecutter.description}}

## Setting Up the Virtual Environment

Follow these steps to create the virtual environment, activate it, and install the project dependencies:

```bash
# Create the virtual environment:
poetry install

# If you don't have the poetry plugin installed, run:
poetry self add poetry-plugin-shell

# Enter the project's virtual environment:
poetry shell

# Start Jupyter Notebook or JupyterLab (if preferred):
jupyter notebook # or jupyter lab

# Alternatively, run it directly with poetry:
poetry run jupyter lab
```

{% if cookiecutter.database == "PostgreSQL" -%}

## Using the Database

To use the database, Docker Desktop must be installed and running. Once set up, start the database with:

```bash
docker-compose up -d
```

After this, the database will be running and accessible through tools like DBeaver or TablePlus using the credentials stored in `.database_env`.

To stop the database, run:

```bash
docker-compose down
```

Additionally, the project includes the Data Build Tool ([DBT](https://docs.getdbt.com/docs/introduction)), which facilitates data transformation, validation, and efficiency monitoring in the database.

{% endif -%}

## Initializing Git Repository

By default, Git is not initialized. If you want to link the project to a repository, follow these steps:

```bash
# Initialize the repository
git init

# Add a remote repository
git remote add origin <your_repo_https_or_ssh_link>

# Push the main branch to the remote repository
git push origin main
```

## Project Structure

The project is structured to streamline data science workflows. Below is an overview of the main directories:

- **data/**: Stores raw and processed datasets.
- **notebooks/**: Contains Jupyter Notebooks.
- **src/**: Source code for the project.
- **outputs/**: Stores project outputs, such as charts and reports.
- **models/** and **models_results/**: Model training files and results. It's recommended to document model explanations using this [standard](https://arxiv.org/pdf/1810.03993).

## Documentation and Planning

For better alignment among team members, a repository will include two markdown files:

- `documentation.md`: Defines project goals and guidelines.
- `todo.md`: Tracks completed, ongoing, and upcoming tasks.

## Best Practices

- Always activate the virtual environment before working on the project to ensure correct dependencies.
- Keep `pyproject.toml` or `requirements.txt` updated with necessary dependencies.
- Use Git for version control and commit regularly to track progress.

