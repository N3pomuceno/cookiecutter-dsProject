from typing import Dict
import json
import os
import pickle
import datetime


def json_to_dict(path: str, name: str) -> Dict:
    """Lê um arquivo JSON e retorna um dicionário."""
    with open(os.path.join(path, name), 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def dict_to_json(data: Dict, path: str, name: str) -> None:
    """Converte um dicionário para um arquivo JSON no diretório especificado."""
    verifica_diretorio(path)  # Garante que o diretório exista

    with open(os.path.join(path, name), 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def verifica_diretorio(path: str, cria_dir: bool = True) -> None:
    """Verifica se o diretório existe. Se não, cria um novo diretório, caso cria_dir seja True."""
    if not os.path.isdir(path) and cria_dir:
        os.mkdir(path)


def salva_modelo_pkl(model: object, filename: str, path: str = './models/') -> None:
    """Salva o modelo como um arquivo .pkl no diretório especificado."""
    suffixe = datetime.datetime.today().strftime("_%d%m%y")  
    nome_arquivo = '{}{}{}'.format(filename, suffixe, '.pkl')
    verifica_diretorio(path)
    
    with open(os.path.join(path, nome_arquivo), 'wb') as file:
        pickle.dump(model, file)


def importa_modelo_pkl(filename: str, path: str = './models/') -> object:
    """Carrega e retorna o modelo a partir de um arquivo .pkl."""
    with open(os.path.join(path, filename), 'rb') as arquivo:
        modelo = pickle.load(arquivo)
    return modelo
