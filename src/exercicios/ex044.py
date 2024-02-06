def funcao(preco):
    pagamento = int(input("""
FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
"""))
    if pagamento == 1:
        novo_valor = preco - (preco * 10 / 100)
        return f'Sua compra de R${preco} vai custar R${novo_valor} no final'
    elif pagamento == 2:
        novo_valor = preco - (preco * 5 / 100)
        return f'Sua compra de R${preco} vai custar R${novo_valor} no final'
    elif pagamento == 3:
        return f'Sua compra de R${preco} vai custar R${preco} no final pois voce está dividindo em 2x'
    elif pagamento == 4:
        parcelas = int(input('Quantas parcelas? '))
        novo_valor = preco + (preco * 20 / 100)
        print(f'Sua compra será parcelada em {parcelas} vezes de R${novo_valor / parcelas} COM JUROS')
        return f'Sua compra de R${preco} vai custar R${novo_valor} no final'


def valor():
    preco = float(input('Preço das compras: R$'))
    return preco


preco = valor()
print(funcao(preco))
