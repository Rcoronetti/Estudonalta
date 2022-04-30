from math import sqrt
A,B,C=map(float,input().split())

delta= (B**2)-(4*A*C)
print(delta)
if delta<0 or A==0:
    print('Impossivel calcular')
else:    
    raizdelta= sqrt(delta)    
    raiz1=(((-B+raizdelta)/2*A)/100)
    raiz2=(((-B-raizdelta)/2*A)/100)
    print('R1 = %0.5f'%raiz1)
    print('R2 = %0.5f'%raiz2)

    
