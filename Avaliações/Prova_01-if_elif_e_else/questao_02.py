data=int(input('digite sua data de nascimento: '))
idade=2023-data
if idade>=65:
    print(f'você poderá se aposentar\nPois sua idade é de {idade} e a idade miníma é de 65!!')
else:
    print(f'você não poderá se aposentar pela sua idade\nPois sua idade é de {idade} e a idade miníma é de 65')