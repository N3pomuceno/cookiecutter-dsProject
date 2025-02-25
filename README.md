Here’s your translated and improved README with proper formatting, corrections, and better flow for an international audience:  

---

# Cookiecutter - Data Science Project  

The purpose of this project is to establish the skeleton of a data science project, with pre-configured notebooks, organized data directories, and predefined dependencies. The project can also include a virtual environment to facilitate running notebooks without needing to install packages on the local system.  

## Setting Up the Virtual Environment for Cookiecutter  

Assuming the repository has been cloned and you are inside the Cookiecutter directory, using **Poetry (version 2.0)**, you can install the dependencies with the following command:  

### 1. **Creating and Installing a Virtual Environment (venv)**  

To create the virtual environment, run:  

```bash
poetry install
```  

### 2. **Running Cookiecutter**  

To run Cookiecutter, ensure you have the **Poetry plugin** for activating the virtual environment installed. If not, install it with:  

```bash
poetry self add poetry-plugin-shell
```  

Then, enter the virtual environment:  

```bash
poetry shell
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

poetry install

poetry shell

# Alternatively, you can work directly with poetry run
poetry run ...
```  

## Explanation of Variables  

When creating a project with Cookiecutter, you can define several variables that control the project’s configuration. Here are some important ones:  

- **`project_name`**: The project name, which will be used as the main directory name and can also configure the repository.  
- **`project_type`**: The type of project, which determines the libraries used for machine learning or whether it is just for exploratory data analysis (EDA).  
- **`use_jupyter`**: Defines whether the package associated with Jupyter will be installed—useful if you plan to work with notebooks.  
- **`description`**: A short description of the project, which will be inserted into the README.  
