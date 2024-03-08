nota=int(input('Digite a sua nota: '))
while nota < 0 or nota > 100:
    print('só pode ser aceito número positivo de 1 a 100.')
    nota=int(input('Coloque um número valido: '))
print('Sua nota é de', nota)
if nota >= 70:
    print('Parabens você foi aprovado, parabéns!')
elif nota >= 40 and nota < 70:
    print('Você está de recuperação!')
else:
    print('Se lascou!!')