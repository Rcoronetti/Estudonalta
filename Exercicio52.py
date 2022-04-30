#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


num=int(input("Digite um número: "))
cont = 0
for c in range(1,num+1):
    if num%c ==0:
        print('\033[33m',end=' ')
        cont+=1        
    else:
        print('\033[31m',end=' ')    
    print('{}'.format(c),end=' ')    
print('\n\033[mO número %d foi divisível %d vezes'%(num,cont))    
if cont ==2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')    