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

21)

escolha = int(input("Digite a opção:
    1 - Soma de dois numeros
    2 - Diferença entre dois numeros
    3 - Produto entre dois numeros
    4 - Divisão entre dois numeros"))

num1 = float(input('Digite um numero'))
num2 = float(input('Digite o outro numero'))

if escolha == 1:
    print(num1 + num2)
elif escolha == 2:
    if num1 > num2:
        print(f'O numero {num1} é maior')
        print(num1 - num2)
    else:
        print(f'O numero {num2} é maior')
        print(num2 - num1)
elif escolha == 3:
    print(f'O produto é {num1 * num2}')
elif escolha == 4:
    if num2 == 0:
        print('O denominador não pode ser 0')
    else:
        print(num1 / num2)

22)

idade = int(input('Idade: '))
servico = int(input('Quantos anos de serviço? '))

if idade >= 65:
    print('Pode se aposentar pela idade')
elif servico >= 30:
    print('Pode se aposentar polo tempo de serviço')
elif idade >= 60 and servico >= 25:
    print('Pode se aposentar por ter mais de 60 anos trabalhando pelo menos 25')
else:
    print('Não pode se aposentar')

23)

ano = int(input("Digite um ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É ano bissexto')
else:
    print('Não é ano bissexto')

24)

valor = float(input('Qual o valor do produto? '))
estado = input('Qual o estado? ')

if estado == 'mg':
    novo_valor = valor + (valor * 7 / 100)
    print(f'O valor do produto para o estado de {estado.upper()} é {novo_valor}')
elif estado == 'sp':
    novo_valor = valor + (valor * 12 / 100)
    print(f'O valor do produto para o estado de {estado.upper()} é {novo_valor}')
elif estado == 'rj':
    novo_valor = valor + (valor * 15 / 100)
    print(f'O valor do produto para o estado de {estado.upper()} é {novo_valor}')
elif estado == 'ms':
    novo_valor = valor + (valor * 8 / 100)
    print(f'O valor do produto para o estado de {estado.upper()} é {novo_valor}')
else:
    print('Estado invalido')

25)

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

if a != 0:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não existe raiz real.")
    elif delta == 0:
        raiz = -b / (2*a)
        print("Raiz única:", raiz)
    else:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        print("Duas raízes reais:", raiz1, "e", raiz2)
else:
    print("Não é uma equação de segundo grau (a = 0).")

26)

dist = float(input('Qual é a distancia em km/h? '))
gasolina = float(input('Quanto de gasolina ? '))

gasto = dist / gasolina
print(gasto)

if gasto < 8:
    print('Venda o carro!')
elif gasto >= 8 and gasto < 12:
    print('Economico')
elif gasto > 12:
    print('Super economico')

27)

idade = int(input('Qual é a idade do nadador? '))

if idade >= 5 and idade <= 7:
    print('Infantil A')
elif idade >= 8 and idade <= 10:
    print('Infantil B')
elif idade >= 11 and idade <= 13:
    print('Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Juvenil B')
elif idade >= 18:
    print('Senior')

28)

import math

def media_geometrica(a, b, c):
    return math.pow(a * b * c, 1/3)

    
def media_ponderada(a, b, c):
    return (a + 2 * b + 3 * c) / 6


def media_harmonica(a, b, c):
    return 3 / (1/a + 1/b + 1/c)


def media_aritmetica(a, b, c):
    return (a + b + c) / 3


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

tipo_media = input("Escolha o tipo de média (geometrica, ponderada, harmonica, aritmetica): ")

if tipo_media == "geometrica":
    resultado = media_geometrica(a, b, c)
elif tipo_media == "ponderada":
    resultado = media_ponderada(a, b, c)
elif tipo_media == "harmonica":
    resultado = media_harmonica(a, b, c)
elif tipo_media == "aritmetica":
    resultado = media_aritmetica(a, b, c)
else:
    resultado = None

if resultado is not None:
    print(f"A média {tipo_media} dos números é:", resultado)
else:
    print("Tipo de média inválido. Escolha entre geometrica, ponderada, harmonica ou aritmetica.")

29)

from random import randint

count = 0
dicionario = dict()

for v in range(5):
    num = randint(1, 50)
    a = num
    num = randint(1, 50)
    b = num

    pergunta = int(input(f'Qual é a soma de {a} + {b}? '))

    if pergunta == a + b:
        print('Acertou!')
        count += 1
        dicionario[f'Qual é a soma de {a} + {b}?'] = a + b
    else:
        print('Voce errou!')

print('Respostas corretas:')
for chave in dicionario:
	print(f'{chave}: {dicionario[chave]}')
print(f'Você acertou {count} vezes!')

30)

num1 = float(input('Digite um numero'))
num2 = float(input('Digite um numero'))
num3 = float(input('Digite um numero'))

if num1 < num2 and num1 < num3:
    print(num1)
    if num2 < num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif num2 < num1 and num2 < num3:
    print(num2)
    if num1 < num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
elif num3 < num1 and num3 < num2:
    print(num3)
    if num1 < num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)

31)

altura = float(input('Digite sua altura '))
peso = float(input('Digite seu peso '))

if altura <= 1.20 and peso <= 60:
    print('Classificação A')
elif altura <= 1.20 and peso > 60 and peso <= 90:
    print('Classificação D')
elif altura <= 1.20 and peso > 90:
    print('Classificação G')

elif altura > 1.20 and altura <= 1.70 and peso <= 60:
    print('Classificação B')
elif altura > 1.20 and altura <= 1.70 and peso > 60 and peso <= 90:
    print('Classificação E')
elif altura > 1.20 and altura <= 1.70 and peso > 90:
    print('Classificação H')

elif altura > 1.70 and peso <= 60:
    print('Classificação C')
elif altura > 1.70 and peso > 60 and peso <= 90:
    print('Classificação F')
elif altura > 1.70 and peso > 90:
    print('Classificação I')

32)

codigo = int(input("Digite o código do produto que você deseja:
    Especificação      Código       Preço
    Cachorro Quente     100          1.20
    Bauru Simples       101          1.30
    Bauru com Ovo       102          1.50
    Hamburguer          103          1.20
    Cheeseburguer       104          1.70
    Suco                105          2.20
    Refrigerante        106          1.00"))

quantidade = int(input('Quantos desse produto você deseja? '))

if codigo == 100 or codigo == 103:
    print(f'O pedido custará {1.20 * quantidade}')
elif codigo == 101:
    print(f'O pedido custará {1.30 * quantidade}')
elif codigo == 102:
    print(f'O pedido custará {1.50 * quantidade}')
elif codigo == 104:
    print(f'O pedido custará {1.70 * quantidade}')
elif codigo == 105:
    print(f'O pedido custará {2.20 * quantidade}')
elif codigo == 106:
    print(f'O pedido custará {1.00 * quantidade}')

33)

valor = float(input('Qual é o preço antigo? '))

if valor < 50:
    novo_valor = valor + (valor * 5 / 100)
elif valor >= 50 and valor <= 100:
    novo_valor = valor + (valor * 10 / 100)
elif valor > 100:
    novo_valor = valor + (valor * 15 / 100)

if novo_valor < 80:
    print(f'Produto custa {novo_valor} e é barato')
elif novo_valor > 80 and novo_valor <= 120:
    print(f'Produto custa {novo_valor} e é normal')
elif novo_valor > 120 and novo_valor <= 200:
    print(f'Produto custa {novo_valor} e é caro')
elif novo_valor > 200:
    print(f'Produto custa {novo_valor} e é muito caro')

34)

nota = float(input('Qual é a nota do aluno? '))
faltas = int(input('E suas faltas? '))

if nota >= 9 and nota <= 10 and faltas <= 20:
    print('Conceito A')
elif nota >= 9 and nota <= 10 and faltas > 20:
    print('Conceito B')
elif nota >= 7.5 and nota <= 8.9 and faltas <= 20:
    print('Conceito B')
elif nota >= 7.5 and nota <= 8.9 and faltas > 20:
    print('Conceito C')
elif nota >= 5.0 and nota <= 7.4 and faltas <= 20:
    print('Conceito C')
elif nota >= 5.0 and nota <= 7.4 and faltas > 20:
    print('Conceito D')
elif nota >= 4.0 and nota <= 4.9 and faltas <= 20:
    print('Conceito D')
elif nota >= 4.0 and nota <= 4.9 and faltas > 20:
    print('Conceito E')
elif nota >= 0 and nota <= 3.9:
    print('Conceito E')

35)

import sys


def verifica_mes(data):
    mes_string = data[2] + data[3]
    mes_inteiro = int(mes_string)
    if mes_inteiro >= 1 and mes_inteiro <= 12:
        return mes_inteiro
    else:
        print('Mes inválido')
        sys.exit()


def verifica_ano(data):
    ano_string = data[4] + data[5]
    ano_int = int(ano_string)
    if ano_int % 4 == 0 and ano_int % 100 != 0 or ano_int % 400 == 0:
        print('É ano bissexto')
        ano_bissexto = True
        return ano_bissexto, ano_int
    else:
        print('Não é ano bissexto')
        ano_bissexto = False
        return ano_bissexto, ano_int


def verifica_dia(data, mes, ano):
    dia_string = data[0] + data[1]
    dia_int = int(dia_string)

    if dia_int > 31 or dia_int < 1:
        print('Data inválida')
        sys.exit()

    if mes == 2:
        if dia_int == 29 and ano[0] == True:
            print('A data é válida, por que o ano é bissexto!')
        elif dia_int == 29 and ano[0] == False:
            print('Data inválida')
            sys.exit()
        elif dia_int >= 30:
            print('Data inválida')
            sys.exit()
        else:
            print('A data é válida')

    elif mes in [4, 6, 9, 11]:
        if dia_int > 30:
            print('Data inválida')
            sys.exit()
        else:
            print('A data é válida')
    else:
        print('A data é válida')

data = input('Digite uma data: ')
mes = verifica_mes(data)
ano = verifica_ano(data)
verifica_dia(data, mes, ano)

36)

valor = float(input('Qual o valor da venda? '))

if valor < 20000:
    novo_valor = valor * 14 / 100
    print(f'A comissão que será paga será: 400 Reais + {novo_valor}, totalizando: {novo_valor + 400}')
elif valor < 40000 and valor >= 20000:
    novo_valor = valor * 14 / 100
    print(f'A comissão que será paga será: 500 Reais + {novo_valor}, totalizando: {novo_valor + 500}')
elif valor < 60000 and valor >= 40000:
    novo_valor = valor * 14 / 100
    print(f'A comissão que será paga será: 550 Reais + {novo_valor}, totalizando: {novo_valor + 550}')
elif valor < 80000 and valor >= 60000:
    novo_valor = valor * 14 / 100
    print(f'A comissão que será paga será: 600 Reais + {novo_valor}, totalizando: {novo_valor + 600}')
elif valor < 100000 and valor >= 80000:
    novo_valor = valor * 14 / 100
    print(f'A comissão que será paga será: 650 Reais + {novo_valor}, totalizando: {novo_valor + 650}')
elif valor > 100000:
    novo_valor = valor * 16 / 100
    print(f'A comissão que será paga será: 700 Reais + {novo_valor}, totalizando: {novo_valor + 700}')

37)

import datetime

hora_entrada = input('Qual o horário da entrada? ')
hora_saida = input('Qual o horário da saida? ')

if hora_entrada[0] != '0':
    h1, h2 = hora_entrada[0], hora_entrada[1]
    hora_que_entrou = int(h1 + h2)
    m1, m2 = hora_entrada[2], hora_entrada[3]
    minutos = int(m1 + m2)
else:
    h1 = hora_entrada[1]
    hora_que_entrou = int(h1)
    m1, m2 = hora_entrada[2], hora_entrada[3]
    minutos = int(m1 + m2)

hora1 = datetime.datetime(2023, 9, 23, hora_que_entrou, minutos)

if hora_saida[0] != '0':
    h1, h2 = hora_saida[0], hora_saida[1]
    hora_que_saiu = int(h1 + h2)
    m1, m2 = hora_saida[2], hora_saida[3]
    minutos = int(m1 + m2)
else:
    h1 = hora_saida[1]
    hora_que_saiu = int(h1)
    m1, m2 = hora_saida[2], hora_saida[3]
    minutos = int(m1 + m2)  

if hora_que_entrou < hora_que_saiu:
    hora2 = datetime.datetime(2023, 9, 23, hora_que_saiu, minutos)
else:
    hora2 = datetime.datetime(2023, 9, 24, hora_que_saiu, minutos)

diferenca = hora2 - hora1

aa = str(diferenca)
print(diferenca)
bb = aa.replace(':', '')
c = int(bb)
print(c)

if c <= 10000:
    print('Como pagou por 1 hora, será pago 1 real')
elif c > 10000 and c <= 20000:
    print('Como pagou por 2 horas, será pago 2 reais')
elif c > 20000 and c <= 40000:
    if c > 20000 and c <= 30000:
        hora = 1
        print(f'Como pagou por 3 horas, será pago {(hora * 1.40) + 2}')
    else:
        hora = 2
        print(f'Como pagou por 4 horas, será pago {(hora * 1.40) + 2}')
elif c > 40000:
    if c < 100000:
        string = str(c)
        hora_string = string[0]
        hora = int(hora_string)
        hora_cobrada = hora - 4
        print(f'Como pagou por {hora} horas, será pago {(hora_cobrada * 2) + 4.8}')
    else:
        string = str(c)
        hora_string = string[0:2]
        hora = int(hora_string)
        hora_cobrada = hora - 4
        print(f'Como pagou por {hora} horas, será pago {(hora_cobrada * 2) + 4.8}')

38)
        
"""


