entrada = int(input())

dict = {}

def fibonacci(n):
  dict.update({n: dict.get(n)+1})
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

f = fibonacci(entrada)
print(f'fibonacci({entrada}) = {f}.')

for item, valor in dict.items():
  print(f'{valor} chamada(s) a fibonacci({item}).')
print(lista)
