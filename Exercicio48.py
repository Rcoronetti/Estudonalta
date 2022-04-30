#Faça um programa que calcule a soma de todos os números impares que são multiplos de 3 e que estão no intervalo de 1 até 500.
soma=0
cont=0
for c in range(1,501,2):
   if c%3==0:
       soma+=c
       cont+=1
       

print('A soma de todos os %d valores é: %d'%(cont,soma))