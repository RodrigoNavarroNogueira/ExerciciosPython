def funcao():
    salario = float(input('Qual é o salário do Funcionário? R$'))
    return f'Um funcionario que ganhava R${salario}, com 15% de aumento, passa a receber R${salario + (salario * 15 / 100):.2f}'


print(funcao())