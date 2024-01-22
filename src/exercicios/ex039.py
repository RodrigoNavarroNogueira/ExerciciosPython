from datetime import datetime


def funcao():
    ano_atual = datetime.now().year
    ano = int(input('Ano de nascimento: '))
    idade = ano_atual - ano
    print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}')
    if idade < 18:
        b = 18 - idade
        print(f'Ainda faltam {18 - idade} anos para o alistamento')
        print(f'Seu alistamento será em {ano_atual + b}')
    if idade > 18:
        print(f'Você já deveria ter se alistado há {idade - 18} anos')
        print(f'Seu alistamento foi em {ano_atual - (idade - 18)}')
    if idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!')


funcao()
