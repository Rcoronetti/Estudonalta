#Programa que verifica se existe a palavra silva dentro de um nome#
nome = input('Digite seu nome: ').strip()
index = (nome.upper())

if 'SILVA' in index:
    print('O nome digitado possui a palavra SILVA')
else:    
    print('Não exixte a palavra SILVA no nome digitado')