#Recebe um número, uma potência, e retorna a tabuada e o número elevado à potência solicitada
import math

while True: 
    try:
        numero = int(input("Digite um número: "))
        potencia = int(input("Digite uma potência: "))
    except: 
        print("Digite apenas número")

    print("O número digitado foi:", numero, "A potencia escolhida foi:", potencia)
    print("A tabuada do número:", numero, "é:")

    for i in range(1,11):
        x = numero * i
        print(str(numero) + " X " + str(i) + " = " + str(x))

    print("A potencia do número escolhido é: " + str(math.pow(numero,potencia)))