op='Opções de uso:\
\n(1) Consultar saldo\
    \n(2) Efetuar saque\
    \n(3) Efetuar depósito\
    \n(4) sair.'
print(op)
per=int(input('Qual opção você deseja executar? '))
saldo=1000.00
while True:
    if per == 1:
        print(f'Seu saldo é de R$ {saldo:.2f}')
        print(op)
        per=int(input('Qual opção você deseja executar? '))
    elif per == 2:
        per2=float(input('Digite quanto você deseja retirar: '))
        while per2 > saldo:
            print('você não tem saldo o suficiente.')
            print(op)
            per2=float(input('Digite quanto você deseja retirar: '))
        saldo-=per2
        print(f'Operção realizada com sucesso.')
        print(op)
        per=int(input('Qual opção você deseja executar agora? '))
    elif per == 3:
        per3=float(input('Quanto você deseja depositar? '))
        saldo+=per3
        print(op)
        per=int(input('Qual opção você deseja executar agora? '))
        print(f'Operção realizada com sucesso.')
    elif per == 4:
        print('Fim de programa')
        break
    else:
        print('Operção inezistente. Tente novamente')
        print(op)
        per=int(input('Qual opção você deseja executar? '))