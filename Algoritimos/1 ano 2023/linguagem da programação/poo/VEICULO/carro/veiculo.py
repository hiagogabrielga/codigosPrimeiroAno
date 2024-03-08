class Veiculo:
    def __init__(self, cor, modelo, ano, marca, buzinar = 0, velocidade = 0) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.velocidade = velocidade
        self.buzinar = buzinar
        print('Objeto do tipo Veiculo construído com sucesso!')

    def alterar_velocidade(self, valor):
        velocidade_atual = self.velocidade + valor
        if velocidade_atual<0:
            print('INDISPONÍVEL')
        else:
            self.velocidade= velocidade_atual
    def buzina(self, valor_bu=int):
        if valor_bu== 1:
            print('Beep')
        elif valor_bu==2:
            print('AAAIIINNNN ZÉÉÉÉ DA MAAANNNGGAAA')
        else:
            print('Buzina Estragada')

''''
crie um método na classe veiculo com o nome de buzinar que receberá por parametro
o valor 1 ou 2, e, conforme o valor, será impresso um tipo de buzina
1 (Beep)
2 (Beeeeeeep)
outros (Buzina estragada)
'''