def contar_pares(*numeros):
    cont = 0
    for n in numeros:
        if n %2 == 0:
            cont+=1
    return f'total de pares {cont}'
print(contar_pares(1,2,3,4,5,6))
