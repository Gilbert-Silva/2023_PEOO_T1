class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_fone(self): return self.__fone
  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_email(self, email): self.__email = email
  def set_fone(self, fone): self.__fone = fone
  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class NCliente:
  __clientes = []         # lista de clientes inicia vazia
  @classmethod
  def inserir(cls, obj):
    cls.__clientes.append(obj)  # insere um cliente (obj) na lista
  @classmethod
  def listar(cls):
    return cls.__clientes       # retorna a lista de clientes
  @classmethod
  def listar_id(cls, id):
    for cliente in cls.__clientes:
      if cliente.get_id() == id: return cliente
    return None
  @classmethod
  def atualizar(cls, obj):
    cliente = cls.listar_id(obj.get_id())
    cliente.set_nome(obj.get_nome())
    cliente.set_email(obj.get_email())
    cliente.set_fone(obj.get_fone())
  @classmethod
  def excluir(cls, obj):
   cliente = cls.listar_id(obj.get_id())
   cls.__clientes.remove(cliente)    


class UI:
  @classmethod
  def Main(cls):
    op = 0
    while(op != 99):
      op = UI.Menu()
      if op == 1: UI.ClienteInserir()
      if op == 2: UI.ClienteListar()
      if op == 3: UI.ClienteAtualizar()
      if op == 4: UI.ClienteExcluir()
  @classmethod
  def Menu(cls):
    print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 99-Sair")
    return int(input())
  @classmethod
  def ClienteInserir(cls):
    id = int(input("Id: "))
    nome = input("Nome: ")
    email = input("E-mail: ")
    fone = input("fone: ")
    cliente = Cliente(id, nome, email, fone)
    NCliente.inserir(cliente)
  @classmethod
  def ClienteListar(cls):
    for cliente in NCliente.listar():
      print(cliente)
  @classmethod
  def ClienteAtualizar(cls):
    pass
  @classmethod
  def ClienteExcluir(cls):
    pass

UI.Main()

"""

a = Cliente(1, "Julia", "julia@email.com", "912345678")        #  Cliente.__init__
b = Cliente(2, "Fernando", "fernando@email.com", "987654321")  #  Cliente.__init__
x = NCliente()  # NCliente.__init__
# inserindo os clientes da lista de clientes
x.inserir(a)
x.inserir(b)
# listando os clientes cadastrados
for cliente in x.listar(): print(cliente)
# outro cliente com os dados atualizados e mesmo id
c = Cliente(2, "Fernando", "fernando@ifrn.edu.br", "987654321") 
x.atualizar(c) # atualiza para os novos dados
# listando os clientes cadastrados
for cliente in x.listar(): print(cliente)
# removendo um cliente da lista
d = Cliente(2, "", "", "")
x.excluir(d) # remove o cliente com o id 
# listando os clientes cadastrados
for cliente in x.listar(): print(cliente)



"""






