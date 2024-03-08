from abc import ABC, abstractmethod

class Conta(ABC):
    numero=0
    def __init__(self, cliente, agencia, saldo=0):
        self.cliente = cliente
        Conta.numero +=1
        self.numero = Conta.numero
        self.agencia = agencia
        self.saldo = saldo
    
    # def sacar(self, valor):
    #     if valor < 0:
    #         print('O Valor não pode ser negativo.')
    #         return False
        
    #     elif valor > self.saldo:
    #         print('Saldo insuficiente.')
    #         return False
    #     else:
    #         self.saldo-=valor
    #         return True
    @abstractmethod
    def sacar(self,valor):
        pass

    def depositar(self, valor):
        if valor < 0:
            print('O valro não pode ser menor que zero.')
            return False
        else:
            self.saldo+=valor
            return True
    
    def transferir(self, valor, destinatario):
        if self.sacar(valor):
            destinatario.depositar(valor)
            print('Trasferência realizada com sucesso!')
        else:
            print('Transferência não realizada.')