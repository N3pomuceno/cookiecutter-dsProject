# Cookiecutter - Data Science project

A ideia desse projeto é estabelecer o esqueleto de um projeto de data science. Onde ele já vem montado com o ambiente virtual para não precisar instalar pacotes na sua máquina e basta ambiente virtual para rodar sem nenhum problema.

Porém inicialmente, após clonar o repositório, é necessário fazer alguns passos:

### Execução do cookiecutter

1. Criar um ambiente virtual venv com o código:
```bash
python3 venv .venv
```
1. Entrar no ambiente virtual e instalar os requisitos para rodar o cookiecutter, o código a seguir é para fazer usado em linux, inclue o wsl do windows:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```
1. Preparado o ambiente virtual, podemos agora rodar o código do cookiecutter para criar o esqueleto do projeto. Ainda no ambiente, recue para um diretório pai, e daí faça o código para executar o cookiecutter:
```bash
cd ..
cookiecutter cookiecutter-dsProject
```

Executado o código do cookiecutter, com o projeto criado com sucesso, você poderá sair do ambiente virtual do cookiecutter e disso ir para o diretório do novo projeto criado e entrar no ambiente virtual do projeto para começar a fazer o projeto! Inicialmente é necessário criar instalar as dependências que estão faltando, porém futuramente um objetivo é fazer com que o próprio cookicutter crie o ambiente virtual pronto.

```bash
# sair do ambiente virtual
deactivate

# Entrar no ambiente virtual do projeto que foi criado, primeiro entra no 
# diretório do projeto e depois entra com o código
source .venv/bin/activate

# Instalar dependências faltantes do projeto
pip install -r requirements.txt

# Entrar no jupyter 
jupyter notebook #Ou o Lab se preferir.
```

---

### Explicação das variáveis

* project_name: Nome do projeto que será definido. Será ele é nome que aparecerá no nome do diretório do projeto além do tipo e também aparecerá no repositório
* project_type: Tipo do projeto, definindo que biblioteca será usado para o aprendizado de máquina, ou se realmente vai ser usado o aprendizado de máquina, e não será somente exploração de dados (EDA)
* description: Descrição que aparecerá no README do projeto.
* repository_name: Por padrão seria o nome do projeto e seu tipo, porém pode ser alterado, mas a ideia é que o nome do repositório seria criado de acordo com essa variável.
