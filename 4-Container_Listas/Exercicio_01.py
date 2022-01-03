"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

# Exemplo 01:
lista_1 = list(range(5))
print(lista_1)

# Exemplo 02:
lista_2 = []
for _ in range(5):
    user = float(input("Insira um número: "))
    lista_2.append(user)
    if len(lista_2) == 5:
        print(lista_2)