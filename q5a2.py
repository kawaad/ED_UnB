import operator

n = int(input())
lista = []

for pretendentes in range(n):
  nome, sobrenome, altura, peso = input().split()
  altura = int(altura)
  peso = int(peso)
  distancia_altura = altura - 180 if altura >= 180 else 180 - altura
  distancia_peso = peso - 75 if peso >= 75 else 75 - peso
  
  lista.append([nome, sobrenome, distancia_altura, distancia_peso])

lista = sorted(lista, key = operator.itemgetter(2, 3))

for item in lista:
  print(f'{item[1]}, {item[0]}')
