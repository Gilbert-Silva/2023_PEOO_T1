class Pacote:

  def __init__(self, id, descricao):
    self.__id = id
    self.__descricao = descricao

  def get_id(self):
    return self.__id

  def set_descricao(self, descricao):
    self.__descricao = descricao

  def get_descricao(self):
    return self.__descricao

  def __str__(self):
    return f"{self.__id}: {self.__descricao}"

"""
class NPacote:

  def __init__(self):
    self.__pacotes = []

  def inserir(self, pacote):
    self.__pacotes.append(pacote)

  def listar(self):
    return self.__pacotes
"""
class NPacote:
  __pacotes = []
  @classmethod
  def inserir(cls, pacote):
    cls.__pacotes.append(pacote)
  @classmethod
  def listar(cls):
    return cls.__pacotes

class Cinema:

  def __init__(self, id, descricao):
    self.__id = id
    self.__descricao = descricao

  def get_id(self):
    return self.__id

  def set_descricao(self, descricao):
    self.__descricao = descricao

  def get_descricao(self):
    return self.__descricao

  def __str__(self):
    return f"{self.__id} - {self.__descricao}"


class NCinema:

  def __init__(self):
    self.__cinemas = []

  def inserir(self, cinema):
    self.__cinemas.append(cinema)

  def listar(self):
    return self.__cinemas


a = Pacote(1, "Seridó")
b = Pacote(2, "Disney")
#x = NPacote()
#y = NPacote()
#x.inserir(a)
#x.inserir(b)
#for pacote in x.listar():
#  print(pacote)
NPacote.inserir(a)
NPacote.inserir(b)
for pacote in NPacote.listar():
  print(pacote)

