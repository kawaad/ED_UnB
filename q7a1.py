V, E, C = input().split()
V = int(V)
E = int(E)
matrix_a = []
for v in range(V):
  linha = []
  for valor in range(V):
    linha.append(0)
  matrix_a.append(linha)

for e in range(E):
  X, Y, P = input().split()
  X = int(X)
  Y = int(Y)
  P = int(P)
  if C == 'N':
    matrix_a[X - 1][Y - 1] = P
    matrix_a[Y - 1][X - 1] = P
  else:
    matrix_a[X - 1][Y - 1] = P

for mat in matrix_a:
  for n in mat:
    if n == 100:
      print(' ', end="")
    elif n >= 10:
      print('  ', end="")
    else:
      print('   ', end="")
    print(n, end="")
  print()
