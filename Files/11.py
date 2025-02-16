#11- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

print('--- Inteiros e Reais ---')

int1 = int(input('Por favor, digite o primeiro número inteiro: '))
int2 = int(input('Por favor, digite o segundo número inteiro: '))
real = float(input('Por favor, digite o número real: '))


print('-------------------------------')

#  a) o produto do dobro do primeiro com metade do segundo .

produto = (int1 * 2) + (int2 / 2)
print(f'a) {produto}')

#  b) a soma do triplo do primeiro com o terceiro.

soma = (int1 * 3) + real
print(f'b) {soma}')

#  c) o terceiro elevado ao cubo.

cubo = real * real * real

print(f'c) {cubo}')

