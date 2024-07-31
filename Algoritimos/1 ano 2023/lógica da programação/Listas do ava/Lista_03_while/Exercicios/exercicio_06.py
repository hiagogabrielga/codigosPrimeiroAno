# Inicializa a variável media com 0 para somar os números digitados
media = 0

# Inicializa a variável soma com 0 para contar os números digitados
soma = 0

# Solicita que o usuário digite um número e converte para inteiro
num = int(input('Digite um número: '))

# Enquanto o número digitado for ímpar (num % 2 == 1)
while num % 2 == 1:
    # Incrementa a variável soma em 1
    soma += 1
    
    # Adiciona o número digitado à variável media
    media += num
    
    # Solicita que o usuário digite outro número e converte para inteiro
    num = int(input('Digite um número: '))

# Calcula a média dividindo a soma dos números pela quantidade de números digitados
# Garante que a divisão não ocorre por zero
if soma != 0:
    print(f'A média é de {media / soma}')
else:
    print('Nenhum número ímpar foi digitado.')

# Imprime uma mensagem indicando o fim do programa
print('Fim de programa.')
