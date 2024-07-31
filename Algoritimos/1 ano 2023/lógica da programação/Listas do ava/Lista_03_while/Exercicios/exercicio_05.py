# Inicializa a variável soma com 0 para contar os números digitados
soma = 0

# Solicita que o usuário digite um número e converte para inteiro
num = int(input('Digite um número: '))

# Enquanto o número digitado for par (num%2 == 0) o loop continua
while num % 2 == 0:
    # Solicita que o usuário digite outro número e converte para inteiro
    num = int(input('Digite um número: '))
    
    # Incrementa a variável soma em 1
    soma += 1
    
    # Se o número for negativo (num < 0) ou ímpar (num % 2 == 1)
    if num < 0 or num % 2 == 1:
        # Interrompe o loop
        break

# Imprime o número de entradas válidas antes do loop ser interrompido
print(f'Fim de programa, números digitados: {soma}')
