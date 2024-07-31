# Solicita que o usuário digite o nome
nome = input('Digite seu nome: ')

# Solicita que o usuário digite o sexo
s = input('Digite o sexo: ')

# Enquanto a entrada para o sexo não for 'M' (masculino) ou 'F' (feminino) o loop será INFINITO.
while s != 'M' and s != 'F':
    # Informa ao usuário que os dados são inválidos
    print('Dados inválidos.')
    # Solicita novamente que o usuário digite o sexo
    s = input('Digite o sexo: ')

# Informa ao usuário que os dados são válidos
print('Dados válidos')

# Verifica se o sexo é masculino
if s == 'M':
    # Se for masculino, imprime o nome e uma mensagem indicando que o sexo é masculino
    print(f'{nome}, seu sexo é Masculino')

# Verifica se o sexo é feminino
elif s == 'F':
    # Se for feminino, imprime o nome e uma mensagem indicando que o sexo é feminino
    print(f'{nome}, seu sexo é Feminino')
