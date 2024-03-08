from cliente import Cliente
from agencia import Agencia
from conta_corrente import ContaCorrente
from conta_poupanca import Conta_poupanca
clientes=[]
contas=[]
i='='*30

def criar_clientes():
    clientes.append (Cliente('João Pedro', '915.650.322-10', '(69) 96623-1195', 'Vilhena'))
    clientes.append (Cliente('Lucas', '325.870.652-14', '(10) 17352-1455', 'Vilhena'))
    clientes.append (Cliente('Rovilson', '534.160.128-61', '(69) 96325-4493', 'Vilhena'))
    clientes.append (Cliente('Judas', '915.090.172-10', '(69) 94623-0985', 'Vilhena'))
    clientes.append (Cliente('Zacarias', '325.090.652-84', '(10) 17352-7646', 'Vilhena'))

def print_clientes():
    for cli in clientes:
        print(f'\n{i}\nNome: {cli.nome}\nCPF: {cli.cpf}\n{i}\n')

def criar_contas():
    agencia = Agencia('1123')
    contas.append (ContaCorrente(clientes[0],agencia))
    contas.append (ContaCorrente(clientes[1],agencia,300))
    contas.append (ContaCorrente(clientes[2],agencia,210, 500.00))
    contas.append (Conta_poupanca(clientes[3],agencia))
    contas.append (Conta_poupanca(clientes[4],agencia,500))

def print_contas():
    for conta in contas:
        print(f'\n{i}\nNome do Cliente: {conta.cliente.nome}\nBanco: {conta.agencia.banco.nome}\nAgencia: {conta.agencia.numero}\nNúmero da conta {conta.numero}\nSaldo: {conta.saldo:.2f}\n{i}\n')

def encontrar_conta():
    while True:
        print_contas()
        numero = int(input('Digite o número de conta: '))
        for conta in contas:
            if conta.numero == numero:
                return conta
        print('Conta não encontrada!')

def main():
    criar_clientes()
    criar_contas()
    conta=encontrar_conta()
    while True:
        
        per=input(f'\n{i}\nEscola as funções:\
                  \n{i}\n(1) Mostra Clientes.\
                  \n(2) Mostrar Contas.\
                  \n(3) Depositar dinheiro.\
                  \n(4) Sacar dinheiro.\
                  \n(5) Transferir.\
                  \n(9) Fechar programa.\n{i}\
                  \nResponda aqui: ')
        
        if per =='1':
            print_clientes()

        elif per == '2':
            print_contas()

        elif per == '3':
            valor=float(input('Qual o valor deseja depositar? '))
            conta.depositar(valor)

        elif per == '4':
                valor=float(input('Qual o valor deseja sacar? '))
                conta.sacar(valor)

        elif per == '5':
            valor=float(input('Qual o valor deseja sacar? '))
            destinatario=encontrar_conta()
            conta.transferir(valor, destinatario)

        elif per == '9':
            print('\nObrigado por utilizar o nosso programa. :)')
            break
        else:
            print('ops, essa função não existe.')
main()