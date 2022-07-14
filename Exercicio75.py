#Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla.No final, mostre:
#Quantas vezes apareceu o valor 9.
#Em que posição foi digitado o primeiro valor 3.
#Quais foram os números pares.
tupla=(int(input(f"Informe o 1ª valor: ")),int(input(f"Informe o 1ª valor: ")),int(input(f"Informe o 1ª valor: ")),int(input(f"Informe o 1ª valor: ")))
print(f'Você informou os valores : {tupla}')    
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
print(f'O valor 3 aparece na posição {tupla.index(3)}')
print(f'Os números pares são {}')   