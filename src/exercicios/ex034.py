def funcao():
    salario = int(input('Qual o salario do funcionario? '))
    if salario <= 1250:
        novo_salario = salario + (salario * 15 / 100)
    else:
        novo_salario = salario + (salario * 10 / 100)
    return f'Quem ganhava R${salario} passa a ganhar R${novo_salario} agora'


print(funcao())
