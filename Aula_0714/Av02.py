import datetime

class ContaPagar:
  def __init__(self, fornecedor, vencimento, valor): # 10
    self.__fornecedor = fornecedor
    self.__vencimento = vencimento
    self.__valor = valor
  def set_fornecedor(self, fornecedor): # 10
    self.__fornecedor = fornecedor
  def set_vencimento(self, vencimento):
    self.__vencimento = vencimento
  def set_valor(self, valor):
    self.__valor = valor
  def get_fornecedor(self):
    return self.__fornecedor 
  def get_vencimento(self):
    return self.__vencimento 
  def get_valor(self):
    return self.__valor 
  def __str__(self): # 10
    return f"{self.__fornecedor} {self.__vencimento} {self.__valor}"

class Empresa:
  def __init__(self, nome, cnpj): # 10
    self.__nome = nome
    self.__cnpj = cnpj
    self.__contas = []
  def inserir(self, c): # 10
    self.__contas.append(c)
  def listar(self):     # 10
    return self.__contas
  def total(self): # 10
    total = 0  
    for c in self.__contas:
      total += c.get_valor()
    return total 
  def a_vencer(self): # 10
    r = []
    for c in self.__contas:
      if c.get_vencimento().date() > datetime.datetime.today().date():
        r.append(c)
    return r    

a = ContaPagar("Telefone", datetime.datetime(2023,7,20), 50)
b = ContaPagar("Telefone", datetime.datetime(2023,6,20), 55)
c = ContaPagar("Energia", datetime.datetime(2023,7,20), 250)

e = Empresa("IF", "1234567890")
e.inserir(a)
e.inserir(b)
e.inserir(c)
print("Contas")
for c in e.listar(): print(c)
print("\nTotal")
print(e.total())
print("\nContas a vencer")
for c in e.a_vencer(): print(c)




