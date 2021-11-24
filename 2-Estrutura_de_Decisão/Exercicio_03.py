'''
3-Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
sexo = input('Informe o Sexo (M ou F): ')

if (sexo == 'M' or sexo == 'm'):
    print(f'{sexo}: Masculino. ')
elif sexo == 'F' or sexo == 'f':
    print(f'{sexo}: Feminino. ')
else:
    print('Valor incorreto!')