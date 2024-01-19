def funcao():
    valor = int(input('Qual o valor da casa? '))
    salario = int(input('Qual seu salario? '))
    anos = int(input('Em quantos anos pretende pagar? '))
    parcela = (valor / anos) / 12
    renda = salario * 30 / 100
    print(f'Para pagar uma casa de {valor} em {anos} anos a prestação será de {parcela:.2f}')
    if renda > parcela:
        return 'Emprestimo CEDIDO!'
    else:
        return 'Emprestimo NEGADO!'


print(funcao())
