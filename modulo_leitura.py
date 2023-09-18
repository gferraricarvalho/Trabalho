import numpy as np
import pandas as pd
import doctest
import datetime

def ler_arquivo (nome_arquivo):
    """
    Funçao para ler o arquivo.

    Parameters
    ----------
    nome_arquivo : string
        Nome do arquivo com a data. O arquivo deve estar na mesma pasta do módulo.

    Returns
    -------
    datas : string
        Retorna as datas que estão escritas no arquivo.

    """
    arquivo = open(nome_arquivo).readlines()
    datas = str(arquivo[0])
    
    return datas

print(ler_arquivo("texto.txt"))