#Faça um programa que leia o nome completo de uma pessoa, mostrando em
#seguida o primeiro e o último nome separadamente.

nome= str(input('Digite seu nome: ')).strip()
index = nome.split()
print('O primeiro nome é: {}'.format(index[0]))
print('O último nome é: {}'.format(index[len(index)-1]))

