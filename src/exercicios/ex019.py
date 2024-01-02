from random import choice

alunos = []


def funcao():
    a1 = input('Primeiro aluno: ')
    a2 = input('Segundo aluno: ')
    a3 = input('Terceiro aluno: ')
    a4 = input('Quarto aluno:')
    alunos.extend([a1, a2, a3, a4])
    return f'O aluno escolhido foi {choice(alunos)}'


print(funcao())