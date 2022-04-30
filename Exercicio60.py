'''Programa que leia um número inteiro e mostre seu fatorial!'''

'''from math import factorial
num=int(input('Informe um número: '))
f=factorial(num)
print('O fatorial de %d é: %d'%(num,f))''' 

'''ou'''
num=int(input('Informe um número: '))
cont=num
f=1
while cont>0:
    print(cont,end='')
    print(' x 'if cont>1 else ' = ', end='')
    f=f*cont
    cont-=1
print (f)    


