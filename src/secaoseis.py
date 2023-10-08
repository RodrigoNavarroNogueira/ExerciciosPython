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

39)

base = int(input('Qual a base? '))
altura = int(input('Qual a altura? '))

def area(base, altura):
    area = (base * altura) / 2
    return area


if base <= 0 or altura <= 0:
    print('Voce digitou valores inválidos')
else:
    a = area(base, altura)
    print(a)

40)

num = 0
lista = []
while num >= 0:
    num = int(input('Digite um número positivo, para sair digite um número negativo: '))
    if num > 0:
        lista.append(num)

print(f'O maior número digitado foi {max(lista)} e o menor foi {min(lista)}')

41)

parar = False
while parar == False:
    r1 = int(input('Digite o primeiro resistor: '))
    r2 = int(input('Digite o segundo resistor: '))
    if r1 == 0 or r2 == 0:
        print('O valor 0 foi fornecido, portanto o programa será encerrado.')
        parar = True
    else:
        r = (r1 * r2) / (r1 + r2)
        print(f'Resistor é {r}')

42)

import math

parar = False
lista = []

while parar == False:
    n = float(input('Digite um numero'))
    if n <= 0:
        parar = True
    else:
        lista.append(n)
 
for num in lista:
    print(f'O quadrado do número {num} é {num ** 2}')
    print(f'O cubo do número {num} é {num ** 3}')
    print(f'A raiz quadrada do número {num} é {math.sqrt(num)}')

43)

import statistics

lista = []

while True:
    idade = int(input('Digite uma idade (Para sair pressione 0): '))
    if idade <= 0:
        break
    else:
        lista.append(idade)

print(f'A média das idades é de {statistics.mean(lista)}')

44)

def fibonacci_ate_superior(numero_lido):
    a, b = 0, 1
    fibonacci_sequence = []

    while a <= numero_lido:
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

numero_lido = int(input("Digite um número positivo: "))

if numero_lido <= 0:
    print("Por favor, digite um número positivo.")
else:
    sequencia_fibonacci = fibonacci_ate_superior(numero_lido)
    print(f"Sequência de Fibonacci até o primeiro número superior a {numero_lido}: {sequencia_fibonacci}")

45)

while True:
    escolha = int(input('Escolha uma opção:\n(1) Para converter km/h para m/s\n(2) Para converter m/s para km/h\n(3) Para sair\n'))
    if escolha == 1:
        km = float(input('Digite a velocidade em km/h: '))
        ms = km / 3.6
        print(f'A velocidade convertida em m/s é {ms}')
    elif escolha == 2:
        ms = float(input('Digite a velocidade em m/s: '))
        km = ms * 3.6
        print(f'A velocidade convertida em km/h é {km}')
    elif escolha == 3:
        print('Encerrando programa')
        break

46)

import random

count = 0
numero_sorteado = random.randint(1, 1000)

while True:
    chute = int(input('Qual o seu palpite?'))
    if chute > numero_sorteado:
        print('O chute foi maior que o numero gerado!')
        count += 1
    elif chute < numero_sorteado:
        print('O chute foi menor que o numero gerado!')
        count += 1
    elif chute == numero_sorteado:
        count += 1
        print(f'Parabéns, voce acertou o número sorteado com {count} tentativas!')
        break
        
47)

while True:
    escolha = int(input(""\nSelecione a opção que você deseja:\n 
    [ 1 ] - Adição 
    [ 2 ] - Subtração
    [ 3 ] - Multiplicação
    [ 4 ] - Divisão
    [ 5 ] - Saida\n\n""))

    if escolha == 5:
        print('Encerrando programa')
        break

    num1 = float(input('Qual o primeiro numero? '))
    num2 = float(input('Qual o segundo numero? '))

    if escolha == 1:
        print(num1 + num2)
    elif escolha == 2:
        print(num1 - num2)
    elif escolha == 3:
        print(num1 * num2)
    elif escolha == 4:
        print(num1 / num2)

48)

def fibonacci_ate_superior():
    a, b = 0, 1
    fibonacci_sequence = []

    while a <= 4000000:
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence


def soma_sequencia_fibonacci(sequencia_fibonacci):
    pares_sequencia_fibonacci = []
    for num in sequencia_fibonacci:
        if num % 2 == 0:
            pares_sequencia_fibonacci.append(num)
    
    return sum(pares_sequencia_fibonacci)


sequencia_fibonacci = fibonacci_ate_superior()
print(sequencia_fibonacci)
soma = soma_sequencia_fibonacci(sequencia_fibonacci)
print(f"A soma de todos os termos de valor par na sequencia de Fibonacci é: {soma}")

49)

carlos = float(input('Digite o salario do Carlos: '))
joao = carlos / 3
meses = 0

while joao <= carlos:
    meses += 1
    carlos = carlos + (carlos * 2 / 100)
    joao = joao + (joao * 5 / 100)

print(carlos)
print(joao)
print(f'Depois de {meses} meses, o salário de João será {joao} e de Carlos {carlos}')

50)

chico = 1.5
ze = 1.10
anos = 0

while ze < chico:
    anos += 1
    chico = chico + 0.02
    ze = ze + 0.03

print(f'Será necessário {anos} anos para que Zé alcance Chico, após esse período Zé terá {ze} metros e Chico {chico}')

51)

salario = 2000
ano = 1995
aumento = 0.75

while ano <= 2023:
    ano += 1
    aumento = aumento * 2
    salario = salario + (salario * (aumento) / 100)

print(f'O salário em {ano - 1} será de {salario}')

52)



"""

