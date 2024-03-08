def detector_d_moeda():
    moeda=input('Escolha as seguintes moedas:\nEUR = Euros\nBRL = Reais\nUSD = Dólar\nQual moeda gostária de escolher?')
    valor=input('Digite o valor: ')
    lista=['EUR', 'BRL', 'USD']
    moeda=moeda.upper()
    ver=valor.isalpha()
    moeda_m=''
    cents_m=''
    while lista.count(moeda) == 0:
        print('A moeda citada não está registrada')
        moeda=input('Escolha as seguintes moedas:\nEUR = Euros\nBRL = Reais\nUSD = Dólar\nQual moeda gostária de escolher?')
        moeda=moeda.upper()
    while ver == True:
        print(f'{valor} é contido por letras.')
        valor=input('Digite o valor novamente: ')
        ver=valor.isalpha()
    else:
        valor = str(valor).replace(".",",")
        lista_d_n=[str(i) for i in (valor)]
        
        if lista_d_n.count(',') == 1:
            inteiro='00'
            cents='00'
            inteiro=valor.split(',')[0]
            cents=valor.split(',')[1]
            valor=(f'{inteiro}.{cents}')
            valor=float(valor)
            valor=f'{valor:.2f}'
            a=int(inteiro)
            b=int(cents)
            if moeda == 'EUR':
                moeda_m = '€'
                cents_m=' '
            elif moeda == 'USD':
                moeda_m='U$'
                if a > 1:  
                    cents_m='Dolares'
                elif a == 0 and b > 0:
                    moeda_m=''
                    cents_m='¢ "cents".'
                elif a == 1 and b == 0:
                    cents_m='Dolar'
            elif moeda == 'BRL':
                valor=float(valor)
                valor = str("%.2f" %valor).replace(".",",")
                moeda_m='R$ '
                if a > 1:  
                    cents_m='Reais'
                elif a == 0 and b > 0:
                    moeda_m=''
                    cents_m='Centavos.'
                elif a == 1 and b == 0:
                    cents_m='Real'
        else:
            cents='00'
            inteiro=valor.split()[0]
            valor=(f'{inteiro}.{cents}')
            valor=float(valor)
            a=int(inteiro)
            b=float(cents)
            if moeda == 'EUR':
                moeda_m = '€ '
                cents_m=' '
                valor=float(valor)
                valor=f'{valor:.2f}'
            elif moeda == 'USD':
                moeda_m='U$ '
                if a > 1:  
                    cents_m='Dolares'
                elif a == 0 and b > 0:
                    moeda_m=''
                    cents_m='¢ "cents".'
                elif a == 1 and b == 0:
                    cents_m='Dolar'
                valor=float(valor)
                valor=f'{valor:.2f}'
            elif moeda == 'BRL':
                valor=float(valor)
                valor = str("%.2f" %valor).replace(".",",")
                moeda_m='R$ '
                if a > 1:  
                    cents_m='Reais'
                elif a == 0 and b > 0:
                    moeda_m=''
                    cents_m='Centavos.'
                elif a == 1 and b == 0:
                    cents_m='Real.'
        
        print(f'O valor ea moeda apresentados foi de {moeda_m}{valor} {cents_m}')
        return (f'{moeda}){valor}')

def conversor(moeda_valor):
    moeda=moeda_valor.split(')')[0]
    valor=moeda_valor.split(')')[1]
    valor = str(valor).replace(",",".")
    valor=float(valor)
    if moeda == 'USD':
        if valor < 0.92:
            convercao1= 'O valor em Dólares é muito curto para ser convertido para Euros.'
        else:
            convercao1=f'EUR -> € {(valor*0.92):.2f}'
        if valor < 4.94:
            convercao2='O valor em Dólares é muito curto para ser convertido para Real.'
        else:
            convercao2=valor*4.94
            convercao2=str("%.2f" %convercao2).replace(".",",")
            convercao2=f'BRL -> R$ {convercao2}.'
        valor=float(valor)
        valor=f'{valor:.2f}'
    elif moeda == 'EUR':
        if valor < 1.08:
            convercao1 = 'O valor em Euros é muito curto para ser convertido para Dólares.'
        if valor < 5.36:

            convercao2 = 'O valor em Euros é muito curto para ser convertido para Real.'
        else:
            convercao1=f'USD -> U$ {(valor*1.08):.2f}'
            convercao2=valor*5.36
            convercao2=str("%.2f" %convercao2).replace(".",",")
            convercao2=f'BRL -> R$ {convercao2}'
        valor=float(valor)
        valor=f'{valor:.2f}'
    elif moeda == 'BRL':
        valor1 = str(valor).replace(",",".")
        valor1=float(valor)
        valor1=f'{valor:.2f}'
        valor1=float(valor)
        if valor < 0.20:
            convercao1='O valor em Real é muito curto para ser convertido para Dólar.'
        else:    
            convercao1=f'USD -> U$ {(valor1*0.20):.2f}'
        if valor < 0.19:
            convercao2='O valor em Real é muito curto para ser convertido para Euro.'
        else:
            convercao2=f'EUR -> € {(valor1*0.19):.2f}'
        valor=float(valor)
        valor=f'{valor:.2f}'
        valor = str(valor).replace(".",",")

    print(f'A converção da moeda {moeda} e do valor {valor} apresentado a cima é de:\n{convercao1}\n{convercao2}\n')


def repetidor():
    while True:
        moeda_valor=detector_d_moeda()
        conversor(moeda_valor)
        per=input('Gostária de continuar? Caso queira basta apertar qualquer tecla, caso NÃO queira, basta digitar "não" ou qualquer palavra com "N":')
        per=per.upper()

        if per == 'NAO' or per == "Não" or 'N':
            return('Obrigado pelo acesso.')
        
print(repetidor())