# Cookiecutter - Data Science project

O propósito desse projeto é estabelecer o esqueleto de um projeto de data science. Com os notebooks já criados, os diretórios dos dados já organizados e os requirements já definidos. Onde ele já pode vir com o ambiente virtual montado para não precisar instalar pacotes na sua máquina e basta o mesmo para rodar os notebooks.

Porém inicialmente, após clonar o repositório do cookiecutter, é necessário fazer alguns passos, esses passos são dedicados a criação da venv do cookicutter, para não instalar pacotes no computador, usaremos de uma venv para fazer todo o processo. 

### Execução do cookiecutter

Supondo que o repositório tenha sido clonado e já está no diretório do cookiecutter:
1. Criar um ambiente virtual venv com o código:
```bash
python3 -m venv .venv
```
1. Entrar no ambiente virtual e instalar os requisitos para rodar o cookiecutter, o código a seguir é para fazer usado em linux, inclue o wsl do windows:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```
1. Preparado o ambiente virtual, podemos agora rodar o código do cookiecutter para criar o esqueleto do projeto. Ainda no ambiente virtual do cookiecutter, recue para um diretório pai, e daí faça o código para executar o cookiecutter:
```bash
cd ..
cookiecutter cookiecutter-dsProject
```

Executado o código do cookiecutter, com o projeto criado com sucesso, você poderá sair do ambiente virtual do cookiecutter e disso ir para o diretório do novo projeto criado e entrar no ambiente virtual do projeto (caso tenha sido criado automaticamente) para começar a fazer o projeto! 

```bash
# sair do ambiente virtual
deactivate
```


### Explicação das variáveis

* project_name: Nome do projeto que será definido. Será ele é nome que aparecerá no nome do diretório do projeto além do tipo e também aparecerá no repositório
* project_type: Tipo do projeto, definindo que biblioteca será usado para o aprendizado de máquina, ou se realmente vai ser usado o aprendizado de máquina, e não será somente exploração de dados (EDA)
* use_jupyter: Usado para definir se será instalado o pacote associado ao jupyter. Caso queira só usar arquivos python ou algo do tipo para não criar os notebooks em vão.
* create_venv: Criação do ambiente virtual será definido por essa variável. Caso rejeite, não será criado.
* description: Descrição que aparecerá no README do projeto.
* repository_name: Por padrão seria o nome do projeto e seu tipo, porém pode ser alterado, mas a ideia é que o nome do repositório seria criado de acordo com essa variável.
