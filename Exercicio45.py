#Game-pedra, papel, tesoura

import random


print('Essas são suas opções:\n0 - Pedra\n1 - Papel\n2 - Tesoura')
jogador = int(input("Qual é  sua jogada?: "))
pc = random.choice(['pedra','papel','tesoura'])
itens = ('pedra','papel','tesoura')
print('PC jogou: ',pc)
print('Jogador jogou: {}'.format(itens[jogador]))
if jogador == 0 and pc =='pedra':
    print('empate')
elif jogador ==0 and pc =='papel':
    print('lose')
elif jogador ==0 and pc == 'tesoura':
    print('win!')        
elif jogador == 1 and pc =='pedra':
    print('lose')
elif jogador ==1 and pc =='papel':
    print('empate')
elif jogador ==1 and pc == 'tesoura':  
    print('lose')
elif jogador == 2 and pc =='pedra':
    print('lose')
elif jogador ==2 and pc =='papel':
    print('win!')
elif jogador ==2 and pc == 'tesoura':  
    print('empate')     
else:
    print('Digite uma jogada válida!')    