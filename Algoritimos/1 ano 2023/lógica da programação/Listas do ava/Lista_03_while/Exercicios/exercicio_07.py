# Inicializa a altura de Pedro com 150 cm
Pedro = 150

# Inicializa a altura de Lucas com 110 cm
Lucas = 110

# Inicializa a variável soma com 0 para contar os anos
soma = 0

# Inicia um loop infinito
while True:
    # Incrementa a altura de Pedro em 2 cm por ano
    Pedro += 2
    
    # Incrementa a altura de Lucas em 3 cm por ano
    Lucas += 3
    
    # Incrementa a variável soma em 1 para contar os anos
    soma += 1
    
    # Verifica se as alturas de Pedro e Lucas são iguais
    if Pedro == Lucas:
        # Imprime a mensagem que Lucas e Pedro estão com a mesma altura
        # Converte as alturas para metros e formata com 2 casas decimais
        print(f'Lucas e Pedro estão com a mesma altura, Lucas tem {Lucas / 100:.2f}m e Pedro tem {Pedro / 100:.2f}m\nForam necessários {soma} anos')
        
        # Interrompe o loop
        break
    
    # Verifica se a altura de Lucas é maior que a altura de Pedro
    if Lucas > Pedro:
        # Imprime a mensagem que Lucas e Pedro estão com alturas diferentes
        # Converte as alturas para metros e formata com 2 casas decimais
        print(f'Lucas e Pedro estão com alturas diferentes, Lucas tem {Lucas / 100:.2f}m e Pedro tem {Pedro / 100:.2f}m\nForam necessários {soma} anos')
        
        # Interrompe o loop
        break
