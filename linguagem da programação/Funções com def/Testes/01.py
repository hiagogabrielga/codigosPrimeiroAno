def alguma(algo):
    try:
        algo = int(algo)
    except:
        return 'Ta algo errado'

    if algo == 8:
        return 'Errado'
    else:
        return 'Termina'
    
print(alguma(input('Digite algo: ')))