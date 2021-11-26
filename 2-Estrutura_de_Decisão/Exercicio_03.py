'''
3-Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
sexo = input('Informe o Sexo: ').upper()

if (sexo == 'M'):
    print(f'{sexo}: Masculino. ')
elif sexo == 'F':
    print(f'{sexo}: Feminino. ')
else:
    print('Sexo inválido!')