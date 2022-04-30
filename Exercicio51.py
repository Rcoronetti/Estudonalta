# 10 termos de uma PA

primeiro= int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo_termo =primeiro+(10-1)*razao
print(decimo_termo)
for c in range(primeiro,decimo_termo+razao,razao):
    print(c, end=" -> ")
print ('Acabou')    