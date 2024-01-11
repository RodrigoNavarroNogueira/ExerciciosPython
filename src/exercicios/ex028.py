import random


def abertura():
    print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')


def computador():
    comp = random.randint(0, 5)
    return comp


def jogador():
    jog = int(input('Em que número eu pensei?'))
    return jog


def funcao(comp, jog):
    if jog == comp:
        return f'Parabéns, você venceu!'
    else:
        return f'Errou, pensei no numero {comp} e não no {jog}'


abertura()
comp = computador()
jog = jogador()
print(funcao(comp, jog))
