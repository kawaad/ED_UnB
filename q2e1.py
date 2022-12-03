class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

stack_of_anilhas = Stack()

value = int(input())

while value != 0:
  stack_of_anilhas.push(value)
  value = int(input())

anilha = int(input())
retirou = False
total_peso = 0

initial_stack_size = stack_of_anilhas.size()

def print_peso(peso):
  print(f"Peso retirado: {peso}")

def anilha_verify(anilha_retirada):
  if anilha_retirada == anilha:
    print_peso(anilha_retirada)
    total_peso += anilha_retirada
    retirou = True
  else:
    print_peso(anilha_retirada)
    total_peso += anilha_retirada


for item in range(stack_of_anilhas.size):
  if not anilha_retirada:
    anilha_retirada = stack_of_anilhas.pop()
    anilha_verify(anilha_retirada)
  else:
    break

total_anilhas_retiradas = initial_stack_size -  stack_of_anilhas.size()
print(f"Anilhas retiradas: {total_anilhas_retiradas}")

print(f"Peso total movimentado: {total_peso}")
