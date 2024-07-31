# Inicializa a variável num1 com 1
num1 = 1

# Solicita que o usuário digite um número maior que 1 e positivo
num = int(input('Digite um número maior que 1 e positivo: '))

# Enquanto o número digitado for menor ou igual a 1
while num <= 1:
    # Informa ao usuário que o número é inválido
    print('Você digitou um número menor ou igual a 1. Tente novamente.')
    
    # Solicita novamente que o usuário digite um número maior que 1 e positivo
    num = int(input('Digite um número maior que 1 e positivo: '))

# Enquanto o número digitado for maior que 1
while num1 <= num:
    # Imprime o valor atual de num1
    print(num1)
    
    # Incrementa a variável num1 em 1
    num1 += 1
    
    # Se num1 for igual ao número digitado
    if num1 == num:
        # Imprime o valor atual de num1
        print(num1)
        
        # Interrompe o loop
        break
