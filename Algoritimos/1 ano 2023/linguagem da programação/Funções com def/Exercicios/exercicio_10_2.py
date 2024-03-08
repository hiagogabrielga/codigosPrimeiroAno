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
        if moeda == 'USD':
            if valor > 1:
                return f'A moeda e valor apresentados foi de $ {valor:.2f} Dólares.'
            
            elif valor < 1:
                return f'A moeda e valor apresentados foi de {valor:.2f} ¢ "cents".'
            
            else:
                return f'A moeda e valor apresentados foi de $ {valor:.2f} Dólar.'
        elif moeda == 'EUR':
            if valor > 1:
                return f'A moeda e valor apresentados foi de € {valor:.2f} Euros.'
            else:
                return f'A moeda e valor apresentados foi de € {valor:.2f} Euro.'
        
            