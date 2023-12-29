# Projeto de {{cookiecutter.project_name}}

De forma resumida: {{cookiecutter.description}}

Enquanto o cookiecutter não cria venv automaticamente, segue os códigos que serão necessários para quando iniciar o projeto, instalar as dependências corretamente:

```
# Entrar no ambiente virtual do projeto que foi criado, primeiro entra no 
# diretório do projeto e depois entra com o código
source .venv/bin/activate

# Instalar dependências faltantes do projeto
pip install -r requirements.txt

# Entrar no jupyter 
jupyter notebook #Ou o Lab se preferir.
```

---

Após isso, já é possível dedicar se ao projeto, adicionando os dados ou até ir direto para os notebooks, deixando claro que é necessário estar na venv para usar os notebooks.