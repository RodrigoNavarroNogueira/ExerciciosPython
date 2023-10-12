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

lista = []

for n in range(1, 11):
    n = int(input('Digite um numero'))
    lista.append(n)

print(f'O maior numero digitado foi {max(lista)} e o menor foi {min(lista)}')

7)

lista = []

for n in range(1, 11):
    n = int(input('Digite um numero: '))
    lista.append(n)
    
print(f'O maior elemento encontrado na lista é o {max(lista)} e ele está na posição {lista.index(max(lista))}')

8)

lista = []

for n in range(1, 7):
    n = int(input('Digite um numero: '))
    lista.append(n)

    
print(f'A ordem reversa dos elementos é {list(reversed(lista))}')

9)

lista = []

for n in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        lista.append(n)
    
print(f'A ordem reversa dos elementos pares é {list(reversed(lista))}')

10)

import statistics

lista = []

for n in range(1, 16):
    n = float(input('Digite a nota do aluno: '))
    lista.append(n)
    
print(f'A media das notas será {statistics.mean(lista)}')

11)

positivos = list()
negativos = 0

for n in range(1, 11):
    n = float(input('Digite um numero: '))
    if n > 0:
        positivos.append(n)
    else:
        negativos += 1
    
print(f'A lista possui {negativos} números negativos e a soma dos pares é {sum(positivos)}')

12)

import statistics

lista = list()

for n in range(1, 6):
    n = float(input('Digite um numero: '))
    lista.append(n)

    
print(lista)
print(f'O maior valor da lista é o {max(lista)}')
print(f'O menor valor da lista é o {min(lista)}')
print(f'A média dos valores é {statistics.mean(lista)}')

13)

lista = list()

for n in range(1, 6):
    n = float(input('Digite um numero: '))
    lista.append(n)

print(f'O maior valor encontra-se na posição {lista.index(max(lista))}, e o menor na posição {lista.index(min(lista))}')

14)



"""
