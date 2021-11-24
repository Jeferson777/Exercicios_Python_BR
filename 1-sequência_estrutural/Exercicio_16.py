'''
16-Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

metro_quadrado = float(input("Informe a metragem: "))

valor_lata_tinta = 80.00
cobertura_lata_tinta = 3 * 18 # 54 metros

if metro_quadrado <= cobertura_lata_tinta:
    print(f'Latas a comprar: 01 unidade, Valor: {valor_lata_tinta}0')
elif metro_quadrado > cobertura_lata_tinta and metro_quadrado <= cobertura_lata_tinta * 2:
    print(f'Latas a comprar: 02 unidade, Valor: {valor_lata_tinta * 2}0')
elif metro_quadrado > cobertura_lata_tinta * 2 and metro_quadrado <= cobertura_lata_tinta * 3:
    print(f'Latas a comprar: 03 unidade, Valor: {valor_lata_tinta * 3}0')
elif metro_quadrado > cobertura_lata_tinta * 3 and metro_quadrado <= cobertura_lata_tinta * 4:
    print(f'Latas a comprar: 04 unidade, Valor: {valor_lata_tinta * 4}0')
elif metro_quadrado > cobertura_lata_tinta * 4 and metro_quadrado <= cobertura_lata_tinta * 5:
    print(f'Latas a comprar: 05 unidade, Valor: {valor_lata_tinta * 5}0')
elif metro_quadrado > cobertura_lata_tinta * 5 and metro_quadrado <= cobertura_lata_tinta * 6:
    print(f'Latas a comprar: 06 unidade, Valor: {valor_lata_tinta * 6}0')
else:
    print('Erro!')



