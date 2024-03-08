import random

def exercicio_01():
    lista=[]
    for i in range(1,7):
        elemento=int(input(f'Digite seu {i}° número: '))
        lista.append(elemento)
    print(lista)


def exercicio_02():
    lista=[]
    for i in range(1,11):
        elemento=float(input(f'Digite seu {i}° número: '))
        lista.append(elemento)
    lista=sorted(lista)
    maior=lista[9]
    menor=lista[0]
    print(f'O maior número digitado foi de {maior} e o menor foi de {menor}')


def exercicio_03():
    lista=['uva','pessego','abacate','morango','tomate','abacate','abacaxi','abacate','pera','banana','cereja','cacau','pessego','banana','cereja']
    per=input('Digite o nome da sua fruta: ').lower()
    print(f'A fruta {per} aparece {lista.count(per)} vezes.')


def exercicio_04():
    lista=['João','Pedro','Bento','Andrade','Wagner','Ana']
    random.shuffle(lista)
    print(lista)
    lista.sort(reverse = True)
    print(lista)


def exercicio_05():
    soma=0
    lista=[]
    for i in range(1,11):
        nota=float(input(f'Digite a {i}° nota da turma: '))
        lista.append(nota)
        soma=soma+nota
    lista.sort(reverse=True)
    print(f'A lista de notss da turma é de\n{lista}\nA média da turma é de {soma/len(lista)}')


def exercicio_06():
    lista=[]
    for i in range(1,9):
        valor=int(input(f'Digite o seu {i}° valor: '))
        lista.append(valor)
    while True:
        try:
            x=int(input('Digite seu valor X: '))
            print(f'O elemento do valor X é de {lista[x]}')
            y=int(input('Digite seu valor Y: '))
            print(f'O elemento do valor Y é de {lista[y]}')

        except IndexError:
            print('Você digitou um indice que não existe.')

        else:
            print(f'A soma desses dois valors são de {lista[y]+lista[x]}')


def exercicio_07():
    lista=[]
    for i in range(1,11):
        nome=input(f'Digite o {i}º nome: ')
        lista.append(nome.lower())
    nome=input('Digite um nome: ')
    if nome.lower() in lista:
        print('ACHEI')
    else:
        print('NÃO ACHEI.')


def exercicio_08():
    lista=[]
    soma=0
    for i in range (1,8):
        while True:
            dia=input(f'Digite a temperatuda do {i}° dia: ')
            try:
                dia=float(dia)
                lista.append(dia)
                soma=soma+dia
                break
            except:
                print('Ops, você colocou algo errado, tente colocar a temperatura novamente.')
    media=soma/7
    lista_d_t_m=[]
    for d in range(7):
        if lista[d] > media:
            lista_d_t_m.append(d+1)
            lista_d_t_m.append('º')
    lista_d_t_m=str(lista_d_t_m).replace(', ','')
    lista_d_t_m=str(lista_d_t_m).replace("'º'",'º ')
    lista_d_t_m=str(lista_d_t_m).replace("[",'')
    lista_d_t_m=str(lista_d_t_m).replace("]",'')
    print(f'A média é de {media:.2f}\nO {lista_d_t_m}dia tiveram a temperatura a cima da média.')


def exercicio_09():
    lista=[]
    numero=random.randint(0,100)
    lista.append(numero)
    for i in range(19):
        numero=random.randint(0,100)
        while True:
            if numero not in lista:
                lista.append(numero)
                break
            else:
                numero=random.randint(0,100)           
    per=int(input('Digite um número entre 0 e 100: '))
    print(lista)
    if per in lista:
        print('Você ganhou!')
    else:
        print('Não foi dessa vez !')


def exercicio_10():
    per=int(input('Qual número você deseja fazer a tabuada? '))
    lista=[per*i for i in range (1,11)]
    print(lista)



while True:
    linha='='*77
    per=input(f'\n{linha}\
        \n| (1)Mostrar os valores digitados.                                          |\
        \n| (2)Mostrar o maior e o menor número digitado.                             |\
        \n| (3)Mostrar quantas vezes a fruta digitado tem na lista.                   |\
        \n| (4)Mostrar a lista de nome em ordem alfabética reversa.                   |\
        \n| (5)Mostrar a média da turma.                                              |\
        \n| (6)Mostrar a soma dos valores encontrados nas respectivas posições X e Y. |\
        \n| (7)Mostrar se o nome digitado está na lista de nomes.                     |\
        \n| (8)Calcular a média das temperaturas digitadas.                           |\
        \n| (9)Brincar de Bingo.                                                      |\
        \n| (10)Mostar a tabuada do número digitado.                                  |\
        \n{linha}\
        \nQual função Você desejar realizar\nR:')
    if per == '1':exercicio_01()

    elif per == '2':exercicio_02()

    elif per == '3':exercicio_03()

    elif per == '4':exercicio_04()

    elif per == '5':exercicio_05()

    elif per == '6':exercicio_06()

    elif per == '7':exercicio_07()

    elif per == '8':exercicio_08()

    elif per == '9':exercicio_09()

    elif per == '10':exercicio_10()

    elif per == '11':
        print('Professor adiciona um pontinho a mais só por causa dessa parte do menu, por favor')
        break 
    

    else:
        print('Ops, Essa função não existe.')
