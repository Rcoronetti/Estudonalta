#Faça um programa que leia um número de 0 a 9999
#e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número entre a 0 e 9999: '))
unidade = num%10
dezena = num//10%10
centena = num//100%10
milhar = num//1000%10

print(unidade,dezena,centena,milhar)

 