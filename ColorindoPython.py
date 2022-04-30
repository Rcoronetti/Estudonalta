#Stilo: 0 = nada; 1 = Negrito; 4 = Sublinhado; 7 = inverte as configurações.
# texto de 30 a 37: 30 = branco ; 31 = vermelho; 32= verde; 33 = amarelo; 34= azul; 35= roxo; 36= ciano; 37= cinza.
#background de 40 a 47: mesma sequência acima.

print('\033[0;30;41mtestevermelho\033[m')
print('\033[1;30;44mtesteazul\033[m')
print('\033[4;35;43mtesteamarelo\033[m')
print('\033[mtestebranco\033[m')
print('\033[7;30mtestebrancopreto\033[m')

# O código \033[m é a formatação de cores. utilizem ela para abrir a formatação e fechar até onde seja necessário.