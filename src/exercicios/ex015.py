def funcao():
    km = float(input('Quantidade de KM percorrido: '))
    dias = int(input('Quantos dias? '))
    return f'O total a pagar é de {(dias * 60) + (km * 0.15)}'


print(funcao())