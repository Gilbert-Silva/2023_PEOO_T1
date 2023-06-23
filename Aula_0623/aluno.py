class Aluno:
  def __init__(self, nome):
    self.__nome = nome;
  def __str__(self):
    return f"{self.__nome}"
    