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

soma = 0
mult = 1
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

for numero in range(num1, num2 + 1):
    if numero % 2 == 0:
        soma += numero
    elif numero % 2 == 1:
        mult *= numero

print(f'A soma do intervalo dos números pares digitados é {soma} e a multiplicação dos valores impares é {mult}')

22)

import statistics

nota = 10
count = 0
lista = []
while nota >= 10 and nota <=20:
    nota = int(input('Digite sua nota entre 10 a 20: '))
    if nota >= 10 and nota <= 20:
        count += 1
        lista.append(nota)
    else:
        break
print(f'Voce verificou {count} notas e a média delas é {statistics.mean(lista)}')

23)

divisores = []
num = int(input('Digite um numero positivo: '))

for n in range(1, num + 1):
    if num % n == 0:
        divisores.append(n)
valores_formatados = ', '.join(map(str, divisores))

print(f'Os números divisores são {valores_formatados}')

24)

divisores = []
num = int(input('Digite um numero positivo: '))

for n in range(1, num):
    if num % n == 0:
        divisores.append(n)
print(f'A soma dos divisores do número {num} é {sum(divisores)}')

25)

soma = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        soma += n
print(f'A soma dos números que são multiplos de 3 ou 5 é {soma}')

26)

num = int(input('Digite um numero positivo: '))

for n in range(num, 10**9):
    if n % 11 == 0:
        print(f'O primeiro multiplo de 11 encontrado é o {n}')
        break
    elif n % 13 == 0:
        print(f'O primeiro multiplo de 13 encontrado é o {n}')
        break
    elif n % 17 == 0:
        print(f'O primeiro multiplo de 17 encontrado é o {n}')
        break

27)

num = int(input('Digite um numero positivo: '))
soma = 0
for n in range(1, num + 1):
    soma += 1 / n
print(soma)

28)

def fatorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for n in range(1, numero + 1):
            resultado *= n
        return resultado


n = int(input('Digite um numero positivo: '))
e = 1

for i in range(1, n + 1):
    e += 1 / fatorial(i)
print(f"O valor de E é aproximadamente: {e}")

29)

def fatorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado
S = 0

for n in range(5):
    termo = n / fatorial(2 * n)
    S += termo

print(f"O valor da série para 5 termos é: {S}")

30)

num = int(input('Digite um numero positivo: '))
soma_sequencial = 0
soma_impar = 0
soma_alternada = 0


def primeira_sequencia(soma_sequencial):
    for n in range(1, num + 1):
        soma_sequencial += n
    print(soma_sequencial)
    return soma_sequencial


def segunda_sequencia(soma_alternada):
    for i in range(1, num + 1):
        if i % 2 == 1:
            soma_alternada += i
        else:
            soma_alternada -= i
    print(soma_alternada)
    return soma_alternada

def terceira_sequencia(soma_impar):
    for n in range(1, num + 1, 2):
        soma_impar += n
    print(soma_impar)
    return soma_impar


primeira_sequencia(soma_sequencial)
segunda_sequencia(soma_alternada)
terceira_sequencia(soma_impar)

31)

soma = 0

for i in range(1, 51):
    numerador = 2 * i - 1 
    denominador = i      
    termo = numerador / denominador
    soma += termo
print(f"O valor da série S é: {soma}")

32)

from random import randint

continuar = True

while continuar == True:
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(d1)
    print(d2)
    if d1 > d2:
        print('O primeiro dado foi maior')
    elif d2 > d1:
        print('O segundo dado foi maior')
    elif d1 == d2:
        print('Os dados sairam iguais')
    cont = input('Deseja continuar? Para sair digite "não": ')
    if cont == 'não':
        continuar = False

33)

n = int(input('Digite um numero positivo: '))
i = int(input('Digite um numero positivo: '))
j = int(input('Digite um numero positivo: '))

for numero in range(0, n + 3):
    if numero % i == 0 or numero % j == 0 or numero % i == 0 and numero % j == 0:
        print(numero)

34)

import math


def mmc(a, b):
    return a * b // math.gcd(a, b)


mmc_atual = 1

for n in range(1, 21):
    mmc_atual = mmc(mmc_atual, n)

print(f"O menor número divisível por todos os números de 1 a 20 é: {mmc_atual}")

35)

inicio = int(input('Digite o valor inicial: '))
fim = int(input('Até que numero? '))

soma = 0
lista = []
for n in range(inicio, fim + 1):
    if n % 2 == 1:
        lista.append(n)
print(f'A soma de todos os impares entre o intervalo de {inicio} e {fim} é {sum(lista)}')

36)

soma_quadrados = 0
soma_numeros = 0
soma = 0

for n in range(1, 101):
    quadrado = n ** 2
    soma_quadrados += quadrado
    
for n in range(1, 101):
    soma += n
    soma_numeros = soma ** 2

print(f'A diferença entre a soma dos quadrados dos cem primeiros numeros naturais e o quadrado da soma é {soma_numeros} - {soma_quadrados} = {soma_numeros - soma_quadrados}')

37)

import math

for num in range(1000, 9999 + 1):
    num_int = str(num)
    primeira_parte = int(num_int[0] + num_int[1])
    segunda_parte = int(num_int[2] + num_int[3])
    soma = primeira_parte + segunda_parte
    b = math.sqrt(num)
    if soma == b:
        print(num)

38)

a, b, c = 0, 0, 0

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            break
    if a**2 + b**2 == c**2:
        break

print(f"O terno pitagórico é: a = {a}, b = {b}, c = {c}")

"""

