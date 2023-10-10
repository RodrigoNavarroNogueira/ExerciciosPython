def contador_divisor(num):
    divisores = 0
    for n in range(1, num + 1):
        if num % n == 0:
            divisores += 1
    return divisores

num = int(input("Digite um número inteiro: "))
divisores = contador_divisor(num)
print(f'Possui {divisores} divisores')
