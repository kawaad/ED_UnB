n = int(input())

altura_ideal = 180
peso_ideal = 75

dict = {}

for pretendentes in range(n):
  nome, sobrenome, altura, peso = input().split()
  dict.update({nome: [sobrenome, int(altura), int(peso)]})

print(dict)
