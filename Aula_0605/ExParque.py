class Parque:
  def __init__(self, dia, altura):    # atributo  - 5
    self.__dia = "dom"                # init      - 5
    self.__altura = 1.5               # validação - 5
    self.set_dia(dia)                 # set       - 5
    self.set_altura(altura)           # get       - 5
  def set_dia(self, dia):             # valor     - 5
    dias = ["dom", "seg", "ter", "qua", "qui", "sex", "sab"]
    if dia in dias: self.__dia = dia  # str       - 5
    else: raise ValueError()  
  def set_altura(self, altura):  
    if 0.5 <= altura <= 2.20: self.__altura = altura
    else: raise ValueError()  
  def get_dia(self):
    return self.__dia
  def get_altura(self):
    return self.__altura
  def valor(self):
    if self.__dia == "qua": return 65
    if self.__altura <= 1.4: return 50
    return 100
  def __str__(self):
    return f"Dia = {self.__dia}, Altura = {self.__altura}"

    
class UI: 
 def main():
   d = input("Informe o dia: ")         # input - 5 pontos
   h = float(input("Informe a altura: "))
   x = Parque(d, h)                     # parque - 5 pontos
   print(x.valor())                     # valor  - 5 pontos

UI.main()
