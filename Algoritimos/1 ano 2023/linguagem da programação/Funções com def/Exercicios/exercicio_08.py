def inverso(num):
    lista_d_n=[str(i) for i in range (10)]

    for i in num:
            if lista_d_n.count(i) == 0: return"válor inválido"        
    return f'{num} -> {num[::-1]}'
print(inverso(input('Digite o número a ser invertido: ')))