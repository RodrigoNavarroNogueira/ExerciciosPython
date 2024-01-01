def funcao():
    preco = float(input('Qual é o preço do produto? R$'))
    return f'O produto que custava R${preco}, na promoção de 5% vai custar R${preco - (preco * 5 / 100):.2f}'


print(funcao())