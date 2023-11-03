"""
1)

def funcao(numero):
    dobro = numero + numero
    return dobro


def pega_numero():
    numero = int(input('Digite um numero inteiro: '))
    return numero


numero = pega_numero()
print(funcao(numero))

2)

def funcao(meses, data):
    mes = meses.get(data[1])
    print(f'{data[0]} de {mes} de {data[2]}')


def pega_data():
    dia = int(input('Digite a data de hoje: '))
    mes = int(input('Digite o mes: '))
    ano = int(input('Digite o ano: '))
    return dia, mes, ano

meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
data = pega_data()
funcao(meses, data)

"""


