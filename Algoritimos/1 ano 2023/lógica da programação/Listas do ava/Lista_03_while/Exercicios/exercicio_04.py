# Solicita que o usuário digite o nome de usuário
usu = input('Digite o nome do usuário: ')

# Solicita que o usuário digite a senha
sen = input('Digite a senha: ')

# Enquanto o nome de usuário não for 'ALUNO' ou a senha não for 'Lógic@2023'
while usu != 'ALUNO' or sen != 'Lógic@2023':
    # Informa ao usuário que a senha ou o nome de usuário estão incorretos
    print('Senha ou usuário incorretos.')

    # Solicita novamente que o usuário digite o nome de usuário
    usu = input('Digite o nome do usuário novamente: ')

    # Solicita novamente que o usuário digite a senha
    sen = input('Digite a senha novamente: ')

# Quando as credenciais corretas são fornecidas, informa que o usuário foi autenticado
print('Usuário autenticado')
