#13- Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

#   Para homens: (72.7*h) - 58
#   Para mulheres: (62.1*h) - 44.7

print('--- Peso ideal de acordo com o Sexo ---')

h = float(input('Por favor, digite sua altura: '))
sexo = input('Por favor digite seu sexo (F / M): ')


print('-------------------------------')


if (sexo == 'F'):
    
    ideal = (62.1*h) - 44.7
else:

    ideal = (72.7*h) - 58

print(f'Seu peso ideal é {ideal}Kg')



