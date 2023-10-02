"""
1)

for num in range(1, 16):
    if num % 3 == 0:
        print(num)

2)

for num in range(1, 101):
    print(num)

num = 1

while num < 101:
    print(num)
    num += 1

num = 1

while num < 101:
    print(num)
    num += 1

count = 0
while count <= 2:
    for num in range(1, 101):
        print(num)
    count += 1

3)

num = 10

while num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(num)
    num -= 1
print('FIM!')

4)

for num in range(0, 100001, 1000):
    print(num)

5)

soma = 0

for num in range(1, 11):
    num = int(input('Digite um valor: '))
    soma += num
print(f'A soma de todos os números é {soma}')

6)

import statistics

lista = []

for num in range(1, 11):
    num = int(input('Digite um valor: '))
    lista.append(num)
print(f'A média dos números é {statistics.mean(lista)}')

7)

import statistics

lista = []

for num in range(1, 11):
    num = int(input('Digite um valor: '))
    if num > 0:
        lista.append(num)
print(f'A média dos números é {statistics.mean(lista)}')

8)

lista = []

for num in range(1, 11):
    num = int(input('Digite um valor: '))
    lista.append(num)
print(f'Menor valor: {min(lista)}')
print(f'Maior valor: {max(lista)}')

9)

num = int(input('Digite um numero: '))

for n in range(1, num + 1):
    if n % 2 == 1:
        print(n)

10)

soma = 0

for n in range(1, 51):
    if n % 2 == 0:
        soma += n
print(soma)

11)

num = int(input('Digite um numero inteiro positivo: '))

for n in range(0, num + 1):
    print(n)

12)

num = int(input('Digite um numero inteiro positivo: '))

for n in range(num, 0, -1):
    print(n)

13)

num = int(input('Digite um numero inteiro positivo par: '))

for n in range(0, num + 1):
    if n % 2 == 0:
        print(n)

14)

num = int(input('Digite um numero inteiro positivo par: '))

for n in range(num, -1, -1):
    if n % 2 == 0:
        print(n)

15)

num = int(input('Digite um numero inteiro positivo impar: '))
if num % 2 == 1:
    for n in range(1, num + 1):
        if n % 2 == 1:
            print(n)
else:
    print('Não digitou um número impar')

16)

num = int(input('Digite um numero inteiro positivo impar: '))
if num % 2 == 1:
    for n in range(num, -1, -1):
        if n % 2 == 1:
            print(n)
else:
    print('Não digitou um número impar')

17)

soma = 0
num = int(input('Digite um numero inteiro positivo: '))

for n in range(0, num + 1):
    soma += n
print(soma)

18)

lista = []
qtd = int(input('Quantos números voce quer ler?: '))
for vezes in range(1, qtd + 1):
    num = int(input('Digite um número?'))
    lista.append(num)
print(f'O mair número que voce digitou foi {max(lista)}, e ele apareceu {lista.count(max(lista))} vezes')

19)

num = input('Digite um numero inteiro entre 100 e 999: ')

print(num[0])
print(num[1])
print(num[2])

20)

num = 0
count_total = 0
count_pares = 0
while num != 1000:
    n = int(input('Digite um numero: '))
    count_total += 1
    if n % 2 == 0:
        count_pares += 1
    num = n
print(f'Foi lido {count_total - 1} dados e {count_pares - 1} são pares.')

21)

"""
