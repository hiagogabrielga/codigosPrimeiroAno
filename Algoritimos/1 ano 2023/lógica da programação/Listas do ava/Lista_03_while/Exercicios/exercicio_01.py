nome=input('Digite seu nome: ')
s=input('Digite o sexo: ')
while s != 'M' and s != 'F':
    print('Dados inválido.')
    s=input('Digite o sexo: ')    
print('Dados válidos')
if s == 'M':
    print(f'{nome} Seu sexo é Masculino')
elif s == 'F':
     print(f'{nome} Seu sexo é Feminino')
