'''
4-Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = input('Digite uma letra: ')

vogais = 'aeiouwy'
vogais = list(vogais)
consoantes = 'bcdfghjklmnpqrstvwxz'
consoantes = list(consoantes)

if letra in vogais:
    print(f'{letra}: Vogal.')
elif letra in consoantes:
    print(f'{letra}: Consoante.')
else:
    print('Letra incorreta!')