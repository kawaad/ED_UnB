n = int(input())

altura_ideal = 180
peso_ideal = 75

dict = {}

alturas = []
pesos = []
for pretendentes in range(n):
  nome, sobrenome, altura, peso = input().split()
  altura = int(altura)
  peso = int(peso)
  distancia_altura = altura - 180 if altura >= 180 else 180 - altura
  distancia_peso = peso - 75 if peso >= 75 else 75 - peso
  alturas.append(distancia_altura)
  pesos.append(distancia_pesos)
  dict.update({f'{nome} {sobrenome}': [sobrenome, distancia_altura, distancia_peso]})

melhor_altura = 0

alturas_ideais = []
for item in dict:
  dicio = dict[item]
  if dicio[1] == min(alturas):
    alturas_ideais.append(item)

pesos_ideais = []
for alturas in alturas_ideais:
  dicio = dict[alturas]
  if dicio[2] == min(pesos):
    pesos_ideais.append(item)

for pessoa in pesos_ideais:
  
melhor_altura = min(alturas)



print(dict)

