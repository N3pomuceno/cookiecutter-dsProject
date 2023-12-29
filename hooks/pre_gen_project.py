# Funções dedicadas a verificações de nomes colocados para o projeto, antes de ser criado.
# Focado principalmente na verificação do nome do projeto. Se há espaços,
# E quantidade de caracteres limitados a 16.


def condicionais(nome_projeto):
    if len(nome_projeto) > 16:
        raise Exception('O nome do projeto deve ter menos de 16 caracteres')

    if " "  in nome_projeto:
        raise Exception('O nome do projeto não deve haver espaços em branco, substitua por underline')

def main():
    nome_projeto = "{{cookiecutter.project_name}}"
    condicionais(nome_projeto)
    


if __name__ == '__main__':
    main()