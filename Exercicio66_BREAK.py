'''Leia vários números inteiros e só pare quando o usuário digitar 999. Mostre no final a soma dos valores digitados, sem mostrar o flag(condição de parada)'''
num=soma =0
while True:   
    soma+=num
    num=int(input('Digite um número ou 999 para parar: '))   
    if num==999:
        break
    
print(f'A soma dos valores digitados é: {soma}')    
