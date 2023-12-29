# Projeto de {{cookiecutter.project_name}}

De forma resumida: {{cookiecutter.description}}

Caso o cookiecutter não crie venv automaticamente, dado que você tenha escolhido essa opção, segue os códigos sugeridos que serão necessários para criar um ambiente virtual e iniciar o projeto, com a instalação as dependências corretamente:

```bash
# Cria venv:
python3 -m venv .venv

# Entra no ambiente virtual do projeto que foi criado
source .venv/bin/activate

# Instala dependências faltantes do projeto
pip install -r requirements.txt

# Entra no jupyter 
jupyter notebook #Ou o Lab se preferir/foi instalado.
```

---

Após isso, já é possível se dedicar ao projeto, adicionando os dados ou até ir direto para os notebooks, lembrando que a ideia é estar na venv para usar os notebooks, para não ter nenhum pacote instalado no computador em si.