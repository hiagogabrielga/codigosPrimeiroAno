def contador_d_carc(num):
    lista_d_n=[str(idade) for idade in range (10)]

    for i in num:
            if lista_d_n.count(i) == 0: return"número inválido"
    

    return f'O  número {num} contém {len(num)} caractéres.'
print(contador_d_carc(input('Digite um número: ')))