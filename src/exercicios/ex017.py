from math import hypot


def funcao():
    catetoa = float(input('Comprimento do cateto oposto: '))
    catetob = float(input('Comprimento do cateto adjacente: '))
    return f'A hipotenusa vai medir {hypot(catetoa, catetob):.2f}'


print(funcao())