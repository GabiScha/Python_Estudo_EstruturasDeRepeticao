#14- João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


print('--- Multa do João ---')

peso = float(input('Digite o peso de peixes em Kg: '))

print('-------------------------------')

if (peso > 50):
    excesso = peso - 50
    multa = int(excesso * 4)
    print(f'O peso total de peixes foi: {peso}Kg. \nO total de kg além do limite foi: {excesso}kg.\nO total da Multa será: R${multa}.')
else:
    print(f'O peso total de peixes foi: {peso}Kg. \nO peso total não ultrapassou o limite, logo não terá que pagar a multa.')


