import shutil
import os
import subprocess


def criacao_git_ignore():
    shutil.copy('.gitignore_project','.gitignore')
    os.remove('.gitignore_project')

def remocao_arquivo_extra(proj_tipo):
    if proj_tipo == "EDA":
        os.remove('Modelling_{{cookiecutter.project_name}}.ipynb')

def cria_venv_completa():
    caminho_venv = '.venv'
    caminho_dependencias = 'requirements.txt'
    cria_venv()
    instala_dependencias(caminho_venv, caminho_dependencias)


def cria_venv():
    comando_bash = "python3 -m venv .venv"
    subprocess.run(comando_bash, shell=True)
    comando_bash = "pwd"
    subprocess.run(comando_bash, shell=True)

def instala_dependencias(caminho_venv, caminho_dependencias):
    comando_pip = "source {}/bin/activate && pip install -r {}".format(caminho_venv, caminho_dependencias)
    subprocess.run(comando_pip, shell=True, executable="bash")


def main():
    proj_tipo = "{{cookiecutter.project_type}}"
    preinstallvenv = "{{cookiecutter.create_venv}}"
    criacao_git_ignore()
    remocao_arquivo_extra(proj_tipo)
    if preinstallvenv == "Yes":
        cria_venv_completa()

if __name__ == '__main__':
    main()