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

lista = []
duplicados = []

for n in range(1, 11):
    n = int(input('Digite um numero: '))
    lista.append(n)

for n in lista:
    num = lista.count(n)
    if num >= 2:
        if n not in duplicados:
            duplicados.append(n)

print(lista)
if len(duplicados) == 0:
    print('Não existem elementos duplicados')
else:
    print(f'Os elementos duplicados são: {duplicados}')

15)

lista = []
duplicados = []

for n in range(1, 21):
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)

print(f'A lista sem repetir os valores será {lista}')

16)

lista = list()
escolha = 4
lista_str = list()
lista_reverso_str = list()

def elementos_lista_de_inteiros(lista):
    for n in lista:
        lista_str.append(str(n))
    lista_completa = ' '.join(lista_str)
    return lista_completa


def elementos_lista_de_inteiros_reversos(reverso):
    for n in reverso:
        lista_reverso_str.append(str(n))
    lista_completa = ' '.join(lista_reverso_str)
    return lista_completa


for n in range(1, 6):
    n = float(input('Digite um numero: '))
    lista.append(n) 

lista_str = elementos_lista_de_inteiros(lista)
reverso = list(reversed(lista))
lista_reverso = elementos_lista_de_inteiros_reversos(reverso)

while escolha != 0:
    escolha = int(input("Qual a sua escolha?
(0) Para encerrar o programa
(1) Mostrar a lista na ordem direta
(2) Mostrar a lista na ordem inversa"))
    if escolha == 1:
        print(lista_str)
    elif escolha == 2:
        print(lista_reverso)
    elif escolha == 0:
        print('Até logo')
    else:
        print('Opção inválida')

17)

lista = list()

for n in range(1, 11):
    n = int(input('Digite um numero: '))
    if n < 0:
        lista.append(0)
    else:
        lista.append(n)

print(lista)

18)

lista = list()

for n in range(10):
    n = int(input(f'Digite o {n + 1}º numero: '))
    lista.append(n)
print(lista)

numero = int(input('Qual será o numero X? '))

for num in lista:
    if numero % num == 0:
        print(f'É divisivel pelo número {num}')

19)



"""
