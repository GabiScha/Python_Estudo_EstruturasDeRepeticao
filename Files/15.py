#   15- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#  a) salário bruto.
#  b) quanto pagou ao INSS.
#  c) quanto pagou ao sindicato.
#  d) o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# [
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# ]
# Obs.: Salário Bruto - Descontos = Salário Líquido.


print('--- Impostos ---')

ganha = int(input('Quanto vc ganha por hr: '))

horas = int(input('Quantas hrs vc trabalha por mes: '))

print(' --------------------------------------- ')

salario_bruto = ganha * horas

salario_liquido = salario_bruto - (((salario_bruto / 100) * 11) + ((salario_bruto / 100) * 8) + ((salario_bruto / 100) * 5))

print(f'+ Salário Bruto : R$ {salario_bruto}\n- IR (11%): R${(salario_bruto / 100) * 11}\n- INSS (8%): R${(salario_bruto / 100) * 8}\n- Sindicato (5%): R${(salario_bruto / 100) * 5}\n= Salário Liquido: R${salario_liquido}')



