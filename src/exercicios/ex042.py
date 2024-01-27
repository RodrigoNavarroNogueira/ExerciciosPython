def funcao():
    a = float(input('Primeiro segmento: '))
    b = float(input('Segundo segmento: '))
    c = float(input('Terceiro segmento: '))

    if a + b > c and a + c > b and b + c > a:
        if a == b and a == c:
            return 'Os segmentos acima PODEM FORMAR triangulo EQUILATERO!'
        elif a == b or a == c:
            return 'Os segmentos acima PODEM FORMAR triangulo! ISOSCELES!'
        elif a != b and a != c:
            return 'Os segmentos acima PODEM FORMAR triangulo! ESCALENO!'
    else:
        return 'Os segmentos acima NÃO PODEM FORMAR triangulo!'


print(funcao())
