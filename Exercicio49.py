#Refaça o exerc. 9, tabuada,  mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.

num = int(input('Informe um número: '))
for c in range(1,11):    
    print (print('{} x {} = {}'.format(num,c,num*c)))    