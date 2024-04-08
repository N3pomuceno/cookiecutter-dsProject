# Importação das bibliotecas 
import shutil
import os
import subprocess

# Funções dedicadas após a execução do cookiecutter, ou seja, criado o projeto, 
# Agora esse arquivo será executado, como o foco principal em:
# Criação do arquivo .gitignore correto.
# Remoção dos arquivos extras de acordo com o tipo do projeto
# Criação do ambiente virtual, venv.

def criacao_git_ignore():
    shutil.copy('.gitignore_project','.gitignore')
    os.remove('.gitignore_project')


def remocao_arquivo_extra(proj_tipo, use_jupyter):
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