# 🍪 cookiecutter-dsProject — Production-Ready Template for Scalable Data Science

![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Template](https://img.shields.io/badge/type-cookiecutter-lightgrey)

This template provides a scaffold for data science projects with pre-configured notebooks, structured data directories, and predefined dependencies. It optionally includes a virtual environment to avoid installing packages globally.

The template is **development and production oriented**: you can prototype using Jupyter notebooks and later transition to production-ready scripts or pipelines.


## ✅ Key Features

- 📁 Predefined folder structure for `data`, `notebooks`, `src`, and `models`.
- 🐍 Supports isolated Python environments via [`uv`](https://github.com/astral-sh/uv) - uv is a fast Python dependency manager that replaces pip and virtualenv with better performance and deterministic environments.
- 📊 Ready for interactive development with **Jupyter Notebooks**.
- 🐳 Integrated with **Docker** and **docker-compose**:
  - Preconfigured `Dockerfile` and `docker-compose.yml`.
  - Environment variables already handled via `.database_env`.
- 🧱 Optional support for **dbt (data build tool)** to enable data transformation pipelines.
- 🔁 Built-in support for **automated data ingestion**, ideal for projects with frequent data updates.


## Setting Up the Virtual Environment for Cookiecutter  

Assuming the repository has been cloned and you are inside the Cookiecutter directory, using **uv**, dependency manager, you can install the dependencies with the following command:  

### 1. **Creating and Installing a Virtual Environment (venv)**  

To create the virtual environment, run:  

```bash
uv sync
```  

### 2. **Running Cookiecutter**  

To run Cookiecutter, ensure you have to activate the virtual environment.

```bash
# On Unix/macOS
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

With the virtual environment activated, you can now generate the project structure using Cookiecutter. First, go back to the parent directory and run the command:  

```bash
cd ..
cookiecutter cookiecutter-dsProject
```  

### 3. **Deactivating the Cookiecutter Virtual Environment**  

After successfully creating the new project, you can deactivate the Cookiecutter virtual environment:  

```bash
deactivate
```  

## Starting the New Project  

Now that the project has been created, navigate to the new project directory and, if a virtual environment was automatically set up, activate it to start working:  

```bash
cd new_project_name

uv sync

.venv/scripts/activate

# Alternatively, you can work directly with uv run
uv run ...
```  

## Explanation of Variables  

When creating a project with Cookiecutter, you can define several variables that control the project’s configuration. Here are some important ones:  

| Variable         | Description                                                                 |
| ---------------- | --------------------------------------------------------------------------- |
| `project_name`   | Name of your project (also becomes the root folder).                        |
| `project_author` | Your name or organization's name.                                           |
| `author_email`   | Your email.                                                                 |
| `project_type`   | Choose one: `EDA`, `ML_Scikit_Learn`, `ML_Pytorch`, `ML_TensorFlow`.        |
| `use_jupyter`    | `Yes` or `No`. Enables Jupyter support.                                     |
| `database`       | `PostgreSQL` or `None`. Adds DB and `.env` config.                          |
| `use_tests`      | `Yes` or `No`. Includes a basic tests/ folder and setup.                    |
| `use_ingestion`  | `Yes` or `No`. Includes scripts and structure for automated data ingestion. |
| `description`    | Short description of the project (included in README).                      |


---


I can't emphasize enough the impact of [Pedro Almeida](https://github.com/allmeidaapedro)'s work, which greatly influenced the structure of the `src/util` folder through his [project](https://github.com/allmeidaapedro/Churn-Prediction-Credit-Card). Additionally, the idea of documenting model results follows an established [standard](https://arxiv.org/pdf/1810.03993), which particularly caught my attention.  