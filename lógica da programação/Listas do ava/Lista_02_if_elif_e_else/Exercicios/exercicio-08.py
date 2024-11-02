pre=float(input('Digite o valor a pagar: '))
print('Temos 4 formas de pagamento, são elas as seguintes\
    \na. Pagamento à vista: conceder desconto de 5%.\
    \nb. Pagamento em 3 parcelas: o valor não sofre alteração.\
    \nc. Pagamento em 5 parcelas: acréscimo de 2%.\
    \nd. Pagamento em 10 parcelas: acréscimo de 8%')
form_d_p=input('Digite a forma desejada de pagamento atraves dos carateres a, b, c ou d: ')
if form_d_p == 'a':
    print(f'O valor a ser pago recebeu o desconto de 5%\nO valor a pagar agora é de R$ {pre-(pre*5/100):.2f}')
elif form_d_p == 'b':
    print(f'O valor valor não sofreu alteração\nValor a pagar é de R$ {pre:.2f}')
elif form_d_p == 'c':
    print(F'O valor a ser pago recebeu o acréscimo de 2%\nO valor a pagar agora é de R$ {(pre*2/100)+pre:.2f}')
elif form_d_p == 'd':
    print(f'O valor a ser pago recebeu o acréscimo de 8%\nO valor a pagar aogra é de R$ {(pre*8/100)+pre}')
else:
    print('Por favor analise se digitou o caractere corretamente.')

