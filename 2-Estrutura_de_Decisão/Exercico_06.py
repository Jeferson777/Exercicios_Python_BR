'''
6-Faça um Programa que leia três números e mostre o maior deles.
'''
a = int(input('Insira um número: '))
b = int(input('Insira um número: '))
c = int(input('Insira um número: '))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)