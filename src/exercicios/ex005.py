def pega_numero():
    numero = int(input('Digite um numero: '))
    return f'Analisando o valor {numero}, seu antecessor é {numero - 1} e o sucessor é {numero + 1}'


print(pega_numero())