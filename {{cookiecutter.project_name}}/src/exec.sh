#!/bin/bash

# descomente para depurar, mostrará no output a execução de cada linha deste script
# set -x

# configuração para o script falhar em caso de erros ou variaves indefinidas
set -eu -o pipefail

# Caminho da pasta onde os logs serão salvos
LOGS="./logs"
mkdir -p "$LOGS"  # Garante que a pasta existe

# Nome base do sistema (ajuste conforme necessário)
sistema_sem_prefixo="exec"

# Ambiente: pode ser 'DEV', 'HML' ou 'PRD'
ENV="${ENV:-DEV}"  # Usa DEV por padrão, se não estiver definido

# Monta o nome do arquivo de log
log_file="${LOGS}/${sistema_sem_prefixo,,}-$(date +"%Y-%m-%d_%H-%M-%S").log"

# Redireciona todas as saídas padrão e de erro para o log (e também exibe no terminal)
exec > >(tee -a "$log_file") 2>&1

# Mensagens de exemplo
echo "==============================="
echo " Iniciando script de logging..."
echo " Ambiente: Local"
echo " Log file: $log_file"
echo "==============================="

# Comando para executar o programa Python
echo "Iniciando execução do script Python para o treinamento do modelo..."
python3 /src/train.py

echo "Iniciando execução do script Python para a previsão do modelo..."
python3 /src/predict.py

# Mensagem final
echo "==============================="
echo " Script finalizado."
echo "==============================="

exit 0
