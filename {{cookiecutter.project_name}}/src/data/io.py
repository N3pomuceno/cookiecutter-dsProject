"""Importing libraries"""

import datetime
import json
import os
import pickle
import sys
from typing import Dict

"""
This script aims to provide functions that will turn modelling process easier.
"""


def read_json_to_dict(file_path: str) -> Dict:
    """
    Reads a JSON file and returns its content as a dictionary.

    Args:
        file_path (str): The full path to the JSON file.

    Returns:
        dict: The content of the JSON file as a dictionary.
    """
    with open(file_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def write_dict_to_json(data: Dict, file_path: str) -> None:
    """
    Writes a dictionary to a JSON file.

    Args:
        data (dict): The dictionary to be written to the file.
        file_path (str): The full path to the file where the dictionary will be saved.
    """
    ensure_directory_exists(os.path.dirname(file_path))  # Ensures the directory exists

    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def ensure_directory_exists(
    directory_path: str, create_if_missing: bool = True
) -> None:
    """
    Checks if the specified directory exists. If not, creates it, based on the `create_if_missing` flag.

    Args:
        directory_path (str): The path of the directory to check.
        create_if_missing (bool, optional): Whether to create the directory if it doesn't exist. Defaults to True.
    """
    if not os.path.isdir(directory_path) and create_if_missing:
        os.makedirs(directory_path, exist_ok=True)


def save_model_as_pkl(
    model: object, filename: str, directory_path: str = "./models/"
) -> None:
    """
    Saves the provided model as a .pkl file in the specified directory.

    Args:
        model (object): The model to save.
        filename (str): The base filename for the saved model.
        directory_path (str, optional): The directory where the model will be saved. Defaults to './models/'.
    """
    suffix = datetime.datetime.today().strftime("_%d%m%y")
    full_filename = f"{filename}{suffix}.pkl"
    ensure_directory_exists(directory_path)

    file_path = os.path.join(directory_path, full_filename)
    with open(file_path, "wb") as file:
        pickle.dump(model, file)


def load_model_from_pkl(filename: str, directory_path: str = "./models/") -> object:
    """
    Loads a model from a .pkl file.

    Args:
        filename (str): The filename of the .pkl file.
        directory_path (str, optional): The directory where the model file is located. Defaults to './models/'.

    Returns:
        object: The loaded model.
    """
    file_path = os.path.join(directory_path, filename)
    with open(file_path, "rb") as file:
        return pickle.load(file)


def get_args(error_message: str = "Missing arguments in CLI.") -> str:
    """
    Get the arguments from the command line.
    """
    args = sys.argv
    if len(args) < 2:
        print(error_message)
        sys.exit(1)
    return args
