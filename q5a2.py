import operator

n = int(input())
lista = []

for pretendentes in range(n):
  nome, sobrenome, altura, peso = input().split()
  altura = int(altura)
  peso = int(peso)
  distancia_altura = abs(altura - 180)
  distancia_peso = 75 - peso if 75 - peso >= 0 else peso
  lista.append([nome, sobrenome, distancia_altura, distancia_peso])

lista = sorted(lista, key = operator.itemgetter(2, 3, 1))

for item in lista:
  print(f'{item[1]}, {item[0]}')
