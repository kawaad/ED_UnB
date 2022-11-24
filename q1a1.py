dia_inicio, horario_inicio = '5 08:12:23'.split()
dia_fim, horario_fim = '9 06:13:23'.split()

dia_inicio, dia_fim = int(dia_inicio), int(dia_fim)

hora_inicio, minutos_inicio, segundos_inicio = map(int, horario_inicio.split(':'))

hora_fim, minutos_fim, segundos_fim = map(int, horario_fim.split(':'))

segundos = 60
minutos = segundos * 60
hora = minutos * 60
dia = hora * 24

if hora_inicio > 0:
  dia_fim -= 1
total_dias = dia_fim - dia_inicio
print(total_dias)

if minutos_inicio > 0:
  hora_inicio -= 1
  
total_minutos = (dia - (hora_inicio * minutos))
total_horas = total_minutos // hora
total_hora = total_minutos / hora
total_horas = total_minutos // hora

print(total_minutos)
print(total_horas)
  
