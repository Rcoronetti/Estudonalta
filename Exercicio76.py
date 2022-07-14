#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços. na sequência.
#No final mostre uma listagem de preços, organizando os dados em forma tabular. import tabulate

tupla = ('Pão', 1.00,"Coxa Sobrecoxa", 9.99, 'Amaciante', 5.89,'Sabão em pó', 12.90,'Condicionador', 10.99)
print(f'Listagem de Preços')
print(f'{tupla[0]} {tupla[1]:>30.2f}')
print(f'{tupla[2]} {tupla[3]:>30.2f}')
print(f'{tupla[4]} {tupla[5]:>30.2f}')
print(f'{tupla[6]:<10} {tupla[7]:>10,.2f}')
print(f'{tupla[8]:<10} {tupla[9]:>10,.2f}')