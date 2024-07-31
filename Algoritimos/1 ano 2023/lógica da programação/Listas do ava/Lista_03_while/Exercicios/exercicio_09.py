# Inicializa a variável sucessor com 1. Esta variável será usada para multiplicar no cálculo do fatorial.
sucessor = 1

# Inicializa a variável fatorial com 1. Esta variável armazenará o resultado do cálculo do fatorial.
fatorial = 1

# Solicita ao usuário que digite um número maior que 1 e positivo.
num = int(input('Digite um número maior que 1 e positivo: '))

# Valida se o número digitado é maior que 1. Se não for, solicita um novo número.
while num <= 1:
    print("Por favor, digite um número maior que 1.")
    num = int(input('Digite um número maior que 1 e positivo: '))

# Calcula o fatorial do número fornecido. O loop continua enquanto o sucessor for menor ou igual ao número.
while sucessor <= num:
    # Multiplica o fatorial pelo sucessor atual.
    fatorial *= sucessor
    
    # Incrementa o sucessor para o próximo número.
    sucessor += 1

# Após o cálculo do fatorial, exibe o resultado no formato "num! = fatorial".
print(f'{num}! = {fatorial}')
