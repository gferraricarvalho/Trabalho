from datetime import datetime

def calcular_data(data_string):
    meses = {"Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Juhno": 6, 
             "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
        }
    
    partes = data_string.split()
    dia = int(partes[0])
    mes = meses[partes[2]]
    ano = int(partes[4])

    return datetime(ano, mes, dia)

def calcular_diferenca(data_inicial, data_final):
    diferenca = data_final - data_inicial
    
    return f"A diferenca entre as datas é de {diferenca.days} dias"

