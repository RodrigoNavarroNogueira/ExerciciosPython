def funcao():
    nome = input('Qual é seu nome completo? ').lower()
    if 'silva' in nome:
        return True
    else:
        return False
    
    
a = funcao()
print(f'Seu nome tem Silva? {a}')