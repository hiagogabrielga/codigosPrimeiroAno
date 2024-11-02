uni=int(input('Digite a quantidade de caquis: '))
if uni < 12:
    print(f'o preço a pagar sera de R$ {uni*3.00:.2f}')
elif uni >= 12:
    print(f'O preço a pagarsera de R$ {uni*2.50:.2f}')