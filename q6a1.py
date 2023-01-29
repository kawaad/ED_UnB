lista = []

class ArvoreBinaria():
  def __init__(self, dado, esq = None, dir = None):
    self.dado = dado
    self.esq = esq
    self.dir = dir

  def inserir(self, valor):
    if self.dado is None:
      self.dado = valor
    else:
      if self.dado != valor:
        if self.dado > valor:
          if self.esq is None:
            self.esq = ArvoreBinaria(valor)
          else:
            self.esq.inserir(valor)
        else:
          if self.dir is None:
            self.dir = ArvoreBinaria(valor)
          else:
            self.dir.inserir(valor)

  def in_print(self):
    if self.dado:
      if self.esq:
        self.esq.in_print()
      lista.append(self.dado)
      if self.dir:
        self.dir.in_print()

  def pre_print(self):
    if self.dado:
      lista.append(self.dado)
      if self.esq:
        self.esq.pre_print()
      if self.dir:
        self.dir.pre_print()

  def pos_print(self):
    if self.dado:
      if self.esq:
        self.esq.pos_print()
      if self.dir:
        self.dir.pos_print()
      lista.append(self.dado)


#lista = [4,2,1,3,6,7,5,'in','pre','pos','quack']

arvore = None

valor = input()

prints = []
while valor != 'quack':

  if valor != 'in' and valor != 'pre' and valor != 'pos':
    if arvore is None:
      arvore = ArvoreBinaria(valor)
    else:
      arvore.inserir(valor)
  elif valor == 'in':
    if arvore:
      arvore.in_print()
      prints.append(' '.join(lista))
      lista = []
    else:
      prints.append('')
  elif valor == 'pre':
    if arvore:
      arvore.pre_print()
      prints.append(' '.join(lista))
      lista = []
    else:
      prints.append('')
  elif valor == 'pos':
    if arvore:
      arvore.pos_print()
      prints.append(' '.join(lista))
      lista = []
    else:
      prints.append('')
  valor = input()

sim = False
for _print in prints:
  if _print:
    sim = True

if sim:
  for _print in prints:
    print(_print)
