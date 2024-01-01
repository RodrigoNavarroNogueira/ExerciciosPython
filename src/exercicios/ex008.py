def pega_numero():
    dist = int(input('Uma distancia em metros: '))
    return f"""
A medida de {dist}m corresponde a:
{dist / 1000}km
{dist / 100}hm
{dist / 10}dam
{dist * 10}dm
{dist * 100}cm
{dist * 1000}mm\n
"""


print(pega_numero())