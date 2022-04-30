#Escreva um programa para aprovar o empréstimo bancário para a compra de
#uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A
#prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor= float(input('Informe o valor da casa a ser comprada: '))
salario= float(input('Informe seu salário: '))
prazo = int(input('Informe qual o tempo para quitação do bem: '))

prestacao = valor/prazo
prestacao_maxima = salario*0.30

if prestacao <= prestacao_maxima:
    print('O imóvel escolhido será no valor de R$: %0.f\nO valor da parcela será de R$: %0.2f\nO tempo de pagamento será de %d meses'%(valor,prestacao,prazo))
else:
    print('Infelizmente o salário informado não é o suficiente para adquirir o imóvel.')    