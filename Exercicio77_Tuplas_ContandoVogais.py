#Crie um programa que tenha uma tupla com várias palavras. Depois disso mostrar para cada palavra, quais são as vogais.
tupla = ('Rafa','Mercado', 'Javali','Penoso', 'Tristeza', 'Jeca', 'Toca' )
for p in tupla:#Esse comando irá percorrer a lista de palavrasna tupla.
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:#Esse comando irá veriricar se tem vogais nas palavras dentro da tupla.
        if letra.lower() in 'aeiou':
            print(letra,end=' ')

