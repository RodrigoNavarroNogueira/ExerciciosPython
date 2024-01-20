def funcao():
    n = int(input('Digite um numero: '))
    o = int(input("""
(1) Converter para binario
(2) Converter para octal
(3) Converter para hexadecimal
"""))
    if o == 1:
        return f'{n} convertido para binario é igual a {bin(n)[2:]}'
    elif o == 2:
        return f'{n} convertido para octal é igual a {oct(n)[2:]}'
    elif o == 3:
        return f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}'


print(funcao())
