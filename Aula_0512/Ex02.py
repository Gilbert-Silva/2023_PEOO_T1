class Triangulo:
  def __init__(self):
    self.__b = 0
    self.__h = 0
  def set_base(self, v):
    if (v >= 0): self.__b = v
    else: raise ValueError()  
  def set_altura(self, v):
    if (v >= 0): self.__h = v
    else: raise ValueError()
  def get_base(self):
    return self.__b
  def get_altura(self):
    return self.__h
  def calc_area(self):
    return self.__b * self.__h / 2

class UI:
  @staticmethod
  def main():
    x = Triangulo()
    #x.b = -10
    #x.h = 20
    x.set_base(10)
    x.set_altura(20)
    print(x.calc_area())
    y = Triangulo()
    y.set_base(15)
    y.set_altura(20)
    print(y.get_base())
    print(y.get_altura())
    print(y.calc_area())

UI.main()