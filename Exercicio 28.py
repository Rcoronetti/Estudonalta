#Escreva um programa que faça o computador “pensar” em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

aleatorio= random.randrange(0,5)
print(aleatorio)
numero = int(input('Digite um número entre 0 e 5: '))

if numero == aleatorio:
    print('\033[1;30;42mYOU WIN!!\033[m')
else:
    print('\033[1;37;41mYOU LOSE!!!!!\033[m')    
