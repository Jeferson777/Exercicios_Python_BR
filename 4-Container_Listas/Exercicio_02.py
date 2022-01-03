"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

# Exemplo 01 - Lista com uma range pré-determinada:
lista = list(range(10))
lista_float = []
# Removendo, convertendo e reinserindo na lista.
for _ in range(10):
    num_int = lista.pop()
    num_float = float(num_int)
    lista_float.append(num_float)
    if len(lista_float) == 10:
        lista.extend(lista_float)
        print(lista)

# Exemplo 02 - Criando uma lista dinâmicamente:
lista_vazia = []
for _ in range(10):
    num = float(_)
    lista_vazia.append(num)
    if len(lista_vazia) == 10:
        lista_vazia.reverse()
        print(lista_vazia)

# Exemplo 03 - Criando uma lista dinâmica por dados de usuário:
lista_vazia_2 = []
for _ in range(10):
    num = float(input("Insira um número: "))
    lista_vazia_2.append(num)
    if len(lista_vazia_2) == 10:
        lista_vazia_2.sort()
        lista_vazia_2.reverse()
        print(lista_vazia_2)
