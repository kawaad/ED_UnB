class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


N = int(input())
NL = map(int, input().split())
K = int(input())

deque = Deque()
deque_max = Deque()

def append_max():
  deque_max.append(max(deque.items))

for i in range(N):
  if deque.isEmpty:
    for k in range(K):
      deque.addFront(NL[k])
    append_max()
  else:
    deque.removeRear()
    deque.addFront(NL[i+2])
    append_max()


print(deque_max)
