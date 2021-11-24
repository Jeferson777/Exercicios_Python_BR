'''
4-Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

nota_1 = float(input('Insira a primeira nota: '))
nota_2 = float(input('Insira a segunda nota: '))
nota_3 = float(input('Insira a terceira nota: '))
nota_4 = float(input('Insira a quarta nota: '))
media_total = sum([nota_1, nota_2, nota_3, nota_4]) / 4

print(f'A Média total é de: {media_total}')