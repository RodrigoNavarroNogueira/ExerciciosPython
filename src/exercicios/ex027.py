def funcao():
    nome = input('Digite seu nome: ')
    lista = nome.split()
    return f"""
Muito prazer em te conhecer!
Seu primeiro nome é {lista[0]}
Seu último nome é {lista[-1]}
"""


print(funcao())
