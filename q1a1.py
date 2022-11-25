dia_inicio, horario_inicio = '1 2:2:2'.split()
dia_fim, horario_fim = '2 2:2:2'.split()

#dia_inicio, horario_inicio = input().split()
#dia_fim, horario_fim = input().split()

dia_inicio, dia_fim = int(dia_inicio), int(dia_fim)

hora_inicio, minutos_inicio, segundos_inicio = map(int, horario_inicio.split(':'))

hora_fim, minutos_fim, segundos_fim = map(int, horario_fim.split(':'))

minuto = 60
hora = minuto * 60

hora_inicio_em_segundos = segundos_inicio + (minutos_inicio * minuto) + (hora_inicio * hora)

hora_fim_em_segundos = segundos_fim + (minutos_fim * minuto) + (hora_fim * hora)

total_em_segundos = hora_fim_em_segundos - hora_inicio_em_segundos

hora_segundos = total_em_segundos % (24 * hora)
total_hora = hora_segundos // hora
minuto_segundos = total_em_segundos % hora
total_minuto = minuto_segundos // minuto
total_segundo = minuto_segundos % 60


dias_diferenca = (dia_fim - dia_inicio) - 1

total_dias = dias_diferenca + 1 if dias_diferenca < 0 or total_hora == 0 else dias_diferenca

if dia_inicio <= dia_fim and (total_em_segundos > 0 or total_dias > 0):
  print(f"{str(total_dias)} dia(s)")
  print(f"{str(total_hora)} hora(s)")
  print(f"{str(total_minuto)} minuto(s)")
  print(f"{str(total_segundo)} segundo(s)")
else:
  print("Data inválida!")
