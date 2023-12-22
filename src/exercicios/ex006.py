import math


def pega_numero():
    numero = int(input('Digite um numero: '))
    return f"""
O dobro de {numero} vale {numero * 2}
O triplo de {numero} vale {numero * 3}
A raiz quadrada de {numero} é igual a {math.sqrt(numero):.2f}

"""


print(pega_numero())
