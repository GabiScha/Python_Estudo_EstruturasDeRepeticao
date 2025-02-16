#17- Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     - comprar apenas latas de 18 litros;
#     - comprar apenas galões de 3,6 litros;
#     - misturar latas e galões, de forma que o desperdício de tinta seja menor. Sempre arredonde os valores para cima, isto é, considere latas cheias.


import math

print('--- Loja de Tintas ⅠⅠ ---')

metros = float(input('Por favor, digite o tamanho em metros quadrados da área a ser pintada: '))

print(' --------------------------------------- ')
print(' -- Apenas latas de 18L --')

coberTinta = metros / 6

latas = math.ceil(coberTinta / 18)

total18 = latas * 80



print(f'A quantidade de latas necessárias é: {latas}\nO preço total das latas é: {total18}')

print(' --------------------------------------- ')
print(' -- Apenas latas de 3.6L --')



latas = math.ceil(coberTinta / 3.6)

total36 = latas * 25



print(f'A quantidade de latas necessárias é: {latas}\nO preço total das latas é: {total36}')


print(' --------------------------------------- ')
print(' -- latas de 18 e 3.6 L --')




if coberTinta >= 18:
    latas = int(coberTinta / 18)

    res = coberTinta - (latas * 18)

    res = math.ceil(res / 3.6)

    totaltd = latas * 80 + res * 25

    print(f'A quantidade de latas de 18L necessárias é: {latas}\nA quantidade de latas de 3.6L necessárias é: {res}\nO preço total das latas é: {totaltd}')

else:
    latas = math.ceil(coberTinta / 3.6)

    totaltd = latas * 25
    print(f'A quantidade de latas de 18L necessárias é: Nenhuma\nA quantidade de latas de 3.6L necessárias é: {latas}\nO preço total das latas é: {totaltd}')


print(' --------------------------------------- ')


if total18 <= total36 and total18 <= totaltd: # se a opção de 18 for menor que todos, ela é a melhor
    
    print("O melhor é a opção Apenas de 18L")

elif total36 <= total18 and total36 <= totaltd: # se a opção de 3.6 for menor que todos, ela é a melhor

    print("O melhor é a opção Apenas de 3.6L")

else:

    print("O melhor é usar as duas juntas") # se se nenhuma das outras forem menor que as duas juntas, ela é a melhor







