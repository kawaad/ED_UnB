import operator

n = int(input())
lista = []

for pretendentes in range(n):
  nome, sobrenome, altura, peso = input().split()
  altura = int(altura)
  peso = int(peso)  
  lista.append([nome, sobrenome, altura, peso])

'''lista = sorted(lista, key = operator.itemgetter(2, 3, 1))'''

lista.sort(key=lambda x: ( abs(x[2]-180), 75-x[3] if 75-x[3] >= 0 else x[3], x[1], x[0]))

for item in lista:
  print(f'{item[1]}, {item[0]}')
