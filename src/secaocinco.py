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

11)

num = input('Digite um numero ')
inteiro = int(num)
if inteiro > 0:
    lista = []
    soma = 0
    for n in num:
        lista.append(n)
    for num in lista:
        numero = int(num)
        soma += numero
    print(f'A soma dos algarismos é: {soma}')
else:
    print('Numero invalido')

12)

import math

num = float(input("Digite um número positivo: "))
if num < 0:
    print('Numero invalido')
else:
    logaritmo = math.log(num)
    print(f'O logaritmo é {logaritmo}')

13)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota "))

media_ponderada = (nota1 + nota2 + (nota3 * 2)) / 4
print(media_ponderada)
if media_ponderada >= 60:
    print('O aluno foi aprovado')
else:
    print('O aluno foi reprovado')

14)

trabalho_de_laboratorio = float(input("Digite a primeira nota: "))
avaliacao_semestral = float(input("Digite a segunda nota: "))
exame_final = float(input("Digite a terceira nota "))

peso1 = 2
peso2 = 3
peso3 = 5

media_ponderada = (trabalho_de_laboratorio * peso1 + avaliacao_semestral * peso2 + exame_final * peso3) / (peso1 + peso2 + peso3)
print(media_ponderada)
if media_ponderada >= 5:
    print('O aluno foi aprovado')
elif media_ponderada >= 3 or media_ponderada <= 4.9:
    print('O aluno ficou de recuperação')
else:
    print('O aluno foi reprovado')

15)

num = int(input("Digite um numero entre 1 e 7: "))
if num == 1:
    print(f'O número {num} corresponde ao Domingo.')
elif num == 2:
    print(f'O número {num} corresponde a Segunda-feira.')
elif num == 3:
    print(f'O número {num} corresponde a Terça-feira.')
elif num == 4:
    print(f'O número {num} corresponde a Quarta-feira.')
elif num == 5:
    print(f'O número {num} corresponde a Quinta-feira.')
elif num == 6:
    print(f'O número {num} corresponde a Sexta-feira.')
elif num == 7:
    print(f'O número {num} corresponde ao Sábado.')
else:
    print('Número invalido')

16)

num = int(input("Digite um numero entre 1 e 12: "))
if num == 1:
    print(f'O número {num} corresponde a Janeiro.')
elif num == 2:
    print(f'O número {num} corresponde a Fevereiro.')
elif num == 3:
    print(f'O número {num} corresponde a Março.')
elif num == 4:
    print(f'O número {num} corresponde a Abril.')
elif num == 5:
    print(f'O número {num} corresponde a Maio.')
elif num == 6:
    print(f'O número {num} corresponde a Junho.')
elif num == 7:
    print(f'O número {num} corresponde ao Julho.')
elif num == 8:
    print(f'O número {num} corresponde ao Agosto.')
elif num == 9:
    print(f'O número {num} corresponde ao Setembro.')
elif num == 10:
    print(f'O número {num} corresponde ao Outubro.')
elif num == 11:
    print(f'O número {num} corresponde ao Novembro.')
elif num == 12:
    print(f'O número {num} corresponde ao Dezembro.')
else:
    print('Número invalido')

17)

base_maior = float(input('Qual a base maior?'))
base_menor = float(input('Qual a base menor?'))
altura = float(input('Qual a altura?'))
if base_maior and base_maior > 0:
    area = (base_maior + base_menor) * altura / 2
    print(f'A área é {area}')
else:
    print('O numero precisa ser maior que zero')

18)

operacao = int(input('Qual operação voce deseja realizar? (1) Adição (2) Subtração (3) Multiplicação (4) Divisão'))
num1 = float(input('Qual o primeiro numero? '))
num2 = float(input('Qual o segundo numero? '))

if operacao == 1:
    print(num1 + num2)
elif operacao == 2:
    print(num1 - num2)
elif operacao == 3:
    print(num1 * num2)
elif operacao == 4:
    print(num1 / num2)

19)

num = int(input('Digite um numero '))

if num % 3 == 0 or num % 5 == 0:
    if num % 3 == 0 and num % 5 == 0:
        print('O número digitado é divisivel por 3 e 5')
    else:
        print('É divisivel por 3 ou 5')
else:
    print('O número não é divisivel por 3 ou 5')

20)

A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))

if A + B > C and A + C > B and B + C > A:
    if A == B == C:
        print("É um triângulo equilátero.")
    elif A != B and A != C and B != C:
        print("É um triângulo escaleno.")
    else:
        print("É um triângulo isósceles.")
else:
    print("Não é um triângulo válido.")

"""

