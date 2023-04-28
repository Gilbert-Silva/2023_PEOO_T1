print("Digite o horário no formato hh:mm")
s = input().split(":")
h = int(s[0])
m = int(s[1])
if h >= 0 and h <= 23 and m >= 0 and m <= 59:
  print("Hora válida")
  if h > 12: h = h - 12
  print(h, m) 
  ph = 30 * h + 0.5 *m # posição do ponteiro das horas
  pm = 6 * m  # posição do ponteiro dos minutos
  print("Ponteiro das horas", ph)
  print("Ponteiro dos minutos", pm)
  if ph > pm: ang = ph - pm # ângulo entre os ponteiros
  else: ang = pm - ph       # quem andou mais - quem andou menos
  if ang > 180: ang = 360 - ang  
  print("Ângulo entre ponteiros", ang)

else:
  print("Hora inválida")
