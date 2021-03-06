'''
17-Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de
tinta a serem compradas e os respectivos preços em 3 situações:

1-comprar apenas latas de 18 litros;
2-comprar apenas galões de 3,6 litros;
3-misturar latas e galões, de forma que o area quadrada a ser pintada o desperdício de tinta seja menor. Acrescente 10%
de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

import math

area_a_ser_pintada = float(input('Informe a medida de area a ser pintada: '))

# Definindo a base para calculos:
area_com_folga = area_a_ser_pintada * 1.1
litros_por_metro = 6
litros_a_serem_usados = area_com_folga / litros_por_metro

# Calculo para latas de 18 litros:
litros_por_lata = 18
numero_de_latas = math.ceil(litros_a_serem_usados / litros_por_lata)
valor_latas_tintas = numero_de_latas * 80
print(f'Você deverá usar {numero_de_latas} latas de 18 litros, no valor de R${math.ceil(valor_latas_tintas)},00')

# Calculo para latas de 3,6 litros:
litros_por_galao = 3.6
numero_de_galoes = math.ceil(litros_a_serem_usados / litros_por_galao)
valor_galoes_tintas = numero_de_galoes * 25
print(f'Você deverá usar {numero_de_galoes} latas de 3,6 litros, no valor de R${math.ceil(valor_galoes_tintas)},00')

# Calculo otimizado para sobras de tinta de latas e galões:
numero_de_latas = math.floor(litros_a_serem_usados / litros_por_lata)
valor_latas_tintas = numero_de_latas * 80
litros_faltantes = litros_a_serem_usados % litros_por_lata
numero_de_galoes = math.ceil(litros_faltantes / litros_por_galao)
valor_com_galoes = numero_de_galoes * 25
valor_total = valor_latas_tintas + valor_com_galoes
print(f'Você deverá usar {numero_de_latas} lata(s) de 18 litros mais {numero_de_galoes} galão(s) de 3.6 litros, no valor'
f' de R${valor_total},00')