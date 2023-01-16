def altura_ordem(alturas):
   for fillslot in range(len(alturas)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alturas[location]>alturas[positionOfMax]:
               positionOfMax = location

       temp = alturas[fillslot]
       alturas[fillslot] = alturas[positionOfMax]
       alturas[positionOfMax] = temp

n = int(input())
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
  pesos.append(distancia_peso)
  dict.update({f'{sobrenome}, {nome}': [sobrenome, distancia_altura, distancia_peso]})

altura_ordem(alturas)


for altura in alturas:
  for item in dict:
    dicio = dict[item]
    if dicio[1] == altura:
      print(item)
