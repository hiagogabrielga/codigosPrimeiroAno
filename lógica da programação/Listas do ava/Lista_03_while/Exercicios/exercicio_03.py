# Inicia um loop infinito
while True:
    # Solicita que o usuário digite um número para multiplicar e converte para inteiro
    num = int(input('Digite o número a ser multiplicado: '))
    
    # Verifica se o número digitado é 999
    if num == 999:
        # Se for 999, interrompe o loop
        break
    
    # Calcula o triplo do número digitado e imprime o resultado
    print(f'O triplo de {num} é {num * 3}')

# Imprime uma mensagem indicando o fim do programa
print('Fim de programa.')
