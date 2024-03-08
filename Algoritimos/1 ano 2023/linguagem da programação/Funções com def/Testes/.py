valor=input('Digite o valor:')
lista_d_n=[str(i) for i in (valor)]
if lista_d_n.count(',') == 1:
    inteiro='00'
    cents='00'
    inteiro=valor.split(',')[0]
    cents=valor.split(',')[1]
    valor=(f'{inteiro}.{cents}')
    valor=float(valor)
print(valor-98)