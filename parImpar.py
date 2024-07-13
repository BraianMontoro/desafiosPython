#Recebe um número inteiro do usuário e retorna a condição se o número é PAR ou Impar
while True:
    try:
        valor = int(input('Digite um valor: '))
        if valor % 2 == 0:
            print ('NUMERO PAR')
        else: 
            print ('IMPAR')
    except:
        print('Digite apenas numeros')