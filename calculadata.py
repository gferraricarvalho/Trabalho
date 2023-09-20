from datetime import datetime
import doctest

def calcular_data(data_string):
    """
    Transforma as datas adicionadas em data inicial e final no formato datetime.

    Parameters
    ----------
    data_string : string
        Recebe a string com a data completa inserida.

    Returns
    -------
    string
        Retorna as datas inicial e final no formato "yyyy-mm-dd" e o horário 00:00:00
        
    Exemplo
    >>> calcular_data("13 de Outubro de 2002 - 10 de Outubro de 2002")
    (datetime.datetime(2002, 10, 10, 0, 0), datetime.datetime(2002, 10, 13, 0, 0))

    """
    
    #trnsforma os meses em número
    meses = {"Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Juhno": 6, 
             "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
        }
    
    #divide as partes em dia, mÊs e ano
    partes = data_string.split()
    dia_1 = int(partes[0])
    mes_1 = meses[partes[2]]
    ano_1 = int(partes[4])

    dia_2 = int(partes[6])
    mes_2 = meses[partes[8]]
    ano_2 = int(partes[10])
    
    #transforma para o formato datetime
    data_inicial = datetime(ano_1, mes_1, dia_1)
    data_final = datetime(ano_2, mes_2, dia_2)

    return data_final, data_inicial

def calcular_diferenca(data_inicial, data_final):
    """
    Calcula a diferença entre as datas.

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
