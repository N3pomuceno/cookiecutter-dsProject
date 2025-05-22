#!/bin/bash

# Uncomment to debug, will show the execution of each line in this script
# set -x

# Configuration to make the script fail on errors or undefined variables
set -eu -o pipefail

source "$(dirname $0)/exec-functions.sh"

initialize "Model Training and Prediction Process"

# Activate the virtual environment
activate_venv

# Command to run the Python script for data ingestion
echo "Starting execution of the Python script for data ingestion..."
python3 -m cmd.ingest_data


# Final message
finalize

exit 0
