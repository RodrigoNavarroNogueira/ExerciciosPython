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


"""
# 976204000

