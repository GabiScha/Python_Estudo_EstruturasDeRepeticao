#10- Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#F = (C × 9/5) + 32.


print('--- Celsius para Fahrenheit ---')

cel = int(input('Digite a temperatura em Celsius: '))

fahr = (cel * 9/5) + 32

print('-------------------------------')

print(f'A temperatura em Fahrenheit é: {fahr}°F')
