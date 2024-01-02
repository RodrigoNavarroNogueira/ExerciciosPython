import math


def funcao():
    graus = int(input('Digite o angulo que voce deseja: '))
    angulo_radianos = math.radians(graus)
    seno = math.sin(angulo_radianos)
    cosseno = math.cos(angulo_radianos)
    tangente = math.tan(angulo_radianos)
    return f"""
O angulo de {graus} tem o seno de {seno:.2f}
O angulo de {graus} tem o cosseno de {cosseno:.2f}
O angulo de {graus} tem a tangente de {tangente:.2f}
"""


print(funcao())
