#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 a 20.Seu programa deverá ler um número pelo teclado(0 a 20) e mostrá-lo por 
# extenso
contagem=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero=int(input("Digite um número entre 0 e 20: ")) 
while numero <0 or numero > 20:
    print('Tente novamente!')
    numero=int(input("Digite um número entre 0 e 20: ")) 
   
print(f'Você digitou o número {contagem[numero]}')