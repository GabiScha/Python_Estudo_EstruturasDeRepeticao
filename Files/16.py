#16- Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

print('--- Loja de Tintas ---')

metros = int(input('Por favor, digite o tamanho em metros quadrados da área a ser pintada: '))

print(' --------------------------------------- ')

coberTinta = metros / 3

latas = math.ceil(coberTinta / 18)

total = latas * 80

print(f'A quantidade de latas necessárias é: {latas}\nO preço total das latas é: {total}')

