from datetime import datetime


def funcao():
    ano = int(input('Digite o ano que quer analisar, coloque 0 para ver o ano atual: '))
    if ano == 0:
        ano = datetime.now().year
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return f'O ano {ano} é bissexto'
            else:
                return f'O ano {ano} não é bissexto'
        else:
            return f'O ano {ano} é bissexto'
    else:
        return f'O ano {ano} não é bissexto'


print(funcao())
