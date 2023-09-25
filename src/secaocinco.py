"""
Lista de exercicios do curso Programação em Python do básico ao avançado da Geek University.

Exercícios Python - Seção 04

1) 

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'O maior número é o {n1}')
elif n2 > n1:
    print(f'O maior número é o {n2}')
else:
    print(f'Os numeros são iguais')

2) 

num = float(input("Digite um número: "))
if num > 0:
    print(num ** 0.5)
elif num == 0:
    print(f'O numero é 0')
else:
    print('Numero inválido')

3) leia um numero real. se o numero for positivo imprima a raiz quadrada, do contrario, imprima o numero
ao quadrado

import math

num = float(input('Digite um numero: '))
if num > 0:
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {raiz}')
else:
    quadrado = num ** 2
    print(f'O quadrado de {num} é {quadrado}')

4)

import math

num = float(input('Digite um numero: '))
if num > 0:
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {raiz}')
    quadrado = num ** 2
    print(f'O quadrado de {num} é {quadrado}')
else:
    print('Digite um numero positivo')

5)

num = int(input('Digite um numero'))

if num % 2 == 0:
    print('O numero é par')
else:
    print('O numero é impar')

6)

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'O maior número é o {n1}')
elif n2 > n1:
    print(f'O maior número é o {n2}')

dif = n1 - n2
print(f'A diferença entre eles é {dif}')

7)

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'O maior número é o {n1}')
elif n2 > n1:
    print(f'O maior número é o {n2}')
else:
    print(f'Os numeros são iguais')

8)

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if n1 < -1 or n2 < -1:
    print('Não é uma nota válida')
elif n1 > 10 or n2 > 10:
    print('Não é uma nota válida')
else:
    print(f'A media entre as notas é de {media}')

9) leia o salario de um trabalhor e o valor da prestacao de um emprestimo, se a prestacao for maior que 20% 
do salario imprima: emprestimo não concedido, caso contrario imprima: emprestimo concedido

salario = float(input('Digite o salario: '))
emprestimo = float(input('Digite o valor a prestação: '))
porcentagem = (emprestimo / salario) * 100
print(f'{porcentagem:.1f}')
if porcentagem > 20:
    print('Emprestimo negado')
else:
    print('Emprestimo concedido')

10)

altura = float(input('Qual a sua altura? '))
sexo = input('Qual seu sexo? (F) Feminino (M) Masculino')
peso_homem = (72.7 * altura) - 58
peso_mulher = (62.1 * altura) - 44.7

if sexo == 'f':
    print(f'O peso ideal para as mulheres é de {peso_mulher}')
elif sexo == 'm':
    print(f'O peso ideal para os homens é de {peso_homem}')

"""
