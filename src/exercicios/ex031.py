def funcao():
    dist = int(input('Qual a distancia da viagem em KM? '))
    if dist <= 200:
        preco = dist * 0.5
    else:
        preco = dist * 0.45
    return f"""
Vc esta prestes a começar uma viagem de {dist} Km
E o preço da sua passagem será de R${preco}
"""


print(funcao())
