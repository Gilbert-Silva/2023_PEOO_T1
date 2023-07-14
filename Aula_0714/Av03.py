class Usuario:
  def __init__(self, id, nome, email):
    self.__id = id
    self.__nome = nome
    self.__email = email

class NUsuario:
  def __init__(self):
    self.__usuarios = []
  def inserir(self, u):
    self.__usuarios.append(u)
  def listar(self):
    return self.__usuarios

class UI:
  @staticmethod
  def main():
    op = 10
    while (op != 0):
      op = UI.menu()
      if op == 1: UI.inserir_usuario()
      if op == 2: UI.listar_usuario()  
    
  @staticmethod
  def menu():
    print("0 - fim, 1 - Inserir usuário, 2 - Listar usuário")
    return int(input())
    
  @staticmethod
  def inserir_usuario():
    id = int(input("Id: "))
    nome = input("Nome: ")
    email = input("Email: ")
    u = Usuario(id, nome, email)
    print(u)
    
  @staticmethod
  def listar_usuario():
    pass

UI.main()