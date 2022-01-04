"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

numero = input('Insira um valor menor que 1.000: ')
base_decimal = '0123456789'

if len(numero) == 3:  # Validando apenas centenas:
    if numero[0] in base_decimal:
        if numero[1] in base_decimal:
            if numero[2] in base_decimal:
                print(f'{numero[0]} centena(s), {numero[1]} Dezena(s), {numero[2]} Unidade(s)')
elif len(numero) == 2:
    if numero[0] in base_decimal:
        if numero[1] in base_decimal:
            print(f'{numero[0]} Dezena(s), {numero[1]} Unidade(s)')
elif len(numero) == 1:
    if numero[0] in base_decimal:
        print(f'{numero[0]} Unidade(s)')
else:
    print(f'{numero}. Erro! Digite apenas valores menor que 1000!')
