'''
16-Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

import math

area_a_ser_pintada = float(input('Informe a medida de area a ser pintada: '))

# Definindo a base para calculos:
litros_por_metro = 3
litros_a_serem_usados = area_a_ser_pintada / litros_por_metro

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