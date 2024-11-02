def obs_num(num):
    lista_d_n=[str(idade) for idade in range (10)]

    for i in num:
            if lista_d_n.count(i) == 0: return "Número Inválido"
    if num > 0: return"Seu número é posito 'P'"
    elif num == 0: return"Seu número é zero 'Z' "
    else: return"Seu número é negátivo 'N'"
print(obs_num(float(input('Digite um número: '))))