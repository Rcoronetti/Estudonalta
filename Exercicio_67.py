'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para os valores digitados pelo usuário. O programa será interrompido quando o número for negativo'''

while True:
    num=int(input('Digite um número para ver sua tabuada: '))
    if num<=0:
        print('Programa finalizado. Obrigado!')
        break
    
    for cont in range(1,11):
        print(f'{num} x {cont} = {num*cont}')

   
    
    

    
    


