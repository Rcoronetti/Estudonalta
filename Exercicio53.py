#Palíndromo

frase=input('Digite uma frase: ').strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1]
''' Ou dessa forma:
inverso=''
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]'''
print('O inverso de: %s é: %s'%(junto,inverso))
if junto==inverso:
    print('Isso é um palindromo')
else:
    print('Isso não é um plíndromo')    
