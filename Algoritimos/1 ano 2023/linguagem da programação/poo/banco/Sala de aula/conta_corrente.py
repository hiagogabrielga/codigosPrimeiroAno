from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, cliente, agencia, saldo=0, limite = 100.00) -> None:
        super().__init__(cliente, agencia, saldo)
        self.__limite = limite
        
    def sacar(self, valor):
        if valor <= 0:
            print('O Valor inválido.')
            return False
        
        elif valor > self.saldo + self.__limite:
            print('Saldo insuficiente.')
            return False
        else:
            self.saldo-=valor
            return True