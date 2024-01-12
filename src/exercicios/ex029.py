def funcao():
    vel = int(input('Digite a velocidade do carro: '))
    if vel > 80:
        multa = (vel - 80) * 7
        return f"""
MULTADO! Voce excedeu o limite permitido que é de 80Km/h
Voce deve pagar uma multa de R${multa}.00!
Tenha um bom dia! Dirija com segurança!
"""
    else:
        return 'Tenha um bom dia! Dirija com segurança!'
    

print(funcao())
