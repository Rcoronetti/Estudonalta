#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
#aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').strip()
index = frase.upper()
cont = index.count('A')
posicaol = index.find('A')
posicaor = index.rfind('A')
print('A frase escolhida foi:',frase)
print('A letra A aparece %s vezes'%cont)
print('A letra A aparece pela primeira vez na posição:',posicaol)
print('A letra A aparece pela ultima vez na posição:',posicaor)

