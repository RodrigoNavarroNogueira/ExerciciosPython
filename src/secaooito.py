"""
1)

def funcao(numero):
    dobro = numero + numero
    return dobro


def pega_numero():
    numero = int(input('Digite um numero inteiro: '))
    return numero


numero = pega_numero()
print(funcao(numero))

2)

def funcao(meses, data):
    mes = meses.get(data[1])
    print(f'{data[0]} de {mes} de {data[2]}')


def pega_data():
    dia = int(input('Digite a data de hoje: '))
    mes = int(input('Digite o mes: '))
    ano = int(input('Digite o ano: '))
    return dia, mes, ano

meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
data = pega_data()
funcao(meses, data)

3)

def funcao(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0


def pega_numero():
    numero = int(input('Digite um numero: '))
    return numero


numero = pega_numero()
print(funcao(numero))

4)

def funcao(numero):
    if numero <= 0:
        return 'Não é um quadrado perfeito'
    else:
        num = 1
        while True:
            quadrado = num * num
            if quadrado == numero:
                return f'O numero {numero} é um quadrado perfeito.'
            else:
                num += 1
                if num == numero:
                    return 'Não é um quadrado perfeito'
                    break
                

def pega_numero():
    numero = int(input('Digite um numero: '))
    return numero


numero = pega_numero()
print(funcao(numero))

5)

import math

def area(raio):
		return (4 / 3) * math.pi * (raio ** 3)
 

def pega_numero():
    numero = int(input('Digite um numero: '))
    return numero


raio = pega_numero()
print(area(raio))

6)

def funcao(numeros):
    hora = numeros[0] * 3600
    minuto = numeros[1] * 60
    segundos = hora + minuto + numeros[2]
    return f'A quantidade digitada dá {segundos} segundos'
    
    
def pega_numero():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite um numero: '))
    num3 = int(input('Digite um numero: '))
    return num1, num2, num3
    
numeros = pega_numero()
print(funcao(numeros))

7)

def funcao(numeros):
    f = numeros * (9 / 5) + 32
    return f'A temperatura de {numeros} graus Celsius é equivalente a {f:.2f} graus Fahrenheit'
    
    
def pega_numero():
    numero = int(input('Digite um numero: '))
    return numero
    
numeros = pega_numero()
print(funcao(numeros))

8)

def funcao(a, b):
    a = a ** 2
    b = b ** 2
    soma = a + b
    raiz = soma ** (1/2)
    return raiz


a = int(input('Digite um numero '))
b = int(input('Digite um numero '))
print(funcao(a, b))

9)

import math

def funcao(a, b):
    v = math.pi * (b ** 2) * a
    return f'O volume é {v}'


a = int(input('Digite um numero '))
b = int(input('Digite um numero '))
print(funcao(a, b))

10)

def funcao(numeros):
    return max(numeros)


def pega_numero():
    a = int(input('Digite um numero '))
    b = int(input('Digite um numero '))
    return a, b
    
numeros = pega_numero()    
print(funcao(numeros))

11)

def funcao(numeros, letra):
    if letra == 'a':
        media_a = sum(numeros) / 3
        return f' A media aritmetica das notas é {media_a}'
    else:
        p = 0
        for n in numeros:
            mult.append(n * pesos[p])
            p += 1
        soma = sum(mult)
        soma_pesos = sum(pesos)
        media_p = soma / soma_pesos
        return f' A media ponderada das notas é {media_p}'


def pega_numero():
    a = int(input('Digite um numero '))
    b = int(input('Digite um numero '))
    c = int(input('Digite um numero '))
    return a, b, c


def tipo_media():
    letra = input('Qual tipo de média vc deseja? ')
    return letra


mult = []
pesos = 5, 3, 2
numeros = pega_numero()
letra = tipo_media()
print(funcao(numeros, letra))

12)

def funcao(numeros):
    if numeros <= 0:
        print('Numero Inválido')
    else:
        soma = 0
        b = str(numeros)
        for n in b:
            n = int(n)
            soma += n
        print(f'A soma dos algarismos é {soma}')


def pega_numero():
    a = int(input('Digite um numero maior que 0: '))
    return a

13)

def funcao(a, b, sim):
    if sim == '+':
        return a + b
    elif sim == '-':
        return a - b
    elif sim == '/':
        return a / b
    elif sim == '*':
        return a * b


def pega_numero():
    a = int(input('Digite um numero: '))
    b = int(input('Digite um numero: '))
    sim = input('Digite o operador que deseja: ')
    return a, b, sim
    

# numeros = pega_numero()
print(funcao(1, 6, '+'))

14)

def funcao(numeros):
    km = numeros[0] / numeros[1]
    print(km)
    if km < 8:
        return 'Venda o carro'
    elif km >= 8 and km <= 11:
        return 'Economico'
    elif km >= 12:
        return 'Super economico'


def pega_numero():
    a = int(input('Digite um numero: '))
    b = int(input('Quantos litros? '))
    return a, b


numeros = pega_numero()
print(funcao(numeros))

16)

def funcao(numeros):
    return '=' * numeros


def pega_numero():
    a = int(input('Digite um numero: '))
    return a


numeros = pega_numero()
print(funcao(numeros))

17)

def funcao(numeros):
    soma = 0
    for n in range(numeros[0], numeros[1]):
        soma += n
    return soma - 1


def pega_numero():
    a = int(input('Digite um numero: '))
    b = int(input('Digite um numero: '))
    return a, b


numeros = pega_numero()
print(funcao(numeros))

18)

def funcao(x, y):
    return x ** y


def pega_numero():
    a = int(input('Digite um numero: '))
    b = int(input('Digite um numero: '))
    return a, b


# numeros = pega_numero()
print(funcao(2, 4))

22)

def funcao(a):
    for n in range(a + 1):
        print("!" * n)

def pega_numero():
    a = int(input('Enter 1st number: '))
    return a

a = pega_numero()
funcao(a)

23)

def funcao(a):
    for n in range(a + 1):
        print("*" * n)
    for num in range(a - 1, 0, -1):
        print("*" * num)

def pega_numero():
    a = int(input('Enter 1st number: '))
    return a

a = pega_numero()
funcao(a)

26)

def funcao(a):
    soma = 0
    for n in range(1, a + 1):
        soma += n
    return f'A soma de todos os numeros é {soma}'

def pega_numero():
    a = int(input('Enter 1st number: '))
    return a

a = pega_numero()
print(funcao(a))

39)

def funcao(a, b):
    c = a
    d = b
    a = d
    b = c
    return f'Os valores trocados são {a} e {b}'
    
    
def pega_numero():
    a = int(input('Enter 1st number: '))
    return a

# a = pega_numero()
print(funcao(5, 90))

40)

def funcao(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += 1
    return f'O vetor possui {soma} elementos pares'
    
    
def pega_numero():
    while True:
        a = int(input('Enter 1st number: '))
        if a == 0:
            break
        else:
            numeros.append(a)
    return numeros


numeros = []
numeros = pega_numero()
print(funcao(numeros))

41)

def funcao(numeros):
    return max(numeros)
    
    
def pega_numero():
    while True:
        a = int(input('Enter 1st number: '))
        if a == 0:
            break
        else:
            numeros.append(a)
    return numeros


numeros = []
numeros = pega_numero()
print(funcao(numeros))

42)

import statistics

def funcao(numeros):
    return statistics.mean(numeros)
    
    
def pega_numero():
    while True:
        a = int(input('Enter 1st number: '))
        if a == 0:
            break
        else:
            numeros.append(a)
    return numeros


numeros = []
numeros = pega_numero()
print(funcao(numeros))

43)

from random import sample

def funcao():
    lista = sample(range(1, 101), 10)
    return lista


print(funcao())

44)

from random import sample

def funcao():
    a = []
    b = []
    x = sample(range(1, 101), 30)
    for n in x:
        if n % 2 == 0:
            a.append(n)
        else:
            b.append(n)
    return f'Lista A: {a} / Lista B: {b}'


print(funcao())

45)

import numpy as np


def funcao(numeros):
    desvio_padrao = np.std(numeros)
    return f'O desvio padrão do vetor é {desvio_padrao}'
    
    
def pega_numero():
    numeros = []
    while True:
        n = input('Digite um numero: ')
        if n == 'x':
            break
        else:
            n = int(n)
            numeros.append(n)
    return numeros
    
numeros = pega_numero()    
print(funcao(numeros))

46)

import statistics


def funcao(numeros):
    print(numeros)
    print(numeros[::-1])
    print(statistics.mean(numeros))
    
    
def pega_numero():
    numeros = []
    while True:
        n = input('Digite um numero: ')
        if n == 'x':
            break
        else:
            n = int(n)
            numeros.append(n)
    return numeros
    
    
numeros = pega_numero()    
print(funcao(numeros))

47)

def funcao(matriz):
    soma = 0
    for elemento in matriz:
        for numero in elemento:
            if numero > 10:
                soma += 1

    return soma


matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(funcao(matriz))

48)

def funcao(matriz):
    um = matriz[0][1]
    dois = matriz[0][2]
    tres = matriz[1][2]
    return um + dois + tres

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(funcao(matriz))

"""


