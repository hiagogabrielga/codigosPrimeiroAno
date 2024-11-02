num = int(input(f'Digite o numéro: '))
maior = num
menor = num
for i in range (5):
    num = int(input(f'Digite o numéro: '))
    if num > maior:
        maior=num
    if num < menor:
        menor = num
print(f'O maior número digitado foi {maior}\nO menor número digitado foi {menor}')