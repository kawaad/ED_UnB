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

def enqueue_simplify(index):
  queue.enqueue(f'{activities[item]} {activities[item+1]}', index)

for item in range(0, len(activities), 2):
  if not queue.isEmpty():
    
    for qitem in range(0, queue.size()):
      if [s for s in queue.items if activities[item] in s]:
        break
      if activities[item+1] == '4':
        import pdb;pdb.set_trace()
      if int(activities[item+1]) < int(queue.items[qitem].split()[1]):
        enqueue_simplify(qitem+1)
        
      elif int(activities[item+1]) == int(queue.items[qitem].split()[1]):
        enqueue_simplify(qitem-1)
        
      else:
        enqueue_simplify(0)
  else:
    enqueue_simplify(0)
print(queue.items)



for item in range(0, qtd_realizar):
  queue.dequeue()

print(f'Tamanho da fila: {queue.size()}')

for item in queue.items:
  print(f'Atividade: {item}')
