def funcao():
    num1 = int(input('Primeiro valor: '))
    num2 = int(input('Segundo valor: '))
    num3 = int(input('Terceiro valor: '))
    return num1,num2,num3


def menores(n):
    if n[0] < n[1] and n[0] < n[2]:
        menor = n[0]
    elif n[1] < n[2] and n[1] < n[0]:
        menor = n[1]
    elif n[2] < n[0] and n[2] < n[1]:
        menor = n[2]
    return menor


def maiores(n, menor):
    if n[0] > n[1] and n[0] > n[2]:
        maior = n[0]
    elif n[1] > n[2] and n[1] > n[0]:
        maior = n[1]
    elif n[2] > n[0] and n[2] > n[1]:
        maior = n[2]
    return f"""
O menor valor digitado foi {menor}
O maior valor digitado foi {maior}
"""


n = funcao()
menor = menores(n)
print(maiores(n, menor))
