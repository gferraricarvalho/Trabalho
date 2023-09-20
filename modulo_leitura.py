import doctest

def ler_arquivo (nome_arquivo):
    """
    Funçao para ler um arquivo.

    Parameters
    ----------
    nome_arquivo : string
        Nome do arquivo com a data. O arquivo deve estar na mesma pasta do módulo.

    Returns
    -------
    datas : string
        Retorna as datas que estão escritas no arquivo.
        
    Exemplo
    -------
    >>> ler_arquivo ("texto.txt")
    '13 de agosto 2023 - 10 de agosto de 2023'

    """
    arquivo = open(nome_arquivo).readlines()
    datas = str(arquivo[0])
    
    return datas

if __name__ == '__main__': 
    doctest.testmod() 