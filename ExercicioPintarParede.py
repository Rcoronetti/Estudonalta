altura = float(input("Informe a altura da parede: ")) 
largura = float(input("Informe a largura da parede: ")) 
area = altura * largura
tinta = area/2
print("Sua parede tem a dimensão de : %0.2f x %0.2f e sua área é de: %0.2f m²\nA quantidade de tinta necessária  é de: %0.2f L" %(altura,largura,area,tinta))