class Ingresso:
  def __init__(self, dia, hora):
    self.__dia = "dom"   # atributos - 5 pontos
    self.__hora = 17     # init      - 5 pontos
                         # validação - 5 pontos
    self.set_dia(dia)
    #if dia == "dom" or dia == "seg" or dia == "ter" or dia == "qua" or dia == "qui" or dia == "sex" or dia == "sab": self.__dia = dia
    #else: raise ValueError()  
    #dias = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]
    #if dia in dias: self.__dia = dia 
    self.set_hora(hora)
    #if 0 <= hora <= 23: self._hora = hora
    #else: raise ValueError()
  def set_dia(self, dia):   # set - 5 pontos
    if dia == "dom" or dia == "seg" or dia == "ter" or dia == "qua" or dia == "qui" or dia == "sex" or dia == "sab": self.__dia = dia
    else: raise ValueError() 
  def set_hora(self, hora): 
    if 0 <= hora <= 23: self.__hora = hora
    else: raise ValueError()
  def get_dia(self):        # get - 5 pontos
    return self.__dia
  def get_hora(self):
    return self.__hora
  def valor(self):          # calculo - 5 pontos
    if self.__dia == "qui": return 6
    if self.__hora <= 16: return 5
    return 10
  def __str__(self):        # str - 5 pontos
    return f"Dia = {self.__dia} - Hora = {self.__hora}"
    
class UI: 
 def main():
   d = input("Informe o dia: ")         # input - 5 pontos
   h = int(input("Informe a hora: "))
   x = Ingresso(d, h)                   # ingresso - 5 pontos
   print(x.valor())                     # valor - 5 pontos

UI.main()
