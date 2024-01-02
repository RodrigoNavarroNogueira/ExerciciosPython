def funcao():
    celsius = float(input('Informe a temperatura em Celsius: '))
    return f'A temperatura de {celsius} corresponde á {(celsius * 9 / 5) + 32}'


print(funcao())