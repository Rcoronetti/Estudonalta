'''Leia vários números inteiros e só pare quando o usuário digitar 999. Mostre no final a soma dos valores digitados, sem mostrar o flag(condição de parada)'''
num= soma =0
num=int(input('Digite um número ou 999 para parar: '))
while num !=999:    
    soma+=num
    num=int(input('Digite um número ou 999 para parar: '))
print('A soma dos valores digitados é: %d'%(soma))    
