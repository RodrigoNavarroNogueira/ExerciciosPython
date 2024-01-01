def pega_numero():
    br = float(input('Quanto dinheiro voce tem na carteira? R$'))
    return f'Com R${br} voce pode comprar US${br / 3.27:.2f}'


print(pega_numero())