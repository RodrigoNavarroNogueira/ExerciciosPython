import random


def funcao(pc):
    lista = ['pedra', 'papel', 'tesoura']
    jogador = int(input("""
Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada? 
"""))
    print(f'Jogador jogou: {lista[jogador].title()}')
    print(f'Computador jogou: {lista[pc].title()}')
    if jogador == 0 and pc == 0 or jogador == 1 and pc == 1 or jogador == 2 and pc == 2:
        return 'Empate!'
    elif jogador == 0 and pc == 1:
        return 'O COMPUTADOR VENCEU!'
    elif jogador == 0 and pc == 2:
        return 'O JOGADOR VENCEU!'
    elif jogador == 1 and pc == 0:
        return 'O JOGADOR VENCEU!'
    elif jogador == 1 and pc == 2:
        return 'O COMPUTADOR VENCEU!'
    elif jogador == 2 and pc == 0:
        return 'O COMPUTADOR VENCEU!'
    elif jogador == 2 and pc == 1:
        return 'O JOGADOR VENCEU!'


def computador():
    pc = random.randint(0, 2)
    return pc


pc = computador()
print(funcao(pc))
