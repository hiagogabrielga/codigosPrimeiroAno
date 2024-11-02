def contar_n_positivos(*numeros):
    cont = 0
    for n in numeros:
        if n > 0:
            cont+=1
    return f'total de números positivos {cont}'
print(contar_n_positivos(1,2,3,4,5,6))