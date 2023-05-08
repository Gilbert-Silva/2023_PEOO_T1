class Triangulo:
  def __init__(self):
    self.b = 0
    self.h = 0
  def calc_area(self):
    return self.b * self.h / 2

x = Triangulo()
x.b = 10
x.h = 20
print(x, x.b, x.h)
print(x.b * x.h / 2)
print(x.calc_area())
y = Triangulo()
y.b = 15
y.h = 25
print(y, y.b, y.h)
print(y.b * y.h / 2)
print(y.calc_area())
z = x
z.b = 50
print(z)
print(x.b)

import math
print(math.pi)

raio = 3
area = math.pi * raio**2
circ = 2 * math.pi * raio
print(area)
print(circ)

