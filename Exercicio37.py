#Escreva um programa em Python que leia um número inteiro qualquer e peça
#para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num= int(input('Digite um número: '))
print('Escolha a base em que o número será convertido:\n1 - Binário\n2 - Octal\n3 - Hexadecimal')
base = int(input('Sua opção: '))

if base ==1:
    print(num, 'convertido para binário é: ',bin(num)[2:])
elif base ==2:
    print(num, 'convertido para octal é: ',oct(num)[2:]) 
elif base ==3:
    print(num, 'convertido para hexadecimal é: ',hex(num)[2:])   
else:
    print('Não existe a opção selecionada!')        