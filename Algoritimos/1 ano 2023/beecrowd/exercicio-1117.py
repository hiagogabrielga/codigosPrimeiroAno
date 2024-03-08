num = float(input())
while num < 0 or num > 10:
    print('nota invalida')
    num = float(input())
num2 = float(input())
while num2 < 0 or num2 > 10:
    print('nota invalida')
    num2 = float(input())
print(f'media = {(num+num2)/2:.2f}')

