from random import shuffle


def funcao():
    a1 = input('Primeiro aluno: ')
    a2 = input('Segundo aluno: ')
    a3 = input('Terceiro aluno: ')
    a4 = input('Quarto aluno:')
    alunos = [a1, a2, a3, a4]
    shuffle(alunos)
    return f'A ordem de apresentação será: {alunos}'


print(funcao())