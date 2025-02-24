import shutil
import os
import subprocess


# Funções dedicadas a serem executadas após a criação do projeto com o Cookiecutter.
# O foco principal é:
# - Criar o arquivo .gitignore apropriado.
# - Remover arquivos extras conforme o tipo de projeto.
# - Criar o ambiente virtual (venv) e instalar as dependências.


def criar_gitignore():
    shutil.copy('.gitignore_project', '.gitignore')
    os.remove('.gitignore_project')


def remover_arquivos_extras(proj_tipo, use_jupyter, database):
    if (use_jupyter == "No"):
        os.remove('Modelling_{{cookiecutter.project_name}}.ipynb')
        os.remove('EDA_{{cookiecutter.project_name}}.ipynb')
    if (proj_tipo == "EDA"):
        if (use_jupyter != "No"):
            os.remove('Modelling_{{cookiecutter.project_name}}.ipynb')
        shutil.rmtree('./models')
        shutil.rmtree('./models_results')
    if (database == "No"):
        os.remove('docker-compose.yml')
        os.remove('.database.env')
        shutil.rmtree('./sql')


def main():
    proj_tipo = "{{cookiecutter.project_type}}"
    use_jupyter = "{{cookiecutter.use_jupyter}}"
    database = "{{cookiecutter.database}}"
    criar_gitignore()
    remover_arquivos_extras(proj_tipo, use_jupyter, database)


if __name__ == '__main__':
    main()