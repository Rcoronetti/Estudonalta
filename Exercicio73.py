#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de futebol.
#Na ordem de colocação.Depois mostre:
#Apenas os 5 primeiros colocados.
#Os ultimos 4 colocados.
#Uma lista com os times em ordem alfabética.
#Em que posição na tabela está o time da Chapecoense.

classificacao= ('Cruzeiro','Bahia','Sport','Vasco','Operário-PR','Grêmio','Novorizontino','Sampaio Corrêa-MA','Náutico','Tombense-MG','CSA','Londrina','CRB','Chapecoense','Brusque ','Ituano','Criciúma','Vila Nova','Ponte Preta','Guarani')
print(f'Os times da série B do campeonato brasileiro são: {classificacao}\n')
print(f'Os 5 primeiros colocados são: {classificacao[:5]}\n')
print(f'Os 4 últimos colocados são: {classificacao[16:]}\n')
print(f'Os times em ordem alfabética {sorted(classificacao)}\n')
chape=classificacao.index('Chapecoense',1)
print(f'A Chapecoense está na {chape+1}ª posição: ')
