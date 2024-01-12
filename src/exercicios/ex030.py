def funcao():
    numero = int(input('Digite um numero qualquer: '))
    if numero % 2 == 0:
        return f'O numero {numero} é PAR'
    else:
        return f'O numero {numero} é IMPAR'
    

print(funcao())
