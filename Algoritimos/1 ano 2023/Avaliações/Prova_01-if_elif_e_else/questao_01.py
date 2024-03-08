print('Código 1 é um Cachorro Quente que custa R$ 8.00\
    \nCódigo 2 é um X-Salada que custa R$ 9.00\
    \nCódigo 3 é um X-Bacon que custa R$ 10.00\
    \nCódigo 4 é uma Torrada Simples que custa R$ 4.00\
    \nCódigo 5 é um Refrigerante que custa R$ 3.50')
cod=int(input('Digite o código do alimento: '))
if cod>=1 and cod<=5:
    quant=int(input('Digite a quantidade de alimento consumido: '))
    lanche1='Cachorro Quente'
    pre_l1=8.00
    lanche2='X-Salada'
    pre_l2=9.00
    lanche3='X-Bacon'
    pre_l3=10.00
    lanche4='Torrada Simples'
    pre_l4=4.00
    lanche5='Refrigerante'
    pre_l5=3.50
    if cod==1:
        print(f'O preço do {lanche1} é R${pre_l1:.2f}\nO preço a pagar é de R${quant*pre_l1:.2f}')
    if cod==2:
        print(f'O preço do {lanche2} é R${pre_l2:.2f}\nO preço a pagar é de R${quant*pre_l2:.2f}')
    if cod==3:
        print(f'O preço do {lanche3} é R${pre_l3:.2f}\nO preço a pagar é de R${quant*pre_l3:.2f}')
    if cod==4:
        print(f'O preço do {lanche4} é R${pre_l4:.2f}\nO preço a pagar é de R${quant*pre_l4:.2f}')
    if cod==5:
        print(f'O preço do {lanche5} é R${pre_l5:.2f}\nO preço a pagar é de R${quant*pre_l5:.2f}')
else:
    print('Código Inválido.')
