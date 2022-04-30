#Faça um programa que leia o ano de nascimento de um jovem e informe, de
#acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
#ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nascimento = int(input('Informe o ano do seu nascimento: '))
ano_atual = date.today().year
maioridade = ano_atual	- nascimento
if maioridade ==18:
    print('Você deve se alistar já!')
elif maioridade >18:
    print('Você deveria ter se alistado a {} anos!!'.format(maioridade-18))
else:
    print('Faltam {} anos para você se alistar!'.format(18-maioridade))        
