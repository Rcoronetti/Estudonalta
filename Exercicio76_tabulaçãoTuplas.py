#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços. na sequência.
#No final mostre uma listagem de preços, organizando os dados em forma tabular. import tabulate

tupla = ('Pão', 1.00,"Coxa Sobrecoxa", 9.99, 'Amaciante', 5.89,'Sabão em pó', 12.90,'Condicionador', 10.99)
print(f'{"Listagem de Preços":>30}')
print(f'{tupla[0]:.<30} R$:{tupla[1]:>5.2f}')
print(f'{tupla[2]:.<30} R$:{tupla[3]:>5.2f}')
print(f'{tupla[4]:.<30} R$:{tupla[5]:>5.2f}')
print(f'{tupla[6]:.<30} R$:{tupla[7]:>5.2f}')
print(f'{tupla[8]:.<30} R$:{tupla[9]:>5.2f}')