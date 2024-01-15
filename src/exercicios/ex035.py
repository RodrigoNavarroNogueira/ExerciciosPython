def funcao():
    a = float(input('Primeiro segmento: '))
    b = float(input('Segundo segmento: '))
    c = float(input('Terceiro segmento: '))

    if a + b > c and a + c > b and b + c > a:
        return 'Os segmentos acima PODEM FORMAR triangulo!'
    else:
        return 'Os segmentos acima NÃO PODEM FORMAR triangulo!'


print(funcao())
