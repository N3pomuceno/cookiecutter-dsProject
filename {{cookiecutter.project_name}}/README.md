# Projeto de {{cookiecutter.project_name}}

## Descrição

{{cookiecutter.description}}

Este projeto já apresenta uma estrutura organizada, com suporte para Jupyter Notebooks, um ambiente virtual para gerenciamento de dependências, e diretórios predefinidos para dados, notebooks e outros recursos.

## Configuração do Ambiente Virtual

As etapas a seguir mostram como criar o ambiente virtual, ativá-lo e instalar as dependências do projeto.

```bash
# Cria venv:
poetry install

# Caso não tenha o plugin do poetry basta fazer a seguinte linha de comando:
poetry self add poetry-plugin-shell

# Entra no ambiente virtual do projeto que foi criado
poetry shell

# Iniciar o Jupyter Notebook ou JupyterLab (se preferir)
jupyter notebook # ou jupyter lab

# Ou se caso queira fazer por fora
poetry run jupyter lab
```

## Estrutura do Projeto

A estrutura do projeto é organizada para facilitar o desenvolvimento de ciência de dados. Aqui está uma visão geral dos diretórios:

- **data/**: Diretório para armazenar dados brutos e processados.

- **notebooks/**: Local para Jupyter Notebooks.

- **src/**: Código fonte para o projeto.

- **outputs/**: Saídas do projeto, como gráficos ou relatórios.

## Dicas para Trabalhar no Projeto

- Sempre ative o ambiente virtual antes de trabalhar no projeto para garantir que está usando as dependências corretas.

- Mantenha o arquivo requirements.txt atualizado para refletir as dependências necessárias.

- Use git para controle de versão e faça commits regulares para rastrear o progresso.