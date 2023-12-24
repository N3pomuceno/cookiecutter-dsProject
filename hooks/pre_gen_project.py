import subprocess


def condicionais(nome_projeto):
    if len(nome_projeto) > 16:
        raise Exception('O nome do projeto deve ter menos de 16 caracteres')

    if " "  in nome_projeto:
        raise Exception('O nome do projeto não deve haver espaços em branco, coloque underline')


def main():
    nome_projeto = "{{cookiecutter.project_name}}"
    nome_dir = "{{cookiecutter.project_name}}_{{cookiecutter.project_type}}"

    condicionais(nome_projeto)



if __name__ == '__main__':
    main()