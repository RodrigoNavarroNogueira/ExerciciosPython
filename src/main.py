"""
# Exercicio Caixa Eletronico

saque = int(input('Quanto voce deseja sacar? '))

notas_cem = saque // 100
resto_cem = saque % 100
notas_cinquenta = resto_cem // 50
resto_cinquenta = resto_cem % 50
notas_vinte = resto_cinquenta // 20
resto_vinte = resto_cinquenta % 20
notas_dez = resto_vinte // 10
resto_dez = resto_vinte % 10
notas_cinco = resto_dez // 5
resto_cinco = resto_dez % 5
notas_dois = resto_cinco // 2
resto_dois = resto_cinco % 2
notas_um = resto_dois // 1
resto_um = resto_dois % 1

print(f'Para sacar R${saque}, será necessário as seguintes notas:
{notas_cem} notas de 100
{notas_cinquenta} notas de 50
{notas_vinte} notas de 20
{notas_dez} notas de 10
{notas_cinco} notas de 5
{notas_dois} notas de 2
{notas_um} notas de 1')

# Exercicio da entrevista usando o Counter

from collections import Counter

def funcao(): 
    string = input('Digite uma string: ')
    ao = Counter(string)
    for chave in ao:
        if ao[chave] >= 10:
            div = ao[chave] // 9
            print(f'9{chave}' * div, end='')
            resto = ao[chave] % 9
            print(f'{resto}{chave}', end='')
        else:
            print(f'{ao[chave]}{chave}', end='')

ao = funcao()

"""
