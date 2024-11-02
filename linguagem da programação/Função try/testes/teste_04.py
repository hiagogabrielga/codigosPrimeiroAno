def main ():
    print('Vamos dividir!')
    while True:
        try:
            x = input('Digite o primeiro valor: ')
            x = int(x)
            y = input('Digite o segundo valor: ')
            y = int(y)
            r=x/y
            break
        except ValueError:
            print('Este progarama só aceita números.')
        except ZeroDivisionError:
            print('Não é possivel dividir por zero.')
        except:
            print('Ocorreu algum erro.')
   
    print(f'O resultado da divisão é: {r}')
main()