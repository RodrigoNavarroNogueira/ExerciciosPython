def funcao():
    frase = input('Digite uma frase ').strip().lower()
    qtd = frase.count('a')
    return f"""
A letra A aparece {qtd} vezes na frase
A primeira letra A apareceu na posição {frase.index('a') + 1}
A ultima letra A apareceu na posicação {frase.rindex('a') + 1}
"""


print(funcao())

