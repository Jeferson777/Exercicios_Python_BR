'''
15-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
programa que nos dê:

a)salário bruto.
b)quanto pagou ao INSS.
c)quanto pagou ao sindicato.
d)o salário líquido.
e)calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

valor_hora = float(input('Qual o valor de sua hora trabalhada? '))
horas_mes = int(input('Qual o número de horas trabalhada no mês? '))

salario_bruto = valor_hora * horas_mes
print(f'Salário Bruto: R${salario_bruto}0')
IR = (salario_bruto / 100) * 11
print(f'Desconto de Imposto de Renda: R${IR}0')
INSS = (salario_bruto / 100) * 8
print(f'Desconto de INSS: R${INSS}0')
sindicato = (salario_bruto / 100) * 5
print(f'Desconto de Sindicato: R${sindicato}0')

soma_descontos = IR + INSS + sindicato
salario_liquido = salario_bruto - soma_descontos
print(f'Salário Líquido é de: R${salario_liquido}0')
