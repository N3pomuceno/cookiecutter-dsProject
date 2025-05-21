#!/bin/bash

######################################################################
##
## exec-funcoes.sh
##
## DEFINE FUNCOES
##
## - inicializa
## - ativa_venv
## - log
## - finaliza
##
######################################################################

### Escreve o cabeçalho e define logs
### Parametros: descricao
###
inicializa () {

    if (( $# < 1 )); then
    log "Parametros insuficientes ($#) na chamada da função [inicializa]"
    exit 10
    fi

    descricao="$1"
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
    echo "    Iniciando script de execução..."
    echo "    Descrição: $descricao"
    echo "    Ambiente: Local"
    echo "    Log file: $log_file"
    echo "==============================="
}

### Ativa o venv python, criando se necessário
### Parametros:
###
ativa_venv () {

    # Testa se está no windows ou linux
    if [ "${OS:-x}" == "Windows_NT" ]; then
        activate_path='Scripts/activate'
    else
        activate_path='bin/activate'
    fi

    # Diretório da VENV
    venv_dir="$(pwd)/cmd/.venv"
    log "Diretório venv: ${venv_dir}"

    # Verifica se a pasta .venv existe
    if [ ! -d "${venv_dir}" ]; then
        log "Erro: VENV não encontrada no caminho ${venv_dir}"
        exit 20
    else
        log "VENV encontrada. Ativando..."
        source "${venv_dir}"/${activate_path}
    fi
}

### log
### Parametros: mensagem-cfg
###
log() {
    echo "$(date "+%Y-%m-%d %H:%M:%S") INFO [$(basename $0)] $*"
}


### finaliza
### Parametros: n/a
###
finaliza() {
    horas=$((SECONDS / 3600))
    minutos=$(( (SECONDS-horas*3600) / 60))
    segundos=$((SECONDS % 60))
    log  "$(printf "Tempo de execução: %02d:%02d:%02d" ${horas} ${minutos} ${segundos})"
}