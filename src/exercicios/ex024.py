def funcao():
    cidade = input('Em que cidade você nasceu? ')
    a = cidade.lower().strip()
    if 'santo' in a:
        return True
    else:
        return False


print(funcao())
