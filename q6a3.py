def verificaSimetria(raiz):
  if not raiz:
    return True
  return oposto(raiz.esq, raiz.dir)


def oposto(esq, dir):
  if not esq and not dir:
    return True
    
  elif not esq and dir:
    return False

  elif esq and not dir:
    return False
    
  elif esq.dado != dir.dado:
    return False
  
  return oposto(esq.esq, dir.dir) and oposto(esq.dir, dir.esq)
