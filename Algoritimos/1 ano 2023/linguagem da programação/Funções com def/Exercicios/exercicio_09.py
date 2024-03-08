def triangulo(a,b,c):
    if a+b > c and a+c > b and b+c > a:
        lista=[a,b,c]
        if lista.count(a) == 3:return f'É um Triângulo Equilatero pois o valor de a, b e c são de: {a}'
        
        elif lista.count(a) == 1:

            if lista.count(b) == 2:return'o triangulo Possui dois lados iguais é um Triângulo Isósceles.'
            
            else:return'o triangulo Possui os três lados diferentes é um Triângulo Escaleno.'

        else:return'O tringulo Possui dois lados iguais é um Triângulo Isósceles.'
    else:
        return"erro! Não é possvel fazer um triangulo"
print(triangulo(int(input('Digite o valor de A: ')), int(input('Digite o valor de B: ')), int(input('Digite o valor de C: '))))