"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
Imprima as consoantes.
"""

animal = 'passarinho'
animal = list(animal)

consoantes = 'bcdfghjklmnpqrstvwxyz'
consoantes = list(consoantes)
filtro_consoante = []

# Tratando os dados:
for caractere in animal:
    if caractere in consoantes:  # Filtrando caracteres.:
        filtro_consoante.append(caractere)  # Adicionando o filtro a uma lista.
        cont = filtro_consoante.count(caractere)  # Contando evento de um mesmo caractere.
        if cont > 1:  # Caso haja mais de um mesmo caractere:
            filtro_consoante.remove(caractere)  # Eliminando caractere repetido:

print(f'{len(filtro_consoante)} consoante: {filtro_consoante}')



