def funcao():
    numero = input('Informe um numero: ')
    unidade = numero[-1]
    try:
        dezena = numero[-2]
    except IndexError:
        dezena = 0
    try:
        centena = numero[-3]
    except IndexError:
        centena = 0
    try:
        milhar = numero[-4]
    except IndexError:
        milhar = 0
    return f"""
Analisando o numero {numero}
Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}
"""

print(funcao())
