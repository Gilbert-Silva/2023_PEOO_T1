import datetime

class Amigo:
  def __init__(self, nome, nasc):
    self.__nome = nome
    self.__nasc = nasc
  def get_nasc(self):
    return self.__nasc
  def __str__(self):
    return f"{self.__nome} - {self.__nasc}"

class UI:
  def main():
    amigos = []
    for k in range(1, 3):
      print(f"Informe o nome do {k}º amigo")
      nome = input()
      print(f"Informe o nascimento do {k}º amigo dd/mm/aaaa")
      nasc = datetime.datetime.strptime(input(), "%d/%m/%Y")
      a = Amigo(nome, nasc)
      amigos.append(a)
    print(*amigos)
    mais_novo = amigos[0]
    for amigo in amigos:
      if amigo.get_nasc() > mais_novo.get_nasc():
        mais_novo = amigo
    print(mais_novo)    


UI.main()
