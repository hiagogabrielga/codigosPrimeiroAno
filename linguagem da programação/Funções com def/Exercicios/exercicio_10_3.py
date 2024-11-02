def detector_d_moeda(moeda,valor):
    lista=['EUR', 'BRL', 'USD']
    moeda=moeda.upper()
    ver=valor.isalpha()
    if lista.count(moeda) == 0:
        return'A moeda citada não está registrada'
    if ver == True:
        return f'{valor} é contido por letras.'
    else:
        lista_d_n=[str(i) for i in (valor)]
        if lista_d_n.count(',') == 1:
            inteiro='00'
            cents='00'
            inteiro=valor.split(',')[0]
            cents=valor.split(',')[1]
            valor=(f'{inteiro}.{cents}')
            valor=float(valor)
            a=int(inteiro)
            b=int(cents)

            if moeda == 'USD':
                if valor > 1:
                    return f'A moeda e valor apresentados foi de $ {valor:.2f} Dólares.'
            
                elif valor < 1:
                    return f'A moeda e valor apresentados foi de {valor:.2f} ¢ "cents".'
            
                else:
                    return f'A moeda e valor apresentados foi de $ {valor:.2f} Dólar.'
            elif moeda == 'EUR':
                if valor > 1.00:
                    return f'A moeda e valor apresentados foi de € {valor:.2f} Euros.'
                else:
                    return f'A moeda e valor apresentados foi de € {valor:.2f} Euro.'
            elif moeda == "BRL":
                inteiro='00'
                cents='00'
                
                valor = str("%.2f" %valor).replace(".",",")

                a = int(valor.split(",")[0])
                b = int(valor.split(",")[1])

                if a > 1:
                    return f'A moeda e valor apresentados foi de R$ {valor} Reais.'
                elif a < 1 and b == 0:
                    return f'A moeda e valor apresentados foi de R$ {valor} Real.'
                elif a == 0 and b > 0:
                    return f'A moeda e valor apresentados foi de R$ {valor} Centavos.'
                valor=float(valor)

        elif lista_d_n.count('.') == 1:
            inteiro='00'
            cents='00'
            inteiro=valor.split('.')[0]
            cents=valor.split('.')[1]
            valor=(f'{inteiro}.{cents}')
            valor=float(valor)
            a=int(inteiro)
            b=int(cents)

            if moeda == 'USD':
                if a > 1:
                    return f'A moeda e valor apresentados foi de $ {valor:.2f} Dólares.'
            
                elif a == 0 and b > 0:
                    return f'A moeda e valor apresentados foi de {valor:.2f} ¢ "cents".'
            
                else:
                    return f'A moeda e valor apresentados foi de $ {valor:.2f} Dólar.'
                
            elif moeda == 'EUR':
                if a == 1 and b == 0:
                    return f'A moeda e valor apresentados foi de € {valor:.2f} Euro.'
                else:
                    return f'A moeda e valor apresentados foi de € {valor:.2f} Euros'
                
            elif moeda == 'BRL':
                inteiro='00'
                cents='00'
                
                valor = str("%.2f" %valor).replace(".",",")

                a = int(valor.split(",")[0])
                b = int(valor.split(",")[1])
    
                if a > 1:
                    return f'A moeda e valor apresentados foi de R$ {valor} Reais.'
                elif a < 1 and b == 0:
                    return f'A moeda e valor apresentados foi de R$ {valor} Real.'
                elif a == 0 and b > 0:
                    return f'A moeda e valor apresentados foi de R$ {valor} Centavos.'
        
        else:
            inteiro='00'
            cents='00'
            inteiro=valor.split()[0]
            valor=(f'{inteiro}.{cents}')
            valor=float(valor)
            a=int(inteiro)
            b=int(cents)
            if moeda == 'USD':
                if a > 1:
                    return f'A moeda e valor apresentados foi de $ {valor:.2f} Dólares.'
            
                elif a == 0 and b > 0:
                    return f'A moeda e valor apresentados foi de {valor:.2f} ¢ "cents".'
            
                else:
                    return f'A moeda e valor apresentados foi de $ {valor:.2f} Dólar.'
                
            elif moeda == 'EUR':
                if a == 1 and b == 0:
                    return f'A moeda e valor apresentados foi de € {valor:.2f} Euro.'
                else:
                    return f'A moeda e valor apresentados foi de € {valor:.2f} Euros'
                
            elif moeda == 'BRL':
                inteiro='00'
                cents='00'
                
                valor = str("%.2f" %valor).replace(".",",")

                a = int(valor.split(",")[0])
                b = int(valor.split(",")[1])

                if a > 1:
                    return f'A moeda e valor apresentados foi de R$ {valor} Reais.'
                elif a < 1 and b == 0:
                    return f'A moeda e valor apresentados foi de R$ {valor} Real.'
                elif a == 0 and b > 0:
                    return f'A moeda e valor apresentados foi de R$ {valor} Centavos.'

print(detector_d_moeda(input('Escolha as seguintes moedas:\nEUR = Euros\nBRL = Reais\nUSD = Dólar\nQual moeda gostária de escolher?'), input('Digite o valor: ')))