def verifacor(ida:str):
    while True:
        try:
            ida=int(ida)
            if ida >= 18:
                return f'Sua idade é de {ida} anos, você é maior de idade.'
            elif ida < 18 and ida > 4:
                return f'Sua idade é de {ida} anos, Você é menor de idade'
            elif ida < 3 and ida >= 0:
                return'Essa idade é ridiculamente baixa.'
            else:
               return'Os dados apresentados são negativos'
        except:
            return'Dados apresentados invalidos.'
print(verifacor(ida=input('Digite sua idade: ')))