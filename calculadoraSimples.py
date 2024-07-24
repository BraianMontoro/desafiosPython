def soma (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def multiplicacao (a,b):
    return a * b

def divisao (a,b):
    return a / b

def calculadora():
    print("Selecione a operação desejada:")
    print("1 - SOMA:")
    print("2 - SUBTRAÇÃO:")
    print("3 - MULTIPLICAÇÃO:")
    print("4 - DIVISÃO:")

    escolha = input("Digite sua escolha: ")

    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(x, "+", y, "=", soma(x,y))
    elif escolha == '2':
        print(x, "+", y, "=", subtracao(x,y))   
    elif escolha == '3':
        print(x, "+", y, "=", multiplicacao(x,y))
    elif escolha == '4':
        print(x, "+", y, "=", divisao(x,y))
    else:
        print("Opção inválida!")

calculadora()