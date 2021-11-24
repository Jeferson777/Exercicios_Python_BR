'''
11-Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
'''

int_1 = int(input('Insira um número inteiro: '))
int_2 = int(input('Insira outro número inteiro: '))
real = float(input('Insira um número real: '))

a_ = (int_1 * 2) + (int_2 / 2)
b_ = (int_1 * 3) + real
c_ = real**3

print(f'O produto do dobro do primeiro com metade do segundo: {a}')
print(f'A soma do triplo do primeiro com o terceiro: {b}')
print(f'O terceiro elevado ao cubo: {c}')
