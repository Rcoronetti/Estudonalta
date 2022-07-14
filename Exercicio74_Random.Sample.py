#Crie um programa que vai gerar cinco números aleatórios e colocar em um tupla.Depois disso, mostre a listagem
# de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

aleatorios = (random.sample(range(100),5))#Esse random irá gerar 5 valores aleatórios até o range 100.
print(aleatorios)
print(f'O maior número é: {max(aleatorios)} ')
print(f'O menor número é: {min(aleatorios)} ')