class Quadrado:
  def __init__(self):
    self.__lado = 1
  def set_lado(self, lado):
    if lado > 0: self.__lado = lado  # 7 pontos
    else: raise ValueError()         # 7 pontos
  def get_lado(self):
    return self.__lado               # 7 pontos
  def calc_area(self):
    return self._lado ** 2           # 7 pontos
  def __str__(self):
    return f"Quadrado de lado = {self.__lado}" # 7

class UI:
  def main():
    for k in range(10):
      x = Quadrado() # 5 pontos
      x.set_lado(float(input("Informe o valor do lado: "))) # 5 pontos
      print(x.calc_area()) # 5 pontos
      
UI.main()    


    