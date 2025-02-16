#18 Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
import math
print('--- Arquivos e Downloads ---')

tamanho = float(input('Qual o tamanho do arquivo (em MB): '))
velocidade = float(input('Qual a velocidade do link (em Mbps): '))

print(' --------------------------------------- ')

tempo = (tamanho / velocidade) / 60

print(f'O tempo em minutos vai ser (aproximadamente): {math.ceil(tempo)} min')