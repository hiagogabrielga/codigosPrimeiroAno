def relogio(hhmm):
    hh=hhmm.split(':')[0]
    mm=hhmm.split(':')[1]
    lista_d_n1=[str(i) for i in range (25)]
    lista_d_n2=[str(i) for i in range (61)]
    lista_d_n3=['00','01','02','03','04','05','06','07','08','09']
    lista_d_n4=lista_d_n1 + lista_d_n3
    lista_d_n5=lista_d_n2 + lista_d_n3

    if lista_d_n4.count(hh) == 0: 
        return "Hora Inválida."
    if lista_d_n5.count(mm) == 0: 
        return "Hora Inválida."
    else:
        if hh == '01':
            if mm == '00':
                return f'São {hh} hora em ponto.'
            elif mm == '01':
                return f'São {hh} hora e {mm} mínuto.'
            
            elif mm == '30':
                return f'São {hh} hora e meia.'

            else:
                return f'São {hh} hora e {mm} mínutos.'
        
        elif hh == '12':
            if mm == '00':
                return f'São meio dia em ponto.'
            
            elif mm == '01':
                return f'São meio dia e {mm} mínuto.'
            
            elif mm == '30':
                return f'São meio dia e meia.'
            
            else:
                return f'São meio dia e {mm} mínutos.'
        elif hh == '00':
            if mm == '00':
                return f'São meia noite em ponto.'
            
            elif mm == '01':
                return f'São meia noite e {mm} mínuto.'
            
            elif mm == '30':
                return f'São meia noite e meia.'
            
            else:
                return f'São meia noite e {mm} mínutos.'
        elif mm == '01':
                return f'São {hh} horas e {mm} mínuto.'
            
        elif mm == '30':
            return f'São {hh} horas e meia.'
        
        elif mm == '00':
            return f'São {hh} horas em ponto.'
        
        else:
            return f'São {hh} horas e {mm} mínutos.'
print(relogio(hhmm=input('Digite a hora: ')))