'''
5-Faça um programa para a leitura de duas notas parciais de um aluno. O programa
deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

nota_um = float(input('Insira a primeira nota: '))
nota_dois = float(input('Insira a segunda nota: '))

media_notas = nota_um + nota_dois / 4

if media_notas == 10:
    print(f'{media_notas}: Aprovado com distinção!')
elif media_notas >= 7:
    print(f'{media_notas}: Aprovado!')
else:
    print(f'{media_notas}: Reprovado!')

