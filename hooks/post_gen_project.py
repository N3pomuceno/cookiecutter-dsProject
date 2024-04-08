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

def remover_arquivos_extras(proj_tipo, use_jupyter):
    if (use_jupyter == "No"):
        os.remove('Modelling_{{cookiecutter.project_name}}.ipynb')
        os.remove('EDA_{{cookiecutter.project_name}}.ipynb')
    elif (proj_tipo == "EDA"):
        os.remove('Modelling_{{cookiecutter.project_name}}.ipynb')



def cria_venv():
    comando_bash = "poetry install"
    subprocess.run(comando_bash, shell=True)



def main():
    proj_tipo = "{{cookiecutter.project_type}}"
    preinstallvenv = "{{cookiecutter.create_venv}}"
    use_jupyter = "{{cookiecutter.use_jupyter}}"
    criacao_git_ignore()
    remocao_arquivo_extra(proj_tipo, use_jupyter)
    if preinstallvenv == "Yes":
        cria_venv()


if __name__ == '__main__':
    main()