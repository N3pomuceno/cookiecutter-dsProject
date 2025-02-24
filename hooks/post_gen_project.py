import shutil
import os
import logging

# Caminho da raiz do projeto gerado
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Funções dedicadas a serem executadas após a criação do projeto com o Cookiecutter.
# O foco principal é:
# - Criar o arquivo .gitignore apropriado.
# - Remover arquivos extras conforme o tipo de projeto.
# - Criar o ambiente virtual (venv) e instalar as dependências.


def criar_gitignore():
    logger.info('Criando arquivo .gitignore...')
    shutil.copy('.gitignore_project', '.gitignore')
    path = os.path.join(PROJECT_DIRECTORY, '.gitignore_project')
    if os.path.exists(path):
        os.remove('.gitignore_project')


def remover_arquivos_extras(proj_tipo, use_jupyter, database):
    logger.info('Removendo arquivos extras...')
    if (use_jupyter == "No"):
        files = ['Modelling_{{cookiecutter.project_name}}.ipynb', 'EDA_{{cookiecutter.project_name}}.ipynb']
        for file in files:
            filepath = os.path.join(PROJECT_DIRECTORY, file)
            if os.path.exists(filepath):
                os.remove(filepath)
    if (proj_tipo == "EDA"):
        files = ['Modelling_{{cookiecutter.project_name}}.ipynb']
        if (use_jupyter != "No"):
            filepath = os.path.join(PROJECT_DIRECTORY, file)
            if os.path.exists(filepath):
                os.remove(filepath)
        shutil.rmtree('./models')
        shutil.rmtree('./models_results')
    if (database == "None"):
        files = ['docker-compose.yml', '.database_env']
        for file in files:
            filepath = os.path.join(PROJECT_DIRECTORY, file)
            if os.path.exists(filepath):
                os.remove(filepath)
        shutil.rmtree('./sql')
    logger.info('Arquivos extras removidos com sucesso!')


def main():
    logger.info('Iniciando pós-processamento em {}...'.format(PROJECT_DIRECTORY))
    proj_tipo = "{{cookiecutter.project_type}}"
    use_jupyter = "{{cookiecutter.use_jupyter}}"
    database = "{{cookiecutter.database}}"
    criar_gitignore()
    remover_arquivos_extras(proj_tipo, use_jupyter, database)
    logger.info('Pós-processamento concluído!')
    logger.info('Lembre-se de criar o ambiente virtual e instalar as dependências do projeto. 😉')


if __name__ == '__main__':
    main()