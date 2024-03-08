def alguma(algo):
    lista_d_n=[str(teste) for teste in range (10)]
    
    for i in algo:
        if lista_d_n.count(i) == 0: 
            return 'Algo errado'
    algo = float(algo)

    if algo > 0:
        return 'P'
    elif algo == 0:
        return 'Z'
    else:
        return 'N'
    
print(alguma(input('Digite algo: ')))