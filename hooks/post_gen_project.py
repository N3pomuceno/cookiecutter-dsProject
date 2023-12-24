import shutil
import os

def criacao_git_ignore():
    shutil.copy('.gitignore_project','.gitignore')
    os.remove('.gitignore_project')

def remocao_arquivo_extra(proj_tipo):
    if proj_tipo == "EDA":
        os.remove('Modelling_{{cookiecutter.project_name}}.ipynb')


def main():
    proj_tipo = "{{cookiecutter.project_type}}"
    criacao_git_ignore()
    remocao_arquivo_extra(proj_tipo)


if __name__ == '__main__':
    main()