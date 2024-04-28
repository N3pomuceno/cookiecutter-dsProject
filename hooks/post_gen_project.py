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


def remover_arquivos_extras(proj_tipo, usa_jupyter):
    if usa_jupyter == "No":
        os.remove(f'Modelling_{{{{cookiecutter.project_name}}}}.ipynb')
        os.remove(f'EDA_{{{{cookiecutter.project_name}}}}.ipynb')
    elif proj_tipo == "EDA":
        os.remove(f'Modelling_{{{{cookiecutter.project_name}}}}.ipynb')


def criar_venv():
    comando_bash = "python3 -m venv .venv"
    subprocess.run(comando_bash, shell=True, check=True)


def instalar_dependencias(caminho_venv, caminho_dependencias):
    comando_pip = f"source {caminho_venv}/bin/activate && pip install -r {caminho_dependencias}"
    subprocess.run(comando_pip, shell=True, executable="bash", check=True)


def criar_venv_completo():
    criar_venv()
    instalar_dependencias('.venv', 'requirements.txt')


def main():
    proj_tipo = "{{ cookiecutter.project_type }}"
    cria_venv = "{{ cookiecutter.create_venv }}"
    usa_jupyter = "{{ cookiecutter.use_jupyter }}"

    criar_gitignore() 
    remover_arquivos_extras(proj_tipo, usa_jupyter)
    
    if cria_venv == "Yes":
        criar_venv_completo()


if __name__ == '__main__':
    main()