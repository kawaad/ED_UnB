def constituiArvoreBinariaDeBusca(raiz):
  if raiz.esq and raiz.esq.dado > raiz.dado:
    return False
  elif raiz.dir and raiz.dir.dado < raiz.dado:
    return False
  elif raiz.esq and not constituiArvoreBinariaDeBusca(raiz.esq):
    return False
  elif raiz.dir and not constituiArvoreBinariaDeBusca(raiz.dir):
    return False
  return True
