import json


class Cliente:

  def __init__(self, id, nome):
    self.id = id
    self.nome = nome

  def __str__(self):
    return f"{self.id} - {self.nome}"


a = Cliente(1, "Guilherme")
b = Cliente(2, "Izabel")

x = [a, b]
with open("clientes.json", mode="w") as f:
  json.dump(x, f, default=vars)

x = []
with open("clientes.json", mode="r") as f:
  s = json.load(f)
  for cliente in s:
    c = Cliente(cliente["id"], cliente["nome"])
    #c = Cliente(**cliente)
    x.append(c)

for c in x:
  print(c)
"""
print(a)
print(vars(a))
print(a.__dict__)

print(b)
print(vars(b))
print(b.__dict__)
"""