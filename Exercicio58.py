'''Melhore o jogo do desafio 28, só que agora o jogador vai adivinhar até acertar.Mostre no final quantos palpites foram necessários.'''

import random
cont=0
aleatorio= random.randrange(0,5)
'''print(aleatorio)'''
numero = int(input('Digite um número entre 0 e 5: '))
while numero!=aleatorio:
    numero=int(input(('\033[1;37;41mVocê errou!Tente novamente: \033[m')))    
    cont+=1


print('\033[1;30;42mYOU WIN!!\033[m')
print('Você acertou com %d tentativas'%(cont+1))
   
