# Cookiecutter - Projeto de Data Science

O propósito deste projeto é estabelecer o esqueleto de um projeto de ciência de dados, com notebooks pré-configurados, diretórios de dados organizados e requisitos já definidos. O projeto também pode incluir um ambiente virtual para facilitar a execução dos notebooks sem a necessidade de instalar pacotes no sistema local.

No entanto, inicialmente, após clonar o repositório do Cookiecutter, é necessário executar alguns passos para configurar o ambiente virtual (venv). Isso é feito para evitar instalar pacotes diretamente no computador e manter a separação do ambiente do projeto.

## Configurando o Ambiente Virtual para o Cookiecutter

Supondo que o repositório foi clonado e você está no diretório do Cookiecutter, siga estas etapas:

1. **Criar um ambiente virtual venv (venv)**

   Para criar o ambiente virtual, execute o seguinte comando:

   ```bash
   python3 -m venv .venv
   ```

2. **Ativar o ambiente virtual e instalar os requisitos** ! Versão Antiga

   Depois de criar o ambiente virtual, ative-o e instale os requisitos necessários para rodar o Cookiecutter. O comando abaixo funciona em sistemas Linux e no Windows com WSL:

   ```bash
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Executar o Cookiecutter**

   Com o ambiente virtual ativado, agora você pode criar a estrutura do projeto usando o Cookiecutter. Primeiro, volte para o diretório pai e, em seguida, execute o comando para criar o novo projeto:

   ```bash
   cd ..
   cookiecutter cookiecutter-dsProject
   ```

4. **Desativar o ambiente virtual do Cookiecutter**

   Depois de criar o novo projeto com sucesso, você pode desativar o ambiente virtual do Cookiecutter:

   ```bash
   deactivate
   ```

## Iniciar o Novo Projeto

Agora que o projeto foi criado, entre no diretório do novo projeto e, se um ambiente virtual foi criado automaticamente, ative-o para começar a trabalhar:

   ```bash
   cd nome_do_novo_projeto
   source .venv/bin/activate
   ```   

## Explicação das variáveis

Ao criar um projeto com o Cookiecutter, você pode definir várias variáveis que controlam a configuração do projeto. Aqui está uma explicação de algumas das variáveis importantes:

- **project_name**: O nome do projeto que aparecerá como o nome do diretório principal. Também pode ser usado para configurar o repositório.

- **project_type**: O tipo de projeto, que pode determinar as bibliotecas a serem usadas para aprendizado de máquina ou se é apenas para exploração de dados (EDA).

- **use_jupyter**: Define se o pacote associado ao Jupyter será instalado, útil se você pretende usar notebooks no projeto.

- **description**: Uma breve descrição do projeto, que será inserida no README.

