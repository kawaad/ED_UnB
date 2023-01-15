n = int(input())

you_died = "You died!"
in_the_box = "It's in the box!"
bora_rala = "Bora ralar: {}"

cases = {}

for testes in range(n):
  conteudo = input()
  ralar = False
  fora = False
  for turno in range(3):
    cont_passado = list(input())
    for letra in cont_passado:
      if letra not in conteudo:
          fora = True
      else:
        list_conteudo = list(conteudo)
        del(list_conteudo[conteudo.find(letra)])
        conteudo = ''.join(list_conteudo)
  list_conteudo = list(conteudo)

  conteudo = ''.join(set(conteudo))
    
  if fora:
    cases.update({testes: you_died})
  elif conteudo:
    cases.update({testes: bora_rala.format(''.join(sorted(conteudo)).upper())})
  else:
    cases.update({testes: in_the_box})

for i in cases:
  print(cases[i])
