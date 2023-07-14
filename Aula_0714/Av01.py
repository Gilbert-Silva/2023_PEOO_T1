import datetime

class Postagem:
  def __init__(self, texto, data, likes): # 10
    self.__texto = texto
    self.__datahora = data
    self.__likes = likes
  def set_texto(self, texto): # 10
    self.__texto = texto
  def set_datahora(self, data):
    self.__datahora = data
  def set_likes(self, likes):
    self.__likes = likes
  def get_texto(self):
    return self.__texto 
  def get_datahora(self):
    return self.__datahora 
  def get_likes(self):
    return self.__likes 
  def __str__(self): # 10
    return f"{self.__texto} {self.__datahora} {self.__likes}"

class Usuario:
  def __init__(self, nome, email): # 10
    self.__nome = nome
    self.__email = email
    self.__postagens = []
  def inserir(self, p): # 10
    self.__postagens.append(p)
  def listar(self):     # 10
    return self.__postagens
  def media_likes(self): # 10
    if len(self.__postagens) == 0: return 0
    total = 0  
    for p in self.__postagens:
      total += p.get_likes()
    return total / len(self.__postagens)
  def postagens_hoje(self): # 10
    r = []
    for p in self.__postagens:
      if p.get_datahora().date() == datetime.datetime.today().date():
        r.append(p)
    return r    

a = Postagem("Sextou!!!", datetime.datetime.today(), 10)
b = Postagem("Próxima semana tem wInfo", datetime.datetime(2023,7,7), 100)
c = Postagem("Eu gosto de programar em Python", datetime.datetime.today(), 1700)
u = Usuario("Fernando", "fernando@email.com")
u.inserir(a)
u.inserir(b)
u.inserir(c)
print("Postagens")
for p in u.listar(): print(p)
print("\nMédia de Likes")
print(u.media_likes())
print("\nPostagens de Hoje")
for p in u.postagens_hoje(): print(p)




