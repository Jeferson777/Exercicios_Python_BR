'''
13-Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
que calcule seu peso ideal, utilizando as seguintes fórmulas:

a)Para
homens: (72.7 * h) - 58
b)Para
mulheres: (62.1 * h) - 44.7
'''

sexo = input('Qual o seu sexo? ')
altura = float(input('Qual a sua altura? '))

if sexo == 'Masculino':
    soma_homem = (72.7 * altura) - 58
    print(f'Seu peso ideal é de {soma_homem}')
else:
    soma_mulher = (62.1 * altura) - 44
    print(f'Seu peso ideal é de {soma_mulher}')
