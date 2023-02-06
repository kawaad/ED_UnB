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
  vizinhos = []
  if len(linhas) > 2: 
    resto = linhas[2:]
    resto_iteravel = iter(resto)
    resto =  zip(resto_iteravel, resto_iteravel)
    for x, y in resto:
      vizinhos.append((y, x))
  no = No(id, vizinhos)
  lista_nos[id] = no

arestas_incluidas = []
vertices_incluidos = []
id_vertices_incluidos = []

vertices_incluidos.append(lista_nos[list(lista_nos)[0]])
id_vertices_incluidos.append(lista_nos[list(lista_nos)[0]].id)

while len(vertices_incluidos) != len(lista_nos):
  arestas_atuais = []
  for no in vertices_incluidos:
    id_no = no.id
    for vizinho in no.lista_vizinhos:
      id_vizinho = vizinho[0]
      peso_vizinho = vizinho[1]
      aresta = [[id_no, id_vizinho], peso_vizinho]
      arestas_atuais.append(aresta)
  aresta_menor_peso = None
  for aresta in arestas_atuais:
    if not all(element in id_vertices_incluidos for element in aresta[0]):
      if aresta_menor_peso is None:
        aresta_menor_peso = aresta
      elif aresta_menor_peso[1] > aresta[1]:
        aresta_menor_peso = aresta
  arestas_incluidas.append(aresta_menor_peso)
  vertice = lista_nos[int(aresta_menor_peso[0][1])]
  vertices_incluidos.append(vertice)
  id_vertices_incluidos.append(vertice.id)

valor = 0
for aresta in arestas_incluidas:
  valor += aresta[1]

print(f'R$ {valor*3.14:.2f}')
      
