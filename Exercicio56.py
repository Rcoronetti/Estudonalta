'''Programa que leia nome, idade e sexo de 4 pessoas. No final mostre:A média de idade do grupo,O nome do homem mais velho, Quantas mulheres tem menos de 20 anos. '''
media_idade=0
maisnova=0
cont=0
maioridade=0
nomemaisvelho=''
for nom in range(1,5):
    print('----------{}ª pessoa---------------\n'.format(nom))
    nome=input('Informe o nome da {}ª pessoa: '.format(nom))
    idade=int(input('Informe a idade da {}ª pessoa: '.format(nom)))
    sexo= input('Informe o sexo da {}ª pessoa [M/F]: '.format(nom)).upper().strip()
    print('\n')   
    media_idade+=idade
    if sexo=='F':
        if idade<20:
            cont+=1 
    if nom==1 and sexo=='M':
        maioridade=idade
        nomemaisvelho=nome
    if sexo=='M' and idade>maioridade:
        maioridade=idade
        nomemaisvelho=nome
media=media_idade/4          
print('A média de idade do grupo é de {} anos\nO grupo possui {} mulheres com menos de 20 anos\nO homem mais velho se chama {} e tem {} anos'.format(media,cont,nomemaisvelho,maioridade))    

