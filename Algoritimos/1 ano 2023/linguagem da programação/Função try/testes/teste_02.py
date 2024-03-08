try:
    def divisao(a, b):
        resultado = a / b
        return resultado
    print(divisao(10, 2))
    print(divisao(10, '2'))
except:
    print('Divisão impossivel de ser realizada.')