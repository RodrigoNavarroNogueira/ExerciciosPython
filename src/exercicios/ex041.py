from datetime import datetime


def funcao():
    ano_atual = datetime.now().year
    ano = int(input('Ano de nascimento: '))
    idade = ano_atual - ano
    print(f'O atleta tem {idade} anos')
    if idade <= 9:
        return 'Classificação: MIRIM'
    elif idade > 9 and idade <= 14:
        return 'Classificação: INFANTIL'
    elif idade > 14 and idade <= 19:
        return 'Classificação: JUNIOR'
    elif idade > 19 and idade <= 25:
        return 'Classificação: SENIOR'
    elif idade > 25:
        return 'Classificação: MASTER'


print(funcao())
