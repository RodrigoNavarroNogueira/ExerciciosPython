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
escolha = None
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
    n = float(input(f'Digite o {n} numero: '))
    lista.append(n) 

lista_str = elementos_lista_de_inteiros(lista)
reverso = list(reversed(lista))
lista_reverso = elementos_lista_de_inteiros_reversos(reverso)

while escolha != 0:
    breakpoint()
    escolha = int(input("Qual a sua escolha?
(0) Para encerrar o programa
(1) Mostrar a lista na ordem direta
(2) Mostrar a lista na ordem inversa"))
    if escolha == 1:
        print(lista_str)
        breakpoint()
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

lista = []

for i in range(1, 51):
    n = (i + 5 + i) % (i + 1)
    lista.append(n)

print(lista)

20)

lista = list()
impares = list()

for n in range(1, 11):
    n = int(input(f'Digite o {n} numero entre 0 á 50: '))
    lista.append(n)
    if n % 2 == 1:
        impares.append(n)

print(lista)
print(impares)

for num in range(0, len(lista), 2):
    num1 = lista[num]
    num2 = lista[num + 1]
    print(num1, num2)

for num in range(0, len(impares), 2):
    try:
        num1 = impares[num]
        num2 = impares[num + 1]
        print(num1, num2)
    except IndexError:
        print(num1)

21)

a = list()
b = list()
c = list()
for n in range(1, 11):
    n = int(input(f'Digite o {n} numero: '))
    a.append(n)

for n in range(1, 11):
    n = int(input(f'Digite o {n} numero: '))
    b.append(n)

indice = 0

for item in a:
    c.append(item - b[indice])
    indice += 1

print(c)

22)

lista1 = list()
lista2 = list()
lista3 = list()
for n in range(1, 11):
    n = int(input(f'Digite o {n} numero: '))
    lista1.append(n)

for n in range(1, 11):
    n = int(input(f'Digite o {n} numero: '))
    lista2.append(n)

indice = 0

for item in lista1:
    if indice == 0:
        lista3.append(item)
    elif indice > 0 and indice % 2 == 0:
        lista3.append(item)
    elif indice > 0 and indice % 2 == 1:
        lista3.append(lista2[indice])
    indice += 1

print(lista3)

23)

lista1 = list()
lista2 = list()
lista3 = list()

for n in range(1, 6):
    n = float(input(f'Digite o {n} numero da primeira lista: '))
    lista1.append(n)
    
for n in range(1, 6):
    n = float(input(f'Digite o {n} numero da segunda lista: '))
    lista2.append(n)
    
indice = 0
escalar = 1

for num in lista1:
    lista3.append((num * escalar) + (lista2[indice] * escalar))
    indice += 1
    escalar += 1

print(lista1)
print(lista2)
print(f'Produto escalar: {sum(lista3)} ')

Primeiro conjunto de números: [1.0, 2.0, 3.0, 4.0, 5.0]
Segundo conjunto de números: [6.0, 7.0, 8.0, 9.0, 10.0]
Produto escalar: 130.0         6   14    24   36

=================================================================================

lista1 = list()
lista2 = list()
lista3 = list()

for n in range(1, 6):
    n = float(input(f'Digite o {n} numero da primeira lista: '))
    lista1.append(n)
    
for n in range(1, 6):
    n = float(input(f'Digite o {n} numero da segunda lista: '))
    lista2.append(n)
    
indice = 0

for num in lista1:
    lista3.append(num * lista2[indice])
    indice += 1

print(lista1)
print(lista2)
print(f'Produto escalar: {sum(lista3)} ')

24)

lista1 = []
lista2 = []
lista3 = []
listas = [lista1, lista2, lista3]

for lista in listas:
    aluno = float(input('Digite o numero do aluno: '))
    altura = float(input('Digite a altura do aluno: '))
    lista.append(aluno)
    lista.append(altura)
    
menor = min(listas, key=lambda lista: lista[1])
maior = max(listas, key=lambda lista: lista[1])
print(f'O menor aluno é o {menor}')
print(f'O maior aluno é o {maior}')
print(lista1)
print(lista2)
print(lista3)

25)

numero = 1

lista = list()
while len(lista) <= 100:
    if numero % 7 != 0:
        lista.append(numero)
    else:
        stri = str(numero)
        if '7' in stri:
            lista.append(numero)
    numero += 1

print(lista)

26)

27)

def contador_divisor(num):
    divisores = 0
    for n in range(1, num + 1):
        if num % n == 0:
            divisores += 1
    return divisores

lista = []
primo = []
posicao = []
for n in range(10):
    num = int(input('Digite um numero maior que 1: '))
    lista.append(num)

    if num == 1 or num % 2 == 0 and num != 2:
        pass
    else:
        divisores = contador_divisor(num)
        if divisores > 2:
            pass
        else:
            primo.append(num)
            posicao.append(lista.index(num))

print(f'os numeros {primo} sao primos e estao na posicões {posicao}')

28)

v = list()
v1 = list()
v2 = list()
utilizados = list()

for n in range(10):
    n = int(input(f'Digite o {n} numero: '))
    v.append(n)
    if n % 2 == 0:
        v2.append(n)
        utilizados.append(n)
    elif n % 2 == 1:
        v1.append(n)
        utilizados.append(n)
print(f'os elementos que foram utilizados no v1 e v2 são: {utilizados}') 

29)

utilizados = list()
pares = list()
soma_pares = 0
impares = list()
qtd_impares = 0

for n in range(6):
    n = int(input(f'Digite o {n} numero: '))
    utilizados.append(n)
    if n % 2 == 0:
        pares.append(n)
        soma_pares += n
    elif n % 2 == 1:
        impares.append(n)
        qtd_impares += 1

print(f'Os numeros pares digitados são {pares}')
print(f'A soma dos numeros pares é {soma_pares}')
print(f'Os numeros imperes digitados são {impares}')
print(f'A quantidade de numeros impares digitados: {qtd_impares}') 

=========================================================

Resolução de exercicio extra:

from collections import Counter

def funcao(): 
    string = input('Digite uma string: ')
    ao = Counter(string)
    for chave in ao:
        if ao[chave] >= 10:
            div = ao[chave] // 9
            print(f'9{chave}' * div, end='')
            resto = ao[chave] % 9
            print(f'{resto}{chave}', end='')
        else:
            print(f'{ao[chave]}{chave}', end='')


ao = funcao()

30)

lista1 = list()
lista2 = list()
lista3 = list()

for n in range(1, 11):
    n = int(input(f'Digite o {n} numero: '))
    lista1.append(n)

for n in range(1, 11):
    n = int(input(f'Digite o {n} numero: '))
    lista2.append(n)

for n in lista1:
    if n in lista2:
        lista3.append(n)

print(lista1)
print(lista2)
print(f'Os elementos que estão repetidos são {lista3}')

31)

lista1 = list()
lista2 = list()
set3 = set()

for n in range(1, 4):
    n = int(input(f'Digite o {n} numero: '))
    lista1.append(n)

for n in range(1, 4):
    n = int(input(f'Digite o {n} numero: '))
    lista2.append(n)

set3 = set(lista1 + lista2)

print(f'A união entre os vetores sem repetir elementos é {set3}')

"""




