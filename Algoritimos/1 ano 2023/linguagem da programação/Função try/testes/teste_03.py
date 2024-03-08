def main():
    print('Inicio do main')
    funcao_01()
    print('Fim do main')

def funcao_01():
    print('inicio da função 01')
    funcao_02()
    print('Fim da função 01')

def funcao_02():
    print('Inicio da funçaõ 02')
    lista = range(10)
    for i in range(11):
        try:
            print(lista[i])
        except IndexError:
            print(f'O indice {i} esta indiponivel')
    print('Fim da função 02')

main()