class Veiculo:
    def __init__(self, cor, modelo, ano, marca, velocidade = 0, buzina = 0) -> None:
        self.cor = cor
        self.moedelo = modelo
        self.ano = ano
        self.marca = marca
        self.velocidade = velocidade
        self.buzina = buzina
        print('Objeto do tipo Veiculo construido com sucesso.')

    def alterar_velocidade(self, valor=int):
        velocidade_atual = self.velocidade + valor
        if velocidade_atual < 0:
            print('INSPONÍVEL')
        else:
            self.velocidade =  velocidade_atual
    def tipo_buzina(self, valor_buzina=int):
        novo_valor_buzina = self.buzina + valor_buzina
        if novo_valor_buzina == 1:
            print('Beep')
        elif novo_valor_buzina == 2:
            print('BEEEEEEP')

        else:
            print('Buzina estragada')
#Crie um método na classe veiculo com o nome de buzinar que receberá por parametro
#valor 1 ou 2, e comforme o valor será imposta um tipo de buzina
#1 (Beep)
#2 (BEEEEEEP)
# outro (Buzina estragada)