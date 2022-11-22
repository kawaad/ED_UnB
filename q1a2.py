string_original = input()
possivel = 'IMPOSSÍVEL'
abc = 'abcdefghijklmnopqrstuvwyxz'
for index_letra, string_letra in enumerate(string_original):

  for letra in abc:
    if letra == string_letra:
      continue
    nova_string = string_original
    nova_string[index_letra] = letra
    string = ''.join(nova_string)
    if string == string[::-1]:
      possivel = 'POSSÍVEL'

  
print(possivel)
