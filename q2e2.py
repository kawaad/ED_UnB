class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item, index):
        self.items.insert(index, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def remove(self, index):
        self.items.remove(self.items[index])

queue = Queue()

activities = input().split()
qtd_realizar = int(input())

new_list = []

for item in range(0, len(activities), 2):
    queue.enqueue([activities[item], activities[item+1]], 0)

for tam in range(0, queue.size()):
    for iitem, qitem in enumerate(queue.items):
        if iitem+2 <= queue.size():
            if int(qitem[1]) < int(queue.items[iitem+1][1]):
                queue.remove(iitem)
                queue.enqueue(qitem, iitem+1)

for item in range(0, qtd_realizar):
    if queue.isEmpty():
        break
    queue.dequeue()

print(f'Tamanho da fila: {queue.size()}')

for tam in range(0, queue.size()):
  item = queue.dequeue()
  print(f'Atividade: {item[0]}, Prioridade: #{item[1]}')
