def pega_numero():
    primeira = float(input('Primeira nota do aluno: '))
    segunda = float(input('Segunda nota do aluno: '))
    soma = (primeira + segunda) / 2
    return f' A media entre {primeira} e {segunda} é igual a {soma}'
    

print(pega_numero())
