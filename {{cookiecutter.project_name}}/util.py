# Arquivo de funções que serão utilizadas nos cadernos.


def verifica_diretorio(path, cria_dir = True):
    import os
    if not os.path.isdir(path):
        os.mkdir(path)

def salva_modelo_pkl(model, filename, path = './models/'):
    import pickle
    import datetime
    
    suffixe = datetime.datetime.today().strftime("_%d%m%y")  
    nome_arquivo = '{}{}{}'.format(filename, suffixe, '.pkl')
    verifica_diretorio(path)
    
    with open(path+nome_arquivo, 'wb') as file:
        pickle.dump(model, file)


def importa_modelo_pkl(filename, path = './models/'):
    import pickle

    with open(path+filename, 'rb') as arquivo:
        modelo = pickle.load(arquivo)
    return modelo
