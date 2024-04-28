# Funções para verificar a validade do nome do projeto antes de sua criação.
# Focado principalmente na verificação do nome do projeto em relação a espaços
# e ao limite de caracteres (máximo de 16).

def verificar_nome_projeto(nome_projeto):
    if len(nome_projeto) > 16:
        raise ValueError("O nome do projeto deve ter no máximo 16 caracteres.")

    if " " in nome_projeto:
        raise ValueError("O nome do projeto não deve conter espaços em branco. Substitua por underline.")

def main():
    nome_projeto = "{{ cookiecutter.project_name }}"
    
    verificar_nome_projeto(nome_projeto)

if __name__ == '__main__':
    main()