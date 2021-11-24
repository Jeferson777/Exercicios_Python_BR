'''
18-Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do
arquivo usando este link (em minutos).
'''

arquivo = int(input('Insira o tamanho do arquivo: '))
link_internet = int(input('Insira a velocidade da internet: '))

soma = (link_internet / 8) * (arquivo / 60)

print(f'O tempo estimado de download do arquivo é de {int(soma)} minutos')
