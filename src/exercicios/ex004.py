def funcao():
    algo = input('Digite algo: ')
    return f"""
O tipo primitivo desse valor é {type(algo)}
Só tem espaços? {algo.isspace()}
É um número? {algo.isnumeric()}
É alfabetico? {algo.isalpha()}
É alfanumerico? {algo.isalnum()}
Está em maiusculas? {algo.isupper()}
Está em minusculas? {algo.islower()}
Está capitalizada? {algo.istitle()}
"""


print(funcao())