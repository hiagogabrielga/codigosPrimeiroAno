cap=input('Digite o nome dá capital do Brasil? ')
while cap != 'Brasília':
    if cap == 'brasília':
        print('Você errou pois não colocou a primeira letra maiúscula.')
    elif cap == 'Brasilia':
        print('Você errou pois não colocou o "´" no i na sílaba si.')
    elif cap == 'brasilia':
        print('Você errou pois não colocou o "´" no i na sílaba si e não colocou a primeira letra maiúscula.')
    else:
        print('Resposta errada')
    cap=input('Digite o nome dá capital do Brasil novamente: ')
print(f'Você acertou. a capital do Brasil é {cap}')