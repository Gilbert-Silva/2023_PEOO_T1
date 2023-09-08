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
  def __init__(self):
    self.__clientes = []         # lista de clientes inicia vazia
  def inserir(self, obj):
    self.__clientes.append(obj)  # insere um cliente (obj) na lista
  def listar(self):
    return self.__clientes       # retorna a lista de clientes
  def listar_id(self, id):
    for cliente in self.__clientes:
      if cliente.get_id() == id: return cliente
    return None
  def atualizar(self, obj):
    cliente = self.listar_id(obj.get_id())
    cliente.set_nome(obj.get_nome())
    cliente.set_email(obj.get_email())
    cliente.set_fone(obj.get_fone())
  def excluir(self, obj):
   cliente = self.listar_id(obj.get_id())
   self.__clientes.remove(cliente)    

class UI:
  @classmethod
  def Main(cls):
    op = 0
    while(op != 99):
      op = UI.Menu()
  @classmethod
  def Menu(cls):
    print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 99-Sair")
    return int(input())
  @classmethod
  def ClienteListar(cls):
    pass
  @classmethod
  def ClienteInserir(cls):
    pass
  @classmethod
  def ClienteAtualizar(cls):
    pass
  @classmethod
  def ClienteExcluir(cls):
    pass

UI.Main()







