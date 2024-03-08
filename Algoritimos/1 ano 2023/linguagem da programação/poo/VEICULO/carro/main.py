from veiculo import Veiculo
ka = Veiculo('Preto','I3',2020,'BMW')

print('Velocidade', ka.velocidade)
ka.alterar_velocidade(int(input("Digite uma velocidade: ")))
print('A Nova Velocidade é', ka.velocidade)


ka.buzina(1)

ka.buzina(2)

ka.buzina(5)
