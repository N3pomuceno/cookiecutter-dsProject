import shutil

def criacao_git_ignore():
    shutil.copy('{{cookiecutter.project_name}}_{{cookiecutter.project_type}}/.gitignore_project','{{cookiecutter.project_name}}_{{cookiecutter.project_type}}/.gitignore')


def main():
    criacao_git_ignore()



if __name__ == '__main__':
    main()