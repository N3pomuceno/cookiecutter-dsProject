#!/bin/bash

# descomente para depurar, mostrará no output a execução de cada linha deste script
# set -x

# configuração para o script falhar em caso de erros ou variaves indefinidas
set -eu -o pipefail

source "$(dirname $0)/exec-functions.sh"

inicializa "Processo de Treinamento e Previsão do Modelo"

# Ativa o ambiente virtual
ativa_venv

{% if cookiecutter.use_data_ingestion == "Yes" -%}
# Comando para executar programa Python para ingestão de dados
echo "Iniciando execução do script Python para a ingestão de dados..."
python3 -m cmd.ingest_data
{% endif -%}


# Comando para executar o programa Python
echo "Iniciando execução do script Python para o treinamento do modelo..."
python3 -m cmd.train

echo "Iniciando execução do script Python para a previsão do modelo..."
python3 -m cmd.predict_new_data

# Mensagem final
finaliza

exit 0
