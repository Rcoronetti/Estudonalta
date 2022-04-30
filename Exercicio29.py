#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
#80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Informe a velocidade do carro: '))
valor = (velocidade-80)*7
if velocidade > 80:
    print('Você foi multado! a velocidade em que seu carro se encontrava era de %d Km/h.\nSua multa será de R$: %d'%(velocidade,valor))
else:
    print('Tenha um bom dia!')    