'''Leia dois valores inteiros e mostre um menu. Seu programa deve mostrar a resolução para cada item do menu.'''

valor1=int(input('Digite o primeiro valor: '))
valor2=int(input('Digite o segundo valor: '))
num=0    
while num!=5:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair')
    num=int(input('O que você gostaria de fazer?: '))
    print()
    if num ==1:
        soma=valor1+valor2
        print('O resultado da soma é: %d'%soma)
        print()
    elif num==2:
        multiplicacao=valor1*valor2
        print('O resultado da multiplicação é: %d'%multiplicacao)    
        print()
    elif num==3:
        if valor1>valor2:
            print('O maior valor é: %d'%valor1)
            print()
        else:
            print('O maior valor é %d'%valor2)
            print()
    elif num==4:
        valor1=int(input('Digite o primeiro valor: '))
        valor2=int(input('Digite o segundo valor: '))  
    elif num==5:
        print()

    else:
        print('Digite um valor válido')    
        print()        

print('Fim do programa, volte sempre!')
    