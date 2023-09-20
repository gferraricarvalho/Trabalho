import doctest

def ler_arquivo (nome_arquivo):
    """
    Funçao para ler um arquivo de texto e transformar em uma string.

    Parameters
    ----------
    nome_arquivo : string
        Nome do arquivo ".txt". O arquivo deve estar na mesma pasta do módulo.

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
    
    #tranforma o primeiro retorno da função open em uma string
    datas = str(arquivo[0])
    
    return datas

if __name__ == '__main__': 
    doctest.testmod() 
