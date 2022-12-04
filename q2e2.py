class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item, index):
        self.items.insert(index,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()


activities = input().split()
qtd_realizar = int(input())

new_list = []

for item in range(0, len(activities), 2):
  if not queue.isEmpty():
    for item in range(0, queue.size()):
      if int(activities[item+1]) < int(item.split()[1]):
        queue.enqueue(f'{activities[item]}, Prioridade: #{activities[item+1]}', queue.items[item+1])
      elif int(activities[item+1]) == int(item.split()[1]):
        queue.enqueue(f'{activities[item]}, Prioridade: #{activities[item+1]}', queue.items[item-1])
      else:
        queue.enqueue(f'{activities[item]}, Prioridade: #{activities[item+1]}', 0)
  else:
    queue.enqueue(f'{activities[item]}, Prioridade: #{activities[item+1]}', 0)
print(queue.items)

for item in range(0, qtd_realizar):
  queue.dequeue()

print(f'Tamanho da fila: {queue.size()}')

for item in queue.items:
  print(f'Atividade: {item}')
