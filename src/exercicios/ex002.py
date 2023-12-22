def funcao(nome):
    return f'É um prazer te conhecer, {nome}'


def pega_nome():
    nome = input('Digite seu nome: ')
    return nome


nome = pega_nome()
print(funcao(nome))
