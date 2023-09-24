"""
Lista de exercicios do curso Programação em Python do básico ao avançado.


1 - Faça um programa que leia um número inteiro e o imprima.

num = int(input('digite um número inteiro'))
print(num)

2 - Faça um programa que leia um número real e o imprima.

num = float(input('digite um número inteiro'))
print(num)

3 - Peça ao usuario para digitar tres valores inteiros e imprima a soma deles.

n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
n3 = int(input('Digite o terceiro número'))
print(n1 + n2 + n3)

4 - Leia um numero real e imprima o resultado do quadrado desse numero.

num = float(input('Digite um número real'))
quadrado = num ** 2
print(quadrado)

5 - leia um numero real e imprima a quinta parte desse numero

num = float(input('Digite um numero real'))

quinta_parte = num / 5

print(f'A quinta parte do {num} é {quinta_parte}')

6 - leia a temperatura em graus celsius e apresente-a convertida em graus fahrenheit

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

41 - 

"""

