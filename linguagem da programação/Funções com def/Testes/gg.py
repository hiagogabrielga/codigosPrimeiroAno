def idades(idade):
    b = []
    b.extend(idade)
    c = ['1','2','3','4','5','6','7','8','9','0']
    num = False
    for i in b:
        for n in c:
            if n == i: num = True

        if num == False: return "Número inválido"
        else:  num = False

    idade = int(idade)

    if idade > 17: return "Maior de idade"
    else: return "Menor de idade" 

print(idades(input))