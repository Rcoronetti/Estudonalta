#Programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for impar, desconsidere.
soma=0
cont = 0
for c in range(0,6):
    num=int(input('Digite um número: '))
    if num % 2 ==0:
        soma +=num
        cont +=1
print('Você informou %d números pares.\nA soma dos números é:%d.'%(cont,soma))        