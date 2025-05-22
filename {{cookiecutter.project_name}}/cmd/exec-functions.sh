#!/bin/bash

######################################################################
##
## exec-functions.sh
##
## DEFINES FUNCTIONS
##
## - initialize
## - activate_venv
## - log_message
## - finalize
##
######################################################################

### Writes the header and sets up logs
### Parameters: description
###
initialize () {

    if (( $# < 1 )); then
        log_message "Insufficient parameters ($#) in function call [initialize]"
        exit 10
    fi

    description="$1"

    # Path where logs will be saved
    LOGS="./logs"
    mkdir -p "$LOGS"  # Ensure the folder exists

    # System base name (adjust if necessary)
    system_base_name="exec"

    # Environment: can be 'DEV', 'HML' or 'PRD'
    ENV="${ENV:-DEV}"  # Default to DEV if not set

    # Builds the log file name
    log_file="${LOGS}/${system_base_name,,}-$(date +"%Y-%m-%d_%H-%M-%S").log"

    # Redirect all stdout and stderr to the log (and also show in terminal)
    exec > >(tee -a "$log_file") 2>&1

    # Example messages
    echo "==============================="
    echo "    Starting execution script..."
    echo "    Description: $description"
    echo "    Environment: Local"
    echo "    Log file: $log_file"
    echo "==============================="
}

### Activates the Python venv, creating if necessary
### Parameters: none
###
activate_venv () {

    # Check if running on Windows or Linux/Mac
    if [ "${OS:-x}" == "Windows_NT" ]; then
        activate_path='Scripts/activate'
    else
        activate_path='bin/activate'
    fi

    # VENV directory
    venv_dir="$(pwd)/cmd/.venv"
    log_message "Venv directory: ${venv_dir}"

    # Check if the .venv folder exists
    if [ ! -d "${venv_dir}" ]; then
        log_message "Error: VENV not found at ${venv_dir}"
        exit 20
    else
        log_message "VENV found. Activating..."
        source "${venv_dir}"/${activate_path}
    fi
}

### Logging function
### Parameters: message
###
log_message() {
    echo "$(date "+%Y-%m-%d %H:%M:%S") INFO [$(basename $0)] $*"
}

### Finalizes and prints execution time
### Parameters: none
###
finalize() {
    hours=$((SECONDS / 3600))
    minutes=$(( (SECONDS-hours*3600) / 60))
    seconds=$((SECONDS % 60))
    log_message "$(printf "Execution time: %02d:%02d:%02d" ${hours} ${minutes} ${seconds})"
}
