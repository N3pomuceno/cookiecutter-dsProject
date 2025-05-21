#!/bin/bash

# descomente para depurar, mostrará no output a execução de cada linha deste script
# set -x

# configuração para o script falhar em caso de erros ou variaves indefinidas
set -eu -o pipefail

source "$(dirname $0)/exec-functions.sh"

inicializa "Processo de Ingestão de Dados"

# Ativa o ambiente virtual
ativa_venv

# Comando para executar o programa Python
echo "Iniciando execução do script Python para a ingestão de dados..."
python3 -m cmd.ingest_data

# Mensagem final
finaliza

exit 0
