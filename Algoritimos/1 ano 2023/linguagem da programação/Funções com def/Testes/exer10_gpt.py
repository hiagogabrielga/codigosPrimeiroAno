from forex_python.converter import CurrencyRates

def leitura_valores():
    valor = float(input("Digite o valor monetário: "))
    moeda = input("Digite a moeda (Real, Euro ou Dólar): ")
    return valor, moeda

def conversao_monetaria(valor, moeda):
    c = CurrencyRates()
    if moeda.lower() == 'real':
        converted_values = {
            'Euro': c.convert('BRL', 'EUR', valor),
            'Dólar': c.convert('BRL', 'USD', valor)
        }
    elif moeda.lower() == 'euro':
        converted_values = {
            'Real': c.convert('EUR', 'BRL', valor),
            'Dólar': c.convert('EUR', 'USD', valor)
        }
    elif moeda.lower() == 'dólar':
        converted_values = {
            'Real': c.convert('USD', 'BRL', valor),
            'Euro': c.convert('USD', 'EUR', valor)
        }
    else:
        return "Moeda não reconhecida"
    
    return converted_values

def main():
    continuar = True
    while continuar:
        valor, moeda = leitura_valores()
        valores_convertidos = conversao_monetaria(valor, moeda)
        
        print("Valores convertidos:")
        for moeda, valor_convertido in valores_convertidos.items():
            print(f"{moeda}: {valor_convertido:.2f}")
        
        resposta = input("Deseja realizar uma nova conversão? (sim/não): ")
        if resposta.lower() != 'sim':
            continuar = False

if __name__ == "__main__":
    main()