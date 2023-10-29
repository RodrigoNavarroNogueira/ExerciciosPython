"""
1)

matriz = [[], [], [], []]
total = 0

for vez in range(4):
    for n in range(4):
        numero = int(input('Digite um numero positivo: '))
        matriz[vez].append(numero)
    
for m in matriz:
    print(matriz)
    
for m in range(4):
    for num in matriz[m]:
        if num > 10:
            total += 1
            
print(f'Na matriz, existem {total} numeros maiores que 10')

2)



"""