def funcao():
    largura = float(input('Largura da parede:'))
    altura = float(input('Altura da parede: '))
    mq = largura * altura
    tinta = mq / 2
    return f"""
Sua parede tem dimensão de {largura}x{altura} e sua área é de {mq}m/2
Para pintar a parede, voce precisará de {tinta}L de tinta
"""


print(funcao())