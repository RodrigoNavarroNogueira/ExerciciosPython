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

"""

