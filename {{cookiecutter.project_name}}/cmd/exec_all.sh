#!/bin/bash

# Uncomment to debug, will show the execution of each line in this script
# set -x

# Configuration to make the script fail on errors or undefined variables
set -eu -o pipefail

source "$(dirname $0)/exec-functions.sh"

initialize "Model Training and Prediction Process"

# Activate the virtual environment
activate_venv

{% if cookiecutter.use_data_ingestion == "Yes" -%}
# Command to run the Python script for data ingestion
echo "Starting execution of the Python script for data ingestion..."
python3 -m cmd.ingest_data

{% endif -%}
# Command to run the Python script for training the model
echo "Starting execution of the Python script for model training..."
python3 -m cmd.train

# Command to run the Python script for making predictions with the model
echo "Starting execution of the Python script for model prediction..."
python3 -m cmd.predict_new_data

# Final message
finalize

exit 0
