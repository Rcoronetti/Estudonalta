a= float(input('Informe o valor do primeiro segmento: '))
b= float(input('Informe o valor do segundo segmento: '))
c= float(input('Informe o valor do terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('As retas informadas podem formar um triângulo')
else:
    print('As retas informadas não podem formar um triângulo')    