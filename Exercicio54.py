'''Crie um progra que leia o ano de nascimento de sete pessoas.No final, mostre quantas pessoas já são maiores e quantas não.'''
from datetime import date
cont=0
soma=0

for pess in range (1,8):
    pessoa=int(input('Digite o ano de nascimento: '))
    idade=date.today().year - pessoa
    if idade>=18:
        cont+=1
    else:
        soma+=1    
         
print('A quantidade de pessoas maior de idade é: %d\nA quantidade de pessoas menor de idade é %d'%(cont,soma))