lista = []

class ArvoreBinaria():
  def __init__(self, dado, esq = None, dir = None):
    self.dado = dado
    self.esq = esq
    self.dir = dir

  def inserir(self, valor):
    if self.dado >= valor:
      if not self.esq:
        self.esq = ArvoreBinaria(valor)
      else:
        self.esq.inserir(valor)
    elif self.dado < valor:
      if not self.dir:
        self.dir = ArvoreBinaria(valor)
      else:
        self.dir.inserir(valor)

  def in_print(self):
    if self.esq:
      self.esq.in_print()
    if self.dado:
      
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
    if self.esq:
      self.esq.pos_print()
    if self.dir:
      self.dir.pos_print()
    if self.dado:
      lista.append(self.dado)


#lista = [4,2,1,3,6,7,5,'in','pre','pos','quack']

arvore = None

valor = input()

while valor != 'quack':

  if isinstance(valor, int) or valor.isdigit():
    if not arvore:
      arvore = ArvoreBinaria(valor)
    else:
      arvore.inserir(valor)
  elif valor == 'in':
    if arvore:
      arvore.in_print()
      print(' '.join(lista))
      lista = []
    else:
      print()
  elif valor == 'pre':
    if arvore:
      arvore.pre_print()
      print(' '.join(lista))
      lista = []
    else:
      print()
  elif valor == 'pos':
    if arvore:
      arvore.pos_print()
      print(' '.join(lista))
      lista = []
    else:
      print()
  valor = input()
