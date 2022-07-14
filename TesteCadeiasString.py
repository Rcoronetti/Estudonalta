frase = "curso em video python"
print(len(frase)) #Informa a quantidade de caracteres presentes na frase#

print(frase[1:15:2])# Esse comando fatiará a frase da posição 1 até a 15 pulando de 2 em 2#

print(frase[::2])# Indica para que a frase seja mostrada pulando de 2 em 2#

print (frase.count('o'))#Faz a contagem de quantos 'o' aparecem na frase, também é possivel utilizar com fatiamento. ex: frase.count('o',3,15)#

print(frase.find('deo'))#Informa a localização, se existir, dos caracteres na frase. Sempre informa o inicio.#

print (frase.find('android'))#Nesse caso a cadeia de caracteres não existe na frase, então será informado o valor de -1#

print('curso' in frase)# Informa se existe essa cadeia de caracteres na variável. Nesse caso retorna true ou false#

print (frase.replace('python','android'))#replace irá substituir a palavra fornecida pela outra informada. Nesse caso python por android.#

print(frase.upper()) #Transforma todas as letras da variável em maiúsculas#

print(frase.lower())#Transforma todas as letras da variável em minúsculas#

print(frase.capitalize())#Deixa somente e primeira letra em maiúscula e o resto em minúsculas#

print(frase.title())#transforma todos os inícios de palavras em maiúsculas#

frase = '   Aprenda Python  '

print(frase.strip()) # Esse comando irá remover todos os espaços vazios no inicio e final de frase#

print(frase.rstrip())# Esse comando irá remover somente os espaços vazios na direita ( r de right)#

print(frase.lstrip())# Esse comando irá remover somente os espaços vazios na esquerda ( l de left)#

#Divisão de Strings#
print(frase.split())# Esse comando irá dividir a frase de acordo com seus intervalos. Irá gerar uma lista com todas as palavras separadas#

#JUNÇÃO#
print('-'.join(frase))# Esse comando irá juntar os caracteres de uma variável ou lista e separa-los de acordo com o comando dado, no caso
# o separador irá ser - #

#PRINTAR UM TEXTO INTEIRO COM LINHAS SEPARADAS SEM PRECISAR USAR VÁRIOS PRINTS#
print('''Eu, agora - que desfecho!
Já nem penso mais em ti...
Mas será que nunca deixo
De lembrar que te esqueci?''')

