def funcao():
    peso = float(input('Qual o seu peso? (Kg) '))
    altura = float(input('Qual a sua altura? (M) '))
    imc = peso / (altura ** 2)
    print(f'O IMC dessa pessoa é {imc:.1f}')
    
    if imc < 18.5:
        return 'Voce está abaixo do peso'
    elif imc >= 18.5 and imc <= 25:
        return 'Voce está com o peso ideal'
    elif imc > 25 and imc <= 30:
        return 'Voce está com sobrepeso'
    elif imc > 30 and imc <= 40:
        return 'Voce está com obesidade'
    elif imc > 40:
        return 'Voce está com obesidade morbida!'
    

print(funcao())
