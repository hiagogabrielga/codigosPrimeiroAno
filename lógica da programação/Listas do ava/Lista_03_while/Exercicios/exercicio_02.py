# Solicita que o usuário digite um número para soma e converte para inteiro
num1 = int(input('Digite um número para soma: '))

# Solicita que o usuário digite outro número para soma e converte para inteiro
num2 = int(input('Digite outro número para soma: '))

# Calcula a soma dos dois números e imprime o resultado
print(f'A soma de {num1} + {num2} é {num1 + num2}')

# Solicita que o usuário indique se deseja continuar o programa (S/N)
per = input('Gostaria de continuar o programa? (S/N): ')

# Enquanto a resposta for 'S' (sim) ou 's' (sim) o códgio continuara em loop até o usuario digitar uma tecla diferente de 's'(minusculo) ou 'S'(maiusculo)
while per == 's' or per == 'S':
    # Solicita que o usuário digite um número para soma e converte para inteiro
    num1 = int(input('Digite um número para soma: '))

    # Solicita que o usuário digite outro número para soma e converte para inteiro
    num2 = int(input('Digite outro número para soma: '))

    # Calcula a soma dos dois números e imprime o resultado
    print(f'A soma de {num1} + {num2} é {num1 + num2}')

    # Solicita que o usuário indique se deseja continuar o programa (S/N)
    per = input('Gostaria de continuar o programa? (S/N): ')

# Imprime uma mensagem indicando que o programa acabou
print('A soma acaba aqui.')
