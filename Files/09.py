#9- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).


print('--- Fahrenheit para Celsius ---')

fahr = int(input('Digite a temperatura em Fahrenheit: '))

cel = 5 * ((fahr-32) / 9)

print('-------------------------------')

print(f'A temperatura em celsius é: {cel}°C')
