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
anilha_retirada = False
total_peso = 0


def print_pop_sum(item):
  print(f"Peso retirado: {stack_of_anilhas.pop(item)}")
  total_peso += item

initial_stack_size = stack_of_anilhas.size()

for item in stack_of_anilhas.items:
  if not anilha_retirada:
    if item == anilha:
      print_pop_sum(item)
    else:
      print_pop_sum(item)
  else:
    break

total_anilhas_retiradas = initial_stack_size -  stack_of_anilhas.size()
print(f"Anilhas retiradas: {total_anilhas_retiradas}")

print(f"Peso total movimentado: {total_peso}")
