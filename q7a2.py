class No:

  def __init__(self, id, vizinhos):
    self.id = id
    self.lista_vizinhos = vizinhos

lista_nos = {}

n = int(input())

for i in range(n):
  lista = input().split()
  linhas = list(map(int, lista))
  id = linhas[0]
  qtd_arest = linhas[1]
  resto = linhas[2:]
  no = No(id, resto)
  lista_nos[id] = no


eu, mussum = list(map(int, input().split()))

nos_percor = []
nos_atuais = []
nos_atuais.append(lista_nos[eu])

distancia = 0
nao_achou = True
while nao_achou:

  nos_proximos = []
  for nos in nos_atuais:
    
    lista_v = nos.lista_vizinhos 
    for viz in lista_v:
      if viz not in nos_percor:
        nos_proximos.append(lista_nos[viz])
        nos_percor.append(lista_nos[viz])
  for NOS in nos_proximos:
    if NOS.id == mussum:
      print(distancia)
      nao_achou = False
      break
  if not nos_proximos:
    print('Forevis alonis...')
    break
  else:
    nos_atuais = nos_proximos
    distancia += 1
