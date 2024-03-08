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
                return f'foi citado a seguinte moeda e valor:\n{moeda} {valor}'
        elif lista_d_n.count('.') == 1 :
            int='00'
            cents='00'
            int=valor.split('.')[0]
            cents=valor.split('.')[1]
            return f'foi citado a seguinte moeda e valor:\n{moeda} {int},{cents}' 
        else:
            return f'foi citado a seguinte moeda e valor:\n{moeda} {valor},00'
        
print(detector_d_moeda(input('Escolha as seguintes moedas:\nEUR = Euros\nBrl = Reais\nUSD = Dólar\nQual moeda gostária de escolher?'), input('Digite o valor: ')))