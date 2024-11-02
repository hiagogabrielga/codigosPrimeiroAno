from banco import Banco
class Agencia:
    def __init__(self, numero) -> None:
        self.numero = numero
        banco = Banco('002','Banco Do Brasil')
        self.banco = banco