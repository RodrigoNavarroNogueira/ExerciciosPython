"""
1)

a = []

a.append(1)
a.append(0)
a.append(5)
a.append(-2)
a.append(-5)
a.append(7)
soma = a[0] + a[1] + a[5]
print(f'A soma é {soma}')
a.insert(4, 100)
for n in a:
    print(n)

2)

lista = []

for n in range(1, 7):
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    
print(f'Os numeros digitados foram: {lista}')

3)

numeros = []
quadrados = []
for n in range(1, 11):
    n = float(input('Digite um numero: '))
    numeros.append(n)
    quadrados.append(n ** 2)

print(numeros)
print(quadrados)

4)

lista = []

for n in range(1, 9):
    n = int(input('Digite um numero: '))
    lista.append(n)

valor_um = int(input('Digite o indice que deseja somar: '))
valor_dois = int(input('Digite o indice numero que deseja somar: '))

print(f'A soma entre os indices é {lista[valor_um] + lista[valor_dois]}')

5)

pares = 0

for n in range(1, 11):
    n = int(input('Digite um numero'))
    if n % 2 == 0:
        pares += 1

print(f'Voce digitou {pares} pares')

6)



"""
