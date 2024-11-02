# Define as opções disponíveis para o usuário
op = 'Opções de uso:\
\n(1) Consultar saldo\
\n(2) Efetuar saque\
\n(3) Efetuar depósito\
\n(4) Sair.'

# Inicializa o saldo
saldo = 1000.00

# Exibe as opções para o usuário
print(op)

# Solicita ao usuário que escolha uma opção
per = int(input('Qual opção você deseja executar? '))

# Loop principal do programa
while True:
    if per == 1:
        # Exibe o saldo atual
        print(f'Seu saldo é de R$ {saldo:.2f}')
        
        # Exibe as opções novamente e solicita uma nova escolha
        print(op)
        per = int(input('Qual opção você deseja executar? '))
    
    elif per == 2:
        # Solicita o valor a ser retirado
        per2 = float(input('Digite quanto você deseja retirar: '))
        
        # Verifica se o valor solicitado é maior que o saldo disponível
        while per2 > saldo:
            print('Você não tem saldo suficiente.')
            # Exibe as opções novamente e solicita um novo valor
            print(op)
            per2 = float(input('Digite quanto você deseja retirar: '))
        
        # Atualiza o saldo após o saque
        saldo -= per2
        print('Operação realizada com sucesso.')
        
        # Exibe as opções novamente e solicita uma nova escolha
        print(op)
        per = int(input('Qual opção você deseja executar agora? '))
    
    elif per == 3:
        # Solicita o valor a ser depositado
        per3 = float(input('Quanto você deseja depositar? '))
        
        # Atualiza o saldo após o depósito
        saldo += per3
        print('Operação realizada com sucesso.')
        
        # Exibe as opções novamente e solicita uma nova escolha
        print(op)
        per = int(input('Qual opção você deseja executar agora? '))
    
    elif per == 4:
        # Exibe mensagem de fim de programa e encerra o loop
        print('Fim de programa')
        break
    
    else:
        # Caso a opção escolhida seja inválida
        print('Opção inexistente. Tente novamente.')
        
        # Exibe as opções novamente e solicita uma nova escolha
        print(op)
        per = int(input('Qual opção você deseja executar? '))
