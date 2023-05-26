class Pais:
  def __init__(self):
    self.nome = "nome do país"
    self.__pop = 1
    self.area = 1
  def set_pop(self, x):
    if x > 0: self.__pop = x
  def get_pop(self):
    return self.__pop
  def dens_demografica(self):
    return self.__pop / self.area
  def __str__(self):
    return f"{self.nome} {self.__pop} hab {self.area} km2"
    
a = Pais()
a.nome = input()
#a.pop = 214000
a.set_pop(int(input()))
#print(a.get_pop())
a.area = float(input())

for k in range(9):
  b = Pais()
  b.nome = input()
  b.set_pop(int(input()))
  b.area = float(input())
  if b.dens_demografica() > a.dens_demografica(): a = b

print(a)  
