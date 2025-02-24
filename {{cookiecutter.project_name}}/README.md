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

{% if cookiecutter.database == "PostgreSQL" -%}

## Como utilizar o banco de dados

Para usa utilização é necessário ter o docker desktop instalado, e uma vez instalado e rodando, basta fazer a seguinte linha de comando para subir o banco:

```bash
docker-compose up -d
```

Após isso, o banco estará em pé, e é possível acessar por algum programa como dbeaver ou tablePlus, com as seguintes informações que estão no `.database_env`.

Quando quiser parar de usar o banco, basta fazer um:

```bash
docker-compose down
```

Além disso, também é adicionado uma ferramenta chamada Data Build Tool ([DBT](https://docs.getdbt.com/docs/introduction)), que pode ser usada para facilitar o processo de transformação de dados do banco, podendo criar visualizações, novas tabelas, fazendo testes mantendo a integridade dos dados, vendo também questão de eficiência.


{% endif -%}

## Estrutura do Projeto

A estrutura do projeto é organizada para facilitar o desenvolvimento de ciência de dados. Aqui está uma visão geral dos diretórios:

- **data/**: Diretório para armazenar dados brutos e processados.

- **notebooks/**: Local para Jupyter Notebooks.

- **src/**: Código fonte para o projeto.

- **outputs/**: Saídas do projeto, como gráficos ou relatórios.

- **models/ e models_results/**: Modelagem e seus resultados, boa prática deixar bem definido, com boas explicações, se possível seguindo o seguinte [padrão](https://arxiv.org/pdf/1810.03993) para explicações.

## Dicas para Trabalhar no Projeto

- Sempre ative o ambiente virtual antes de trabalhar no projeto para garantir que está usando as dependências corretas (ou pelo menos tenha sempre em mente que é uma boa prática manter os pacotes isolados).

- Mantenha o arquivo pyproject.toml/requirements.txt atualizado para refletir as dependências necessárias.

- Use git para controle de versão e faça commits regulares para rastrear o progresso.