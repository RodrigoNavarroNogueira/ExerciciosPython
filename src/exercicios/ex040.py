def funcao():
    notaum = float(input('Primeira nota: '))
    notadois = float(input('Segunda nota: '))
    media = (notaum + notadois) / 2
    print(f'Tirando {notaum} e {notadois} a média do aluno é {media}')
    if media < 5:
        return 'Reprovado!'
    elif media >= 5 and media < 7:
        return 'Recuperação!'
    elif media > 7:
        return 'Aprovado!'
    

print(funcao())
