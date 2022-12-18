entrada = int(input())

dict = {}

def fibonacci(n):
  valor_atual = dict.get(n)
  dict.update({n: valor_atual+1 if valor_atual else 1})
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

f = fibonacci(entrada)
print(f'fibonacci({entrada}) = {f}.')

if not dict.get(0):
  print(f'0 chamada(s) a fibonacci(0).')

for item, valor in sorted(dict.items()):
  print(f'{valor} chamada(s) a fibonacci({item}).')
