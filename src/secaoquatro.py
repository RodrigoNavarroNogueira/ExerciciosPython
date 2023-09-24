"""
Lista de exercicios do curso Programação em Python do básico ao avançado da Geek University.

Exercícios Python - Seção 04

1)

num = int(input('digite um número inteiro'))
print(num)

2)

num = float(input('digite um número inteiro'))
print(num)

3)

n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
n3 = int(input('Digite o terceiro número'))
print(n1 + n2 + n3)

4)

num = float(input('Digite um número real'))
quadrado = num ** 2
print(quadrado)

5)

num = float(input('Digite um numero real'))

quinta_parte = num / 5

print(f'A quinta parte do {num} é {quinta_parte}')

6)

cel = float(input('Digite a temperatura em Celsius'))
f = cel * (9 / 5) + 32

print(f'A temperatura convertida é {f}')

7 - leia a temperatura em fahrenheit e apresente-a convertida em graus celsius

f = float(input('Digite a temperatura em fahrenheit'))
c = 5 * (f - 32) / 9

print(f'A temperatura convertida é {c}')

8 - leia a temperatura em graus kelvin e apresente-a convertida em graus celsius

k = float(input('Digite a temperatura em kelvin'))
c = k - 273.15

print(f'A temperatura convertida é {c}')

9 - leia a temperatura em graus celsius e apresente-a convertida em graus kelvin

c = float(input('Digite a temperatura em celsius'))
k = c - 273.15

print(f'A temperatura convertida é {k}')

10 - leia uma velocidade em km/h e apresente-a convertida em m/s

k = float(input('Digite a velocidade em km/h'))
m = k / 3.6

print(f'A velocidade convertida é {m}')

11 - leia uma velocidade em m/s e apresente-a convertida em km/h

m = float(input('Digite a velocidade em m/s'))
k = m * 3.6

print(f'A velocidade convertida é {k}')

12 - leia uma distancia em milhas e apresente-a convertida em km

m = float(input('Digite a velocidade em milhas'))
k = 1.61 * m

print(f'A velocidade convertida é {k}')

13 - leia uma distancia em km e apresente-a convertida em milhas

k = float(input('Digite a velocidade em km'))
m = k * 0.621371

print(f'A velocidade convertida é {m}')

14 - leia um ângulo em graus e apresente-o convertido em radianos

g = float(input('Digite um angulo em graus'))
r = g * 3.14 / 180

print(f'O angulo convertido é {r}')

15 - leia um ângulo em radianos e apresente-o convertido em graus

r = float(input('Digite um angulo em radianos'))
g = r * 180 / 3.14

print(f'O angulo convertido é {g}')

16 - leia um valor de comprimento em polegadas e apresente-o convertido em centímetros

p = float(input('Digite o comprimento em polegadas'))
c = p * 2.54

print(f'O comprimento convertido é {c}')

17 - leia um valor de comprimento em centímetros e apresente-o convertido em polegadas

c = float(input('Digite o comprimento em centimetros'))
p = c / 2.54

print(f'O comprimento convertido é {p}')

18 - leia um valor de volume em metros cubicos m3 e apresente-o convertido em litros

m = float(input('Digite o valor de volume em metros cubicos'))
l = m * 1000

print(f'O valor de volume convertido é {l}')

19 - leia um valor de volume em litros e apresente-o convertido em metros cubicos m3

l = float(input('Digite o valor de volume em litros'))
m = l / 1000

print(f'O valor de volume convertido é {m}')

20 - leia um valor de massa em quilogramas e apresente-o convertido em libras

k = float(input('Digite o valor de massa em quilogramas'))
l = k * 2.20462

print(f'O valor de volume convertido é {l}')

21 - leia um valor de massa em libras e apresente-o convertido em quilogramas

l = float(input('Digite o valor de massa em libras'))
k = l * 0.453592

print(f'O valor de volume convertido é {k}')

22 - leia um valor de comprimento em jardas e apresente-o convertido em metros

j = float(input('Digite o valor de comprimento em jardas'))
m = 0.91 * j

print(f'O valor do comprimento convertido é {m}')

23 - leia um valor de comprimento em metros e apresente-o convertido em jardas

m = float(input('Digite o valor de comprimento em metros'))
j = m / 0.91

print(f'O valor do comprimento convertido é {j}')

24 - leia um valor de área em metros quadrados m2 e apresente-o convertido em acres

m = float(input('Digite o valor da area em metros quadrados'))
a = m * 0.000247

print(f'O valor da area convertida é {a}')

25 - leia um valor de área em acres e apresente-o convertido em metros quadrados m2

a = float(input('Digite o valor da area em acres'))
m = a * 4048.58

print(f'O valor da area convertida é {m}')

26 - leia um valor de area em metros quadrados m2 e apresente-o convertido em hectares

m = float(input('Digite o valor da area em metros quadrados'))
h = m * 0.0001

print(f'O valor da area convertida é {h}')

27 - leia um valor de area em hectares e apresente-o convertido em metros quadrados

h = float(input('Digite o valor da area em hectares'))
m = h * 10000

print(f'O valor da area convertida é {m}')

28 - faça a leitura de tres valores e apresente como resultado a soma dos quadrados dos tres valores lidos

n1 = float(input('Digite um valor'))
n2 = float(input('Digite um valor'))
n3 = float(input('Digite um valor'))

lista = [n1, n2, n3]

soma = 0
for num in lista:
    soma += num ** 2
    
print(f'O valor da soma dos quadrados dos valores é {soma}')

29 - leia quatro notas, calcule a media aritmetica e imprima o resultado

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
n4 = float(input('Digite a quarta nota:'))

media = (n1 + n2 + n3 + n4) / 4

print(f'A media das notas é {media}')

30 - leia um valor em real e a cotação do dolar. Em seguida, imprima o valor correspondente em dolares

reais = float(input('Digite a quantidade em reais:'))
dolar = reais / 4.92
print(f'{reais} reais equivalem a {dolar} dolares')

31 - leia um numero inteiro e imprima o seu antecessor e o seu sucessor

num = int(input('Digite um numero:'))
print(f'O antecessor de {num} é {num - 1} e o sucessor é {num + 1}')

32 - leia um numero inteiro e imprima a soma do seu sucessor de seu triplo com o antecessor de seu dobro

num = int(input('Digite um numero:'))
sucessor = (num * 3) + 1
antecessor = (num * 2) - 1
soma = sucessor + antecessor
print(f'A soma é {soma}')

33 - leia o tamanho do lado de um quadrado e imprima como resultado a sua area

lado = float(input(f'Qual o tamanho do lado do quadrado?'))
area = lado * lado
print(f'A área é {area}')

34 - leia o valor do raio de um circulo e calcule e imprima a area do circulo correspondente

r = float(input('Qual o valor do raio?'))
a = 3.14 * (r ** 2)
print(f'A area é {a}')

35 - sejam a e b is catetos de um triangulo, faça um programa que receba os valores e calcule o valor da hipotenusa

import math
c1 = float(input('Digite o primeiro cateto:'))
c2 = float(input('Digite o segundo cateto:'))

h = math.sqrt(c1 ** 2 + c2 ** 2)
print(f'A hipotenusa é {h}')

36 - leia a altura e o raio de um cilindro circular e imprima o volume do cilindro

r = float(input('Digite o raio:'))
a = float(input('Digite a altura:'))

v = math.pi * (r ** 2) * a
print(f'O volume do cilindro é {v}')

37 - faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%

produto = float(input(f'Qual o valor do produto?'))
desconto = produto - (produto * 12 / 100)
print(f'O valor do produto com desconto é {desconto}')

38 - leia o salario de um funcionario, calcule e imprima o valor do novo salario, sabendo que ele recebeu um aumento de 25%

salario = float(input('Qual é o salario?'))
novo = salario + (salario * 25 / 100)
print(f'O novo salario será de {novo}')

39 - a importancia de r$ 780.000,00 será dividida entre tres ganhadores de um concurso, o primeiro ganhador receberá 46%,
o segundo receberá 32, e o terceiro receberá o restante

premio = 780000
primeiro = premio * 45 / 100
segundo = premio * 32 / 100
terceiro = premio * 23 / 100
soma = primeiro + segundo + terceiro
print(f'O primeiro receberá {primeiro}, o segundo receberá {segundo} e o terceiro {terceiro}, totalizando os {soma}')

40 - uma empresa contrata um encanador a 30 reias por dia, faça um programa que solicite o numero de dias trabalhados pelo encanador e imprima
a quantia liquida que deve ser paga, sabendo-se que são descontados 8% para imposto de renda.

dias = int(input('Quantos dias trabalhos?'))
valor = 30
final = valor * dias
desconto = final - (final * 8 / 100)
print(desconto)

41 - faça um programa que leia o valor da hora de trabalho em reais e numero de horas trabalhadas no mes.
imprima o valor a ser pago ao funcionario, adicionando 10% sobre o valor calculado

valor = float(input('Qual o valor que ganha por hora?'))
horas = float(input('Quantas horas trabalhou?'))
total = valor * horas
final = total + (total * 10 / 100)
print(f'O funcionario ira receber {final}')

42 - receba o salario base de um funcionario. calcule e imprima o salario a receber, sabendo que esse
funcionario tem uma gratificação de 5% sobre o salario-base. além disso, ele paga 7% de imposto sobre a base 

salario = float(input('Qual o salario?'))
grat = salario * 5 / 100
imposto = salario * 7 / 100
final = salario + grat - imposto
print(f'O salário será de {final}')

43 - escreva um programa de ajuda para vendedores. a partir de um valor total lido, mostre:
o total a pagar com desconto de 10%
o valor de cada parcela, no parcelamento de 3x sem juros
a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

total = float(input('Qual é o valor do produto? '))
desconto = total - (total * 10 / 100)
parcela = total / 3
com_vista = desconto * 5 / 100
com_parcela = total * 5 / 100
print(f'Total a pagar com desconto: {desconto}')
print(f'Se parcelar em 3x, cada parcela será de {parcela}')
print(f'Comissão se for a vista {com_vista}')
print(f'Comissão se for parcelado {com_parcela}')

44 - receba a altura de um degrau de uma escada e a altura que o usuario deseja alcançar subindo a escada.
calcule e mostre quantos degraus o usuario deverá subir para atingir seu objetivo

degrau = float(input('Qual a altura do degrau?'))
altura = float(input('Qual altura deseja alcançar?'))
f = altura / degrau
print(f'Será necessário subir {f} degraus')

45 - faça um programa para converter uma letra maiuscula em letra minuscula. use a tabela ascii para resolver
o problema

a = input('Digite algo')
print(f'Convertendo para minusculo: {a.lower()}')

46 - faça um programa que leia um numero inteiro positivo de tres digitos (de 100 á 999). gere um outro numero
formado pelos digitos invertidos do numero lido.

n = int(input('Digite um numero'))
if n < 100 or n > 999:
    print('O numero precisa ser de 100 á 999')
else:
    s = str(n)
    if len(s) < 3:
        print('Precisa digitar 3 numeros')
    else:
        string = s[::-1]
        n = int(string)
        print(f'Os numeros invertidos: {n}')

47 - leia um numero inteiro de 4 digitos (de 1000 a 9999) e imprima 1 digito por linha

n = int(input('Digite um numero'))
if n < 1000 or n > 9999:
    print('O numero precisa ser de 1000 á 9999')
else:
    s = str(n)
    lista = list(s)
    for numero in lista:
        print(numero)

48 - leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

seg = int(input('Quantos segundos?'))
horas = seg / 3600
min = seg / 60
print(f'Horas: {horas}\nMinutos: {min}\nSegundos: {seg}')

49 - faça um programa para ler o horario(hora, minuto, segundo) de inicio e a duração, em segundos, de uma
experiencia biologica o programa deve resultar com o novo horario (hora, minuto, segundo) do termino da mesma

import datetime

comeca = input('Que horas vai começar?')
seg = int(input('Quantos segundos de duração?'))
h1, h2 = comeca[0], comeca[1]
hora = int(h1 + h2)
m1, m2 = comeca[2], comeca[3]
minutos = int(m1 + m2)
s1, s2 = comeca[4], comeca[5]
segundos = int(s1 + s2)
hora = datetime.datetime(2023, 9, 23, hora, minutos, segundos)
hora_nova = hora + datetime.timedelta(seconds=seg)
breakpoint()
print(f'Como o programa se iniciou em {hora}, então ele se encerra em {hora_nova}')

50 - implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual

idade = int(input('Qual a sua idade?'))
ano = int(input('Em que ano estamos?'))
nascimento = ano - idade
print(f'Sua data de nascimento é {ano - idade}!')

51 - escreva um programa que leia as coordenadas x e y de pontos no r2 e calcule sua distancia da origem (0,0)

import math

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))
distancia = math.sqrt(x ** 2 + y ** 2)
print(f'A distância é:{distancia}')

52 - tres amigos jogaram na loteria, caso eles ganhem, o premio deve ser repartido proporcionalmente ao valor
que cada deu para a realização da aposta. faça um programa que leia 

amigo1 = float(input('Quanto o primeiro amigo apostou? '))
amigo2 = float(input('Quanto o segundo amigo apostou? '))
amigo3 = float(input('Quanto o terceiro amigo apostou? '))
premio = int(input('Qual o valor do premio? '))
aposta = amigo1 + amigo2 + amigo3  # Somando o valor das apostas
lucro1 = (amigo1 / aposta) * 100   # Porcentagem do primeiro amigo, referente ao valor da aposta 
lucro2 = (amigo2 / aposta) * 100   # Porcentagem do segundo amigo, referente ao valor da aposta 
lucro3 = (amigo3 / aposta) * 100
print(lucro1, lucro2, lucro3)
premio1 = (lucro1 / 100) * premio  # Valor do premio do primeiro amigo
premio2 = (lucro2 / 100) * premio  # Valor do segundo do primeiro amigo
premio3 = (lucro3 / 100) * premio
print(f'O primeiro amigo vai lucrar {premio1} que corresponde a {lucro1}% do premio')
print(f'O segundo amigo vai lucrar {premio2} que corresponde a {lucro2}% do premio')
print(f'O terceiro amigo vai lucrar {premio3} que corresponde a {lucro3}% do premio')

53) faça um programa para ler as dimensoes de um terreno, bem como o preço do metro da tela, imprima o custo 
para cercar o terreno com a tela

comprimento = float(input('Comprimento do terreno: '))
largura = float(input('Largura do terreno: '))
cerca = int(input('Qual o valor do metro? '))
area = comprimento * largura
print(f'Irá custar {cerca * area} pois o terreno tem uma area de {area}')
"""
