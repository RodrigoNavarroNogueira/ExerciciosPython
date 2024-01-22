def funcao():
    n1 = int(input('Primeiro numero: '))
    n2 = int(input('Segundo numero: '))
    if n1 > n2:
        return 'O primeiro valor é maior'
    elif n1 < n2:
        return 'O segundo valor é maior'
    else:
        return 'Os valores são iguais!'
    

print(funcao())
