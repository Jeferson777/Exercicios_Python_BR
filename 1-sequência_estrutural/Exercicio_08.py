'''
8-Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.
'''

valor_hora = float(input('Qual o valor de sua hora trabalhada? '))
horas_mes = int(input('Qual o número de horas trabalhada no mês? '))
salario = valor_hora * horas_mes

print(f'O salário bruto no mês é de: {salario}')