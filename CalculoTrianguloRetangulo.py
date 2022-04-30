from math import sqrt
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adj = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = sqrt ((cateto_oposto**2)+ (cateto_adj**2))
print ('Cateto oposto: %0.2f\nCateto adjacente: %0.2f\nHipotenusa: %0.2f'%(cateto_oposto,cateto_adj,hipotenusa))