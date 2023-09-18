import numpy as np
import pandas as pd
from datetime import datetime 
import calculadata as cd
import modulo_leitura as ml

while True:
    print("Menu:")
    print("1. Fornecer a data no formato 'data inicial - data final'")
    print("2. Ler data de um arquivo de texto")
    print("3. Sair do programa")
    
    escolha = input("Escolha uma opção (1/2/3): ")

    if escolha == '1':
        data_string = input("Digite a data no formato 'Dia de Mês de Ano - DiaFinal de MêsFinal de AnoFinal:':")
        partes = data_string.split('-')
        if len(partes) != 2:
            print("Formato inválido. Use 'data inicial - data final'.")
            continue
        else:
            data_inicial, data_final = cd.calcular_data(data_string)
            print(cd.calcular_diferenca(data_final, data_inicial))
    elif escolha == '2':
        nome_arquivo = input("Digite o nome do arquivo de texto: ")
        data_string = ml.ler_arquivo(nome_arquivo)
        if data_string is not None:
            partes = data_string.split('-')
            if len(partes) != 2:
                print("Formato inválido no arquivo. Use 'data inicial - data final'.")
                continue
            data1 = cd.converter_data(partes[0].strip())
            data2 = cd.converter_data(partes[1].strip())
            print(cd.calcular_diferenca(data1, data2))
        else:
            print(f"Arquivo '{nome_arquivo}' não encontrado.")
    elif escolha == '3':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
