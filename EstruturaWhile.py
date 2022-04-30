'''Programa que leia o sexo de uma pessoa, mas só aceite M e F. Caso esteja errado peça que digite novamente até estar correto'''

sexo=str(input('Digite seu sexo com M ou F: ')).upper().strip()[0]
while sexo not in 'MnFf':
    sexo=str(input('Comando não reconhecido, por favor tente novamente: ')).upper().strip()[0]   
print(sexo)    