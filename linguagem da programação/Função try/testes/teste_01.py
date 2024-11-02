try:
    def main():
        resultado = numero + 10
        print(resultado)
    main()
except:
    print('Não é possivel fazer a soma.')
    numero=int(input())
    main()