'''Refaça o exercicio 51 lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando while.'''
primeiro= int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo_termo =primeiro+(10-1)*razao
c=primeiro

while c <= decimo_termo:    
    print(c, end=" -> ")
    c=c+razao
print ('Acabou')     

