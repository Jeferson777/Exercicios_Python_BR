'''
10-Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

temperatura = int(input('Insira a temperatura em Celsius: '))
soma = ((temperatura / 5) * 9) + 32

print(f'A temperatura em Fahrenheit é: {int(soma)}F°')