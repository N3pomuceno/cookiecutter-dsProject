# Project {{cookiecutter.project_name}}

## Description

{{cookiecutter.description}}

To get a more complete description of the project, you can find in the `docs/documentation.md`.

## Setting Up the Virtual Environment

Follow these steps to create the virtual environment, activate it, and install the project dependencies:

```bash
# Create the virtual environment:
uv sync


# Enter the project's virtual environment:
.venv/scripts/activate

# Start Jupyter Notebook or JupyterLab (if preferred):
jupyter notebook # or jupyter lab
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
```
{{cookiecutter.project_name}}/
├── README.md                   # Project overview and usage instructions
├── .env                        # General environment variables
├── .gitignore_project          # Git ignore rules
{% if cookiecutter.database != "None" -%}
├── .database_env               # Database-specific environment variables
├── docker-compose.yml          # Configuration for containerized services
{% endif -%}
├── pyproject.toml              # Dependency management and project metadata

├── cfg/
│   └── cfg.json                # Main project configuration file

├── data/
│   ├── raw/                    # Raw, unprocessed data
│   ├── processed/              # Cleaned and transformed datasets
│   └── summary.json            # Data summary and statistics

├── docs/
│   ├── documentation.md        # Project goals and detailed instructions
│   └── todo.md                 # Task tracking and roadmap

├── logs/                       # Logs generated during execution

├── models/                     # Trained machine learning models
├── models_results/             # Model evaluation metrics and reports
{% if cookiecutter.use_jupyter == "Yes" -%}
├── notebooks/
│   ├── EDA_{{cookiecutter.project_name}}.ipynb         # Exploratory Data Analysis
│   ├── Modelling_{{cookiecutter.project_name}}.ipynb   # Model training and evaluation
│   └── ingest_{{cookiecutter.project_name}}.ipynb      # Data ingestion and preprocessing
{% endif -%}
├── sql/
│   ├── queries/                # SQL queries for data extraction and analysis
│   └── schemas/                # Database schema definitions
{% if cookiecutter.project_type == "EDA" -%}
├── cmd/
│   ├── __init__.py
│   ├── exec-functions.sh      # Shell functions for modular execution
│   ├── exec_all.sh            # Full pipeline execution script
│   ├── ingest.sh              # Data ingestion execution (shell)
│   ├── ingest_data.py         # Python-based data ingestion
│   ├── predict.sh             # Prediction execution (shell)
│   ├── predict_new_data.py    # Predicting outcomes on new data
│   └── train.py               # Model training logic
{% endif -%}
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── db.py              # Database interaction helpers
│   │   ├── ingest.py          # Data ingestion functions
│   │   └── io.py              # Input/output utilities
│   ├── features/
│   │   └── build_features.py  # Feature engineering logic
│   └── util/
│       ├── eda.py             # Exploratory Data Analysis utilities
│       ├── exception.py       # Custom exception classes
│       └── logger.py          # Logging configuration
{% if cookiecutter.use_tests == "Yes" -%}
└── tests/                      # Unit and integration tests
{% endif -%}
```


## Documentation and Planning

To ensure proper alignment between team members and maintain clarity throughout the development process, this repository includes two key markdown files within the `docs/` folder:

* **documentation.md**: Contains the overall goals, project scope, modeling strategy, and development guidelines. It serves as the reference document for decisions, assumptions, and rationale behind the project's structure.
* **todo.md**: Tracks completed, ongoing, and upcoming tasks.
* **/models_results**: The idea of documenting model results follows an established [standard](https://arxiv.org/pdf/1810.03993).  

### Transition from Notebook to Pipeline

After thoroughly developing and validating your modeling approach using the Jupyter notebook (Modelling_{{cookiecutter.project_name}}.ipynb), you are encouraged to:

 * Modularize the logic by migrating key components into Python scripts:

    * Preprocessing → feature_eng.py

    * Training → train.py

    * Evaluation/Prediction → predict.py

* Automate execution using the shell script exec.sh, enabling a more reproducible and production-ready pipeline.

This structure supports a clear path from experimentation to deployment, facilitating collaboration and future scaling in real environments.

## Best Practices

- Always activate the virtual environment before working on the project to ensure correct dependencies.
- Keep `pyproject.toml` or `requirements.txt` updated with necessary dependencies.
- Use Git for version control and commit regularly to track progress.


## About the Configuration File

This project includes a `cfg/cfg.json` file that centralizes important configuration values such as file paths, model hyperparameters, and general settings. This approach:

* Avoids hardcoding values across the codebase
* Facilitates experimentation by allowing easy switching of parameters
* Enhances code clarity, reusability, and maintainability

The `cfg.json` is loaded within the `util/io.py` file, keeping configuration management streamlined and accessible throughout the project.