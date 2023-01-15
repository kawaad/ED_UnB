n = int(input())

you_died = "You died!"
in_the_box = "It's in the box!"
bora_rala = "Bora ralar: {}"

cases = {}

for testes in range(n):
  conteudo = list(input())
  u_died = False
  ralar = False
  resto = conteudo
  fora = []
  for turno in range(3):
    cont_passado = list(input())
    resto = list(set(resto) - set(cont_passado))
    fora = list(set(cont_passado) - set(conteudo))
    if fora:
      u_died = True
    

  if u_died:
    cases.update({testes: you_died})
  elif resto:
    cases.update({testes: bora_rala.format(''.join(resto).upper())})
  else:
    cases.update({testes: in_the_box})

for i in cases:
  print(cases[i])
