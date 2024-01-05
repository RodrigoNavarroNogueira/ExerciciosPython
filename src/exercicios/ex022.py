def funcao():
    nome = input('Digite seu nome completo: ')
    return f"""
Analisando seu nome...
Seu nome em maiusculas é {nome.upper()}
Seu nome em minusculas é {nome.lower()}
Seu nome tem ao todo {len(nome) - nome.count(' ')} letras
Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras
"""


print(funcao())
