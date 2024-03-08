def contador(nome):
    list_nome=nome.split()[0]
    ver=list_nome.isalpha()
    if ver == True:
        return f'{list_nome} é contido apenas por letras'
    else:
        return'Erro'
print(contador(nome=input('Digite seu nome: ')))
