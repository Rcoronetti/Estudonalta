'''Sequência de Fibonacci'''
termo=int(input('Quantos termos você quer mostrar?: '))
t1=0
t2=1
c=3
print('%d -> %d'%(t1,t2),end='')
while c<=termo:
    t3=t1+t2
    print('->',t3, end='')
    t1=t2
    t2=t3
    c+=1
print(' -> FIM!')    