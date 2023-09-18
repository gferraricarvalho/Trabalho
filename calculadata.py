from datetime import datetime
import doctest

def calcular_data(data_string):
    """
    Calcula as datas e divide em data inicial e final

    Parameters
    ----------
    data_string : string
        Recebe a string com a data completa inserida.

    Returns
    -------
    string
        Retorna a data no formato "yyyy-mm-dd" e o horário 00:00:00
        
    Exemplo
    >>> calcular_data("13 de Outubro de 2002")
    datetime.datetime(2002, 10, 13, 0, 0)

    """
    meses = {"Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Juhno": 6, 
             "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
        }
    
    partes = data_string.split()
    dia = int(partes[0])
    mes = meses[partes[2]]
    ano = int(partes[4])

    return datetime(ano, mes, dia)

def calcular_diferenca(data_inicial, data_final):
    """
    Calcula a diferença entre as datas

    Parameters
    ----------
    data_inicial : datetime
        Data inicial inserida
    data_final : datetime
        Data final inserida

    Returns
    -------
    string
        Retorna a diferença, em dias, entre as datas.

    """
    diferenca = data_final - data_inicial
    
    return f"A diferenca entre as datas é de {diferenca.days} dias"

if __name__ == '__main__': 
    doctest.testmod() 