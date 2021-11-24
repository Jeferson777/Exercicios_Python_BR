'''
9-Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''

temperatura = int(input('Insira a temperatura em Fahrenheit: '))
soma = 5 * ((temperatura - 32) / 9)

print(f'A temperatura em Celsius é: {int(soma)}C°')