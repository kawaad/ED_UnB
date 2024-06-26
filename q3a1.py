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
NL = list(map(int, input().split()))
K = int(input())

deque = Deque()
deque_window = Deque()
deque_max = Deque()

def append_max():
  deque_max.addFront(max(deque_window.items))

for item in range(N):
  if deque_window.isEmpty():
    for k in range(K):
      deque_window.addFront(NL[k])
    append_max()
  else:
    if item <= N - K:
      deque_window.removeRear()
      deque_window.addFront(NL[item+K-1])
      append_max()

print(*deque_max.items, sep='  ')

