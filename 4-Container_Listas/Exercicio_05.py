"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
números IMPARES no vetor impar. Imprima os três vetores.
"""

num_inteiros = list(range(20))
num_pares = []
num_impares = []

for item in num_inteiros:
    if item % 2 == 0:
        num_pares.append(item)
        if len(num_pares) == 10:
            print(f'Pares {num_pares}')
    elif item % 2 == 1:
        num_impares.append(item)
        if len(num_impares) == 10:
            print(f'Impares {num_impares}')
