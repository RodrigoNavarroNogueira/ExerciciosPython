def pega_numero():
    numero = int(input('Digite um numero para ver sua tabuada: '))
    return numero


def funcao(numero):
    print('--------------')
    for n in range(1, 11):
        print(f'{numero} x  {n} = {numero * n}')
    print('--------------')


numero = pega_numero()
funcao(numero)