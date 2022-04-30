'''Maior e menor peso informado'''
maior=0
menor=0
for p in range(1,6):
    peso=float(input('Informe o peso da {}ª pessoa: '.format(p)))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso 
        if peso<menor:
            menor=peso
print('O maior peso lido foi: %0.2fKg\nO menor peso lido foi: %0.2fKg'%(maior,menor))            

