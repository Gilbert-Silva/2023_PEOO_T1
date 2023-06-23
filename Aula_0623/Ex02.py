import enum

class Estacao(enum.Enum):
  OUTONO = 1
  INVERNO = 2
  PRIMAVERA = 3
  VERAO = 4

x = Estacao.OUTONO
print(x)
