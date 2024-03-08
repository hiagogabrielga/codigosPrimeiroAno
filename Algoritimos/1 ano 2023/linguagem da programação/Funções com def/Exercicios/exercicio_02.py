def calculadora(num1,num2,op):
    lista_d_n=[str(idade) for idade in range (10)]

    for i in num1:
            if lista_d_n.count(i) == 0: return "Número Inválido"
    for i in num2:
            if lista_d_n.count(i) == 0: return "Número Inválido"
    num1=float(num1)
    num2=float(num2)
    
    if op == "+":
           return f"{num1} {op} {num2} = {num1+num2}"
    if op == "/":
           return f"{num1} {op} {num2} = {num1/num2}"
    if op == "-":
           return f"{num1} {op} {num2} = {num1-num2}"
    if op == "*" or op == "x":
           return f"{num1} {op} {num2} = {num1*num2}"
print(calculadora(num1=input('Digite Seu Número:'),op=input('Digite sua operação: '),num2=input('Digite seu outro número: ')))