import json
from datetime import datetime

class Paciente:

  def __init__(self, id, nome, fone, nasc):
    self.__id = id
    self.__nome = nome
    self.__fone = fone
    self.__nasc = nasc

  def get_id(self):
    return self.__id

  def get_nome(self):
    return self.__nome

  def get_fone(self):
    return self.__fone

  def get_nasc(self):
    return self.__nasc

  def set_id(self, id):
    self.__id = id

  def set_nome(self, nome):
    self.__nome = nome

  def set_fone(self, fone):
    self.__fone = fone

  def set_nasc(self, nasc):
    self.__nasc = nasc

  def __str__(self):
    return f"\n{self.__id} - {self.__nome} - {self.__fone} - {self.__nasc.strftime('%d/%m/%Y')}\n"

  def dicionario(self):
    return {
      "id": self.__id,
      "nome": self.__nome,
      "fone": self.__fone,
      "nasc": self.__nasc.strftime("%d/%m/%Y")
    }


class NPaciente:
  __pacientes = []

  @classmethod
  def inserir(cls, obj):
    NPaciente.abrir()
    id = 0
    for paciente in cls.__pacientes:
      if paciente.get_id() > id: id = paciente.get_id()
    obj.set_id(id + 1)
    cls.__pacientes.append(obj)
    NPaciente.salvar()

  @classmethod
  def listar(cls):
    NPaciente.abrir()
    return cls.__pacientes

  @classmethod
  def listar_id(cls, id):
    NPaciente.abrir()
    for paciente in cls.__pacientes:
      if paciente.get_id() == id: return paciente
    return None

  @classmethod
  def atualizar(cls, obj):
    NPaciente.abrir()
    paciente = cls.listar_id(obj.get_id())
    if paciente is not None:
      paciente.set_nome(obj.get_nome())
      paciente.set_fone(obj.get_fone())
      paciente.set_nasc(obj.get_nasc())
      NPaciente.salvar()

  @classmethod
  def excluir(cls, obj):
    NPaciente.abrir()
    paciente = cls.listar_id(obj.get_id())
    if paciente is not None:
      cls.__pacientes.remove(paciente)
      NPaciente.salvar()

  @classmethod
  def abrir(cls):
    try:
      cls.__pacientes = []
      with open("pacientes.json", mode="r") as f:
        s = json.load(f)
        for paciente in s:
          c = Paciente(paciente["id"], paciente["nome"], paciente["fone"],
                       datetime.strptime(paciente["nasc"], "%d/%m/%Y"))
          cls.__pacientes.append(c)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("pacientes.json", mode="w") as f:
      json.dump(cls.__pacientes, f, default=Paciente.dicionario)

  @classmethod
  def Aniversariantes(cls, mes):
    NPaciente.abrir()
    aniversariantes = []
    for paciente in cls.__pacientes:
      if paciente.get_nasc().month == mes:
        aniversariantes.append(paciente)
    return aniversariantes


class UI:

  @classmethod
  def Main(cls):
    op = 99
    while (op != 0):
      op = UI.Menu()
      if op == 1: UI.PacienteInserir()
      if op == 2: UI.PacienteListar()
      if op == 3: UI.PacienteAtualizar()
      if op == 4: UI.PacienteExcluir()
      if op == 5: UI.UIaniversariantes()

  @classmethod
  def Menu(cls):
    print(
      "1 - Inserir Paciente\n2 - Listar v\n3 - Atualizar Pacientes\n4 - Excluir Paciente\n5 - Aniversariantes \n0 - Sair"
    )
    return int(input())

  @classmethod
  def PacienteInserir(cls):
    nome = input("nome: ")
    fone = input("fone: ")
    nasc = datetime.strptime(input("nasc: "), "%d/%m/%Y")
    paciente = Paciente(0, nome, fone, nasc)
    NPaciente.inserir(paciente)

  @classmethod
  def PacienteListar(cls):
    for paciente in NPaciente.listar():
      print(paciente)

  @classmethod
  def PacienteAtualizar(cls):
    UI.PacienteListar()
    id = int(input("Id do paciente a ser atualizado: "))
    nome = input("Novo nome: ")
    fone = input("Novo fone: ")
    nasc = datetime.strptime(input("nasc: "), "%d/%m/%Y")
    paciente = Paciente(id, nome, fone, nasc)
    NPaciente.atualizar(paciente)

  @classmethod
  def PacienteExcluir(cls):
    UI.PacienteListar()
    id = int(input("Id do paciente a ser excluído: "))
    paciente = Paciente(id, "", "", "")
    NPaciente.excluir(paciente)

  @classmethod
  def UIaniversariantes(cls):
    mes = int(input("Informe o mês para a lista de aniversariantes: "))
    print('-----Aniversariantes do mês-----\n')
    for paciente in NPaciente.Aniversariantes(mes):
      print(paciente)
      
UI.Main()
